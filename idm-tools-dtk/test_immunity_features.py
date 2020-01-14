import unittest
__unittest = True

from test_idm_tools_dtk import IdmToolsDtkTest

from immunity_feature_configuration import ImmunityFeatureConfiguration, ImmunityFeatureKeys
from immunity_decay_feature_configuration import ImmuneDecayFeatureConfiguration, ImmuneDecayKeys

IMMUNITY_ENABLE_KEY = ImmunityFeatureKeys.enable
DECAY_ENABLE_KEY = ImmuneDecayKeys.enable

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