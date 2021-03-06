import unittest

from aguaclara.design.floc import Flocculator
from aguaclara.core.units import unit_registry as u


class FlocTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        self.floc = Flocculator()

    def test_vel_grad_avg(self):
        self.assertAlmostEqual(self.floc.vel_grad_avg, 118.71480891150065 * (u.s ** -1))

    def test_retention_time(self):
        self.assertAlmostEqual(self.floc.retention_time,
                               311.6713099170526 * u.s)

    def test_vol(self):
        self.assertAlmostEqual(self.floc.vol, 6.233426198341053 * u.m**3)

    def test_l_max_vol(self):
        self.assertAlmostEqual(self.floc.l_max_vol, 3.463014554633918 * u.m)

    def test_channel_l(self):
        self.assertAlmostEqual(self.floc.channel_l, 3.463014554633918 * u.m)

    def test_w_min_hs_ratio(self):
        self.assertAlmostEqual(self.floc.w_min_hs_ratio,
                               11.026896890543643 * u.cm)

    def test_w_min(self):
        self.assertAlmostEqual(self.floc.w_min, 45 * u.cm)

    def test_channel_n(self):
        self.assertEqual(self.floc.channel_n, 2)

    def test_w_total(self):
        self.assertAlmostEqual(self.floc.w_total, 0.9 * u.m)

    def channel_w(self):
        self.assertAlmostEqual(self.floc.channel_w, 0.45 * u.m)

    def test_expansion_h_max(self):
        self.assertAlmostEqual(self.floc.expansion_h_max,
                               1.171475181753684 * u.m)

    def test_expansion_n(self):
        self.assertAlmostEqual(self.floc.expansion_n, 2)

    def test_expansion_h(self):
        self.assertAlmostEqual(self.floc.expansion_h, 100 * u.cm)

    def test_baffle_s(self):
        self.assertAlmostEqual(self.floc.baffle_s, 19.524586362561394 * u.cm)

    def test_obstacle_n(self):
        self.assertAlmostEqual(self.floc.obstacle_n, 1)
