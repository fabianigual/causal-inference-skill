"""Comprobaciones numéricas de los ejemplos, sin atribuirles identificación causal.

Ejecutar desde la raíz: python -m unittest discover -s tests -v.
Requiere las dependencias básicas; no instala ni prueba CausalML o differences.
"""
from pathlib import Path
import sys
import unittest

import numpy as np
import pandas as pd
from scipy import integrate, stats

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from formulas_basicas import (welch_ci, independent_t_power,
                             independent_t_sample_size)
from ejemplo_did import did_2x2_panel
from ejemplo_psm_diagnosticos import greedy_pairs, balance_table


class InferenciaBasica(unittest.TestCase):
    def test_welch_con_varianzas_y_tamanos_distintos(self):
        rng = np.random.default_rng(20261020)
        for _ in range(100):
            x = rng.normal(0.3, 2, rng.integers(5, 100))
            y = rng.normal(0, 0.5, rng.integers(5, 100))
            result = welch_ci(x, y)
            ref = stats.ttest_ind(x, y, equal_var=False).confidence_interval()
            np.testing.assert_allclose([result["ci_low"], result["ci_high"]],
                                       [ref.low, ref.high], rtol=1e-12, atol=1e-12)

    def test_poder_con_integracion_independiente(self):
        # Integra Z/sqrt(V/df), sin usar la CDF de t no central como referencia.
        for n1, n0, delta in [(2, 3, 0), (5, 9, .3), (30, 50, .5),
                               (100, 150, 2), (2, 2, 10)]:
            with self.subTest(n1=n1, n0=n0, delta=delta):
                df = n1 + n0 - 2
                critical = stats.t.ppf(.975, df)
                shift = delta * np.sqrt(n1 * n0 / (n1 + n0))

                def integrand(v):
                    bound = critical * np.sqrt(v / df)
                    return (stats.norm.cdf(-bound - shift)
                            + stats.norm.sf(bound - shift)) * stats.chi2.pdf(v, df)

                # Evita que la cuadratura omita la masa de chi2 con muchos df.
                # Masa total excluida <= 2e-12; tolerancia admite error numérico
                # de las rutinas t no centrales en colas extremas.
                low, high = stats.chi2.ppf([1e-12, 1 - 1e-12], df)
                ref = integrate.quad(integrand, low, high, epsabs=1e-10)[0]
                np.testing.assert_allclose(independent_t_power(delta, 1, n1, n0),
                                           ref, rtol=1e-6, atol=1e-9)

    def test_tamano_alcanza_poder_tras_redondear(self):
        for ratio in [.25, 1, 4]:
            for delta in [.1, .3, 1]:
                result = independent_t_sample_size(delta, 1, ratio=ratio)
                self.assertGreaterEqual(result["power_achieved"], .8)

    def test_did_coincide_con_cuatro_medias(self):
        rng = np.random.default_rng(20261020)
        a = np.repeat([0, 1], 40)
        for _ in range(100):
            pre = rng.normal(size=80)
            post = .6 * pre + rng.normal(size=80)
            result = did_2x2_panel(pre, post, a)
            contrast = ((post[a == 1].mean() - pre[a == 1].mean())
                        - (post[a == 0].mean() - pre[a == 0].mean()))
            self.assertAlmostEqual(result["estimate"], contrast, places=12)
            variance = sum(np.var((post - pre)[a == arm], ddof=1) / 40
                           for arm in [0, 1])
            self.assertAlmostEqual(result["se"] ** 2, variance, places=12)

    def test_did_incorpora_covarianza_del_panel(self):
        pre = np.array([0., 10., 20., 30., 0., 10., 20., 30.])
        change = np.array([0., 1., 0., 1., 1., 2., 1., 2.])
        result = did_2x2_panel(pre, pre + change, np.repeat([0, 1], 4))
        self.assertAlmostEqual(result["estimate"], 1)
        self.assertAlmostEqual(result["se"] ** 2, 1 / 6)


class DisenoMatching(unittest.TestCase):
    def test_score_constante_admite_pares_exactos(self):
        data = pd.DataFrame({"treated": [0, 0, 1, 1, 1],
                             "logit_ps": [0.] * 5}, index=[10, 20, 30, 40, 50])
        pairs = greedy_pairs(data)
        self.assertEqual(len(pairs), 2)
        self.assertTrue(pairs.distance.eq(0).all())
        self.assertTrue(pairs.caliper_absolute.eq(0).all())
        self.assertTrue(pairs.treated_id.is_unique)
        self.assertTrue(pairs.control_id.is_unique)
        self.assertTrue(data.loc[pairs.treated_id, "treated"].eq(1).all())
        self.assertTrue(data.loc[pairs.control_id, "treated"].eq(0).all())
        pd.testing.assert_frame_equal(pairs, greedy_pairs(data))

    def test_caliper_y_ausencia_de_reutilizacion(self):
        data = pd.DataFrame({"treated": [0, 0, 0, 1, 1, 1],
                             "logit_ps": [0., 1., 2., .01, 1.01, 9.]})
        pairs = greedy_pairs(data)
        self.assertEqual(len(pairs), 2)
        self.assertTrue((pairs.distance <= pairs.caliper_absolute).all())
        self.assertTrue(pairs.treated_id.is_unique and pairs.control_id.is_unique)
        np.testing.assert_allclose(pairs.distance, .01)

    def test_sin_soporte_no_inventa_pares(self):
        data = pd.DataFrame({"treated": [0, 0, 1, 1],
                             "logit_ps": [-10., -9., 9., 10.]})
        self.assertTrue(greedy_pairs(data).empty)

    def test_balance_con_denominador_pre_fijo(self):
        before = pd.DataFrame({"treated": [0, 0, 0, 1, 1, 1],
                               "x": [0., 2., 4., 1., 3., 9.]})
        after = before.loc[[0, 1, 3, 4]]
        result = balance_table(before, after, ["x"]).iloc[0]
        # Varianzas pre: 4 y 52/3. Medias post: 1 y 2.
        reference = np.sqrt((4 + 52 / 3) / 2)
        self.assertAlmostEqual(result.sd_reference, reference)
        self.assertAlmostEqual(result.smd_post, 1 / reference)

    def test_balance_referencia_cero_con_diferencia(self):
        data = pd.DataFrame({"treated": [0, 0, 1, 1], "x": [0., 0., 1., 1.]})
        result = balance_table(data, data, ["x"]).iloc[0]
        self.assertTrue(result.reference_zero)
        self.assertTrue(np.isnan(result.smd_post))

    def test_matching_basal_puede_alterar_did(self):
        # Caso construido: efecto cero, niveles persistentes distintos y ruido
        # basal de media cero por grupo. El post vuelve al nivel de cada grupo.
        # Ilustra una posibilidad, no la frecuencia del sesgo en datos reales.
        data = pd.DataFrame({"treated": [0, 0, 0, 1, 1, 1],
                             "pre": [-1., 0., 1., 0., 1., 2.],
                             "post": [0., 0., 0., 1., 1., 1.]})
        original = did_2x2_panel(data.pre, data.post, data.treated)
        pairs = greedy_pairs(data, score_col="pre", caliper_sd=.01)
        matched = data.loc[list(pairs.treated_id) + list(pairs.control_id)]
        # El panel emparejado tiene cambios variables; admite Welch.
        result = did_2x2_panel(matched.pre, matched.post, matched.treated)
        self.assertAlmostEqual(original["estimate"], 0)
        self.assertAlmostEqual(result["estimate"], 1)


if __name__ == "__main__":
    unittest.main()
