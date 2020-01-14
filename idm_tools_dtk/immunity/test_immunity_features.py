import unittest
__unittest = True

from idm_tools_dtk.test_idm_tools_dtk import IdmToolsDtkTest

from idm_tools_dtk.immunity.immunity_feature_configuration import ImmunityFeatureConfiguration, ImmunityFeatureKeys
from idm_tools_dtk.immunity.immunity_decay_feature_configuration import ImmuneDecayFeatureConfiguration, ImmuneDecayKeys
from idm_tools_dtk.immunity.maternal_protection_configuration import MaternalProtectionConfiguration,\
    MaternalProtectionConfigurationLinear, MaternalProtectionConfigurationSigmoid,\
    MaternalProtectionKeys

from idm_tools_dtk.emod_simulation_configuration import EmodSimulationConfiguration

IMMUNITY_ENABLE_KEY = ImmunityFeatureKeys.enable
DECAY_ENABLE_KEY = ImmuneDecayKeys.enable
MATERNAL_PROTECTION_ENABLE_KEY = MaternalProtectionKeys.enable

class ImmunityFeatureTest(IdmToolsDtkTest):

    # region Immunity

    def test_immunity_disabled(self):
        disable_immunity = ImmunityFeatureConfiguration(enable_immunity=False)
        self.config_params = disable_immunity.get_config_params()
        self.assertEqual(1, len(self.config_params))
        self.assertIn(IMMUNITY_ENABLE_KEY, self.config_params,
                      f"key {IMMUNITY_ENABLE_KEY} should be in params. Instead {self.config_params}.")
        config_value = self.config_params[IMMUNITY_ENABLE_KEY]
        self.assertFalse(config_value, f"{IMMUNITY_ENABLE_KEY} should be set to False. Got {config_value}.")
        pass


    def test_immunity_enabled_specified(self):
        acqu_multiplier = 1.1
        mort_multiplier = 1.2
        trax_multiplier = 0.9
        enabled_immunity = ImmunityFeatureConfiguration(enable_immunity=True,
                                                        acquisition_multiplier=acqu_multiplier,
                                                        mortality_mutliplier=mort_multiplier,
                                                        transmission_multiplier=trax_multiplier)
        self.config_params = enabled_immunity.get_config_params()
        self.assertEqual(4, len(self.config_params))
        self.assertIn(IMMUNITY_ENABLE_KEY, self.config_params,
                      f"key {IMMUNITY_ENABLE_KEY} should be in params. Instead {self.config_params}.")
        config_value = self.config_params[IMMUNITY_ENABLE_KEY]
        self.assertTrue(config_value, f"{IMMUNITY_ENABLE_KEY} should be set to True. Got {config_value}.")
        for k in ImmunityFeatureKeys.all_keys:
            self.assertIn(k, self.config_params)
            if k == ImmunityFeatureKeys.acquisition_multiplier:
                self.assertEqual(self.config_params[k], acqu_multiplier, msg="Acquisition multiplier incorrect.")
            elif k == ImmunityFeatureKeys.mortality_multiplier:
                self.assertEqual(self.config_params[k], mort_multiplier, msg="Mortality multiplier incorrect.")
            elif k == ImmunityFeatureKeys.transmission_multiplier:
                self.assertEqual(self.config_params[k], trax_multiplier, msg="Transmission multiplier incorrect.")
        pass


    def test_immunity_enabled_specified_full_sim(self):
        acqu_multiplier = 1.1
        mort_multiplier = 1.2
        trax_multiplier = 0.9
        enabled_immunity = ImmunityFeatureConfiguration(enable_immunity=True,
                                                        acquisition_multiplier=acqu_multiplier,
                                                        mortality_mutliplier=mort_multiplier,
                                                        transmission_multiplier=trax_multiplier)
        self.assertEqual(4, len(enabled_immunity.get_config_params()))
        emod_sim = EmodSimulationConfiguration(immunity_config=enabled_immunity)
        self.config_params = emod_sim.get_parameters()
        self.assertIn(IMMUNITY_ENABLE_KEY, self.config_params,
                      f"key {IMMUNITY_ENABLE_KEY} should be in params. Instead {self.config_params}.")
        config_value = self.config_params[IMMUNITY_ENABLE_KEY]
        self.assertTrue(config_value, f"{IMMUNITY_ENABLE_KEY} should be set to True. Got {config_value}.")
        for k in ImmunityFeatureKeys.all_keys:
            self.assertIn(k, self.config_params)
            if k == ImmunityFeatureKeys.acquisition_multiplier:
                self.assertEqual(self.config_params[k], acqu_multiplier, msg="Acquisition multiplier incorrect.")
            elif k == ImmunityFeatureKeys.mortality_multiplier:
                self.assertEqual(self.config_params[k], mort_multiplier, msg="Mortality multiplier incorrect.")
            elif k == ImmunityFeatureKeys.transmission_multiplier:
                self.assertEqual(self.config_params[k], trax_multiplier, msg="Transmission multiplier incorrect.")
        pass


    def test_immunity_disabled_add_bad_keys(self):
        acqu_multiplier = 1.1
        mort_multiplier = 1.2
        trax_multiplier = 0.9
        disable_immunity = ImmunityFeatureConfiguration(enable_immunity=False,
                                                        acquisition_multiplier=acqu_multiplier,
                                                        mortality_mutliplier=mort_multiplier,
                                                        transmission_multiplier=trax_multiplier)
        self.config_params = disable_immunity.get_config_params()
        self.assertEqual(1, len(self.config_params))
        self.assertIn(IMMUNITY_ENABLE_KEY, self.config_params,
                      f"key {IMMUNITY_ENABLE_KEY} should be in params. Instead {self.config_params}.")
        config_value = self.config_params[IMMUNITY_ENABLE_KEY]
        self.assertFalse(config_value, f"{IMMUNITY_ENABLE_KEY} should be set to False. Got {config_value}.")
        pass


    # endregion

    # region Immune Decay

    def test_immune_decay_disabled(self):
        decay_feature = ImmuneDecayFeatureConfiguration(enable_decay=False)
        self.config_params = decay_feature.get_config_params()
        self.assertEqual(1, len(self.config_params))
        self.assertIn(DECAY_ENABLE_KEY, self.config_params)
        self.assertFalse(self.config_params[DECAY_ENABLE_KEY], "Enable config decay should be False.")
        pass


    def test_immune_decay_enabled_specified(self):
        ack_rate = 0.2,
        ack_duration_before = 5,
        ded_rate = 0.3,
        ded_duration_before = 6,
        txn_rate = 0.1,
        txn_duration_before = 7
        decay_feature = ImmuneDecayFeatureConfiguration(enable_decay=True,
                                                        acquisition_rate=ack_rate,
                                                        acquisition_duration_before=ack_duration_before,
                                                        mortality_rate=ded_rate,
                                                        mortality_duration_before=ded_duration_before,
                                                        transmission_rate=txn_rate,
                                                        transmission_duration_before=txn_duration_before)
        self.config_params = decay_feature.get_config_params()
        self.assertEqual(7, len(self.config_params))
        self.assertIn(DECAY_ENABLE_KEY, self.config_params)
        self.assertTrue(self.config_params[DECAY_ENABLE_KEY], "Enable config decay should be True.")
        self.assertEqual(ack_rate, self.config_params[ImmuneDecayKeys.acquisition_rate],
                         "Acquisition Rate should be correct.")
        self.assertEqual(ack_duration_before, self.config_params[ImmuneDecayKeys.acquisition_duration_before_decay],
                         "Acquisition duration before decay should be correct.")
        self.assertEqual(ded_rate, self.config_params[ImmuneDecayKeys.mortality_rate],
                         "Acquisition Rate should be correct.")
        self.assertEqual(ded_duration_before, self.config_params[ImmuneDecayKeys.mortality_duration_before_decay],
                         "Acquisition duration before decay should be correct.")
        self.assertEqual(txn_rate, self.config_params[ImmuneDecayKeys.transmission_rate],
                         "Acquisition Rate should be correct.")
        self.assertEqual(txn_duration_before, self.config_params[ImmuneDecayKeys.transmission_duration_before_decay],
                         "Acquisition duration before decay should be correct.")
        pass


    def test_immune_decay_enabled_specified_full_sim(self):
        ack_rate = 0.2,
        ack_duration_before = 5,
        ded_rate = 0.3,
        ded_duration_before = 6,
        txn_rate = 0.1,
        txn_duration_before = 7
        decay_feature = ImmuneDecayFeatureConfiguration(enable_decay=True,
                                                        acquisition_rate=ack_rate,
                                                        acquisition_duration_before=ack_duration_before,
                                                        mortality_rate=ded_rate,
                                                        mortality_duration_before=ded_duration_before,
                                                        transmission_rate=txn_rate,
                                                        transmission_duration_before=txn_duration_before)
        self.assertEqual(7, len(decay_feature.get_config_params()))
        emod_sim = EmodSimulationConfiguration(immunity_config=decay_feature)
        self.config_params = emod_sim.get_parameters()
        self.config_params = decay_feature.get_config_params()
        self.assertEqual(7, len(self.config_params))
        self.assertIn(DECAY_ENABLE_KEY, self.config_params)
        self.assertTrue(self.config_params[DECAY_ENABLE_KEY], "Enable config decay should be True.")
        self.assertEqual(ack_rate, self.config_params[ImmuneDecayKeys.acquisition_rate],
                         "Acquisition Rate should be correct.")
        self.assertEqual(ack_duration_before, self.config_params[ImmuneDecayKeys.acquisition_duration_before_decay],
                         "Acquisition duration before decay should be correct.")
        self.assertEqual(ded_rate, self.config_params[ImmuneDecayKeys.mortality_rate],
                         "Acquisition Rate should be correct.")
        self.assertEqual(ded_duration_before, self.config_params[ImmuneDecayKeys.mortality_duration_before_decay],
                         "Acquisition duration before decay should be correct.")
        self.assertEqual(txn_rate, self.config_params[ImmuneDecayKeys.transmission_rate],
                         "Acquisition Rate should be correct.")
        self.assertEqual(txn_duration_before, self.config_params[ImmuneDecayKeys.transmission_duration_before_decay],
                         "Acquisition duration before decay should be correct.")
        pass


    def test_immune_decay_disabled_specified(self):
        ack_rate = 0.2,
        ack_duration_before = 5,
        ded_rate = 0.3,
        ded_duration_before = 6,
        txn_rate = 0.1,
        txn_duration_before = 7
        decay_feature = ImmuneDecayFeatureConfiguration(enable_decay=False,
                                                        acquisition_rate=ack_rate,
                                                        acquisition_duration_before=ack_duration_before,
                                                        mortality_rate=ded_rate,
                                                        mortality_duration_before=ded_duration_before,
                                                        transmission_rate=txn_rate,
                                                        transmission_duration_before=txn_duration_before)
        self.config_params = decay_feature.get_config_params()
        self.assertEqual(1, len(self.config_params))
        self.assertIn(DECAY_ENABLE_KEY, self.config_params)
        self.assertFalse(self.config_params[DECAY_ENABLE_KEY], "Enable config decay should be True.")
        pass

    # endregion

    # region Maternal Protection
    def test_maternal_protection_disabled(self):
        maternal_protection = MaternalProtectionConfiguration(
            enable=False
        )
        self.config_params = maternal_protection.get_config_params()
        self.assertEqual(1, len(self.config_params))
        self.assertIn(MATERNAL_PROTECTION_ENABLE_KEY, self.config_params)
        self.assertFalse(self.config_params[MATERNAL_PROTECTION_ENABLE_KEY], "Maternal protection should be disabled.")
        pass

    def test_maternal_protection_linear_specified(self):
        good_slope = 0.05
        good_sus_zero = 0.1
        m_p = MaternalProtectionConfigurationLinear(slope=good_slope,
                                                    sus_zero=good_sus_zero)
        self.config_params = m_p.get_config_params()
        self.assertEqual(4, len(self.config_params))
        self.assertIn(MATERNAL_PROTECTION_ENABLE_KEY, self.config_params)
        self.assertTrue(self.config_params[MATERNAL_PROTECTION_ENABLE_KEY], "Maternal protection should be enabled.")
        self.assertEqual(self.config_params[MaternalProtectionKeys.type_enum],
                         MaternalProtectionKeys.enum_options.linear,
                         "Maternal protection type should be correct.")
        self.assertEqual(good_slope,
                         self.config_params[MaternalProtectionKeys.linear_slope],
                         "Maternal Linear Slope should be correct.")
        self.assertEqual(good_sus_zero,
                         self.config_params[MaternalProtectionKeys.linear_suszero],
                         "Maternal Linear Susceptibility on day 0 should be correct.")
        pass

    def test_maternal_protection_sigmoid_specified(self):
        good_halfmax = 180
        good_steep_fac = 20
        good_initial_susceptibility = 0.4
        maternal_config = MaternalProtectionConfigurationSigmoid(
            halfmax_age=good_halfmax,
            steepness_factor=good_steep_fac,
            initial_susceptibility=good_initial_susceptibility
        )
        self.config_params = maternal_config.get_config_params()
        self.assertEqual(5, len(self.config_params))
        self.assertIn(MATERNAL_PROTECTION_ENABLE_KEY, self.config_params)
        self.assertTrue(self.config_params[MATERNAL_PROTECTION_ENABLE_KEY], "Maternal protection should be enabled.")
        self.assertEqual(self.config_params[MaternalProtectionKeys.type_enum],
                         MaternalProtectionKeys.enum_options.sigmoid,
                         "Maternal protection type should be correct.")
        self.assertEqual(good_steep_fac,
                         self.config_params[MaternalProtectionKeys.sigmoid_steepness_factor],
                         "Maternal Sigmoid Steepfac should be correct.")
        self.assertEqual(good_initial_susceptibility,
                         self.config_params[MaternalProtectionKeys.sigmoid_initial_susceptibility],
                         "Maternal Sigmoid Initial Susceptibility should be correct.")
        self.assertEqual(good_halfmax,
                         self.config_params[MaternalProtectionKeys.sigmoid_halfmax],
                         "Maternal Sigmoid Halfmax should be correct.")
        pass

    # endregion
