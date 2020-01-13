import unittest
__unittest = True
from immunity_feature_configuration import ImmunityFeatureConfiguration, ImmunityFeatureKeys
from immunity_decay_feature_configuration import ImmuneDecayFeatureConfiguration, ImmuneDecayKeys
from maternal_protection_configuration import MaternalProtectionConfiguration,\
    MaternalProtectionConfigurationLinear, MaternalProtectionConfigurationSigmoid,\
    MaternalProtectionKeys
from initial_susceptibility_feature_configuration import SusceptibilityDistributionKeys, \
    InitialSusceptibilityFeatureConfiguration
from birth_feature_configuration import BirthKeys, \
    BirthRateTimeDependenceKeys, \
    BirthFeatureConfiguration, \
    BirthRateSinusoidalTimeDependenceFeatureConfiguration, \
    BirthRateBoxcarTimeDependenceFeatureConfiguration, \
    BirthRateNoTimeDependenceFeatureConfiguration, \
    BirthRateDependenceFeatureConfiguration, BirthRateDependenceKeys
from death_feature_configuration import DeathKeys, \
    DeathFeatureConfiguration, \
    DeathRateDependenceKeys, \
    DeathAgeAndGenderFeatureConfiguration, \
    DeathYearAgeGenderFeatureConfiguration
from individual_sampling_feature_configuration import IndividualSamplingKeys, \
    SamplingAgeGroupKeys, \
    IndividualSamplingFeatureConfiguration, \
    IndividualSamplingFixedFeatureConfiguration, \
    IndividualSamplingAgeGroupFeatureConfiguration, \
    IndividualSamplingAgeGroupSizeFeatureConfiguration, \
    IndividualSamplingPopulationSizeFeatureConfiguration, \
    IndividualSamplingImmuneStateFeatureConfiguration
from demographics_feature_configuration import DemographicsKeys, \
    DemographicsBuiltinFeatureConfiguration, \
    DemographicsCustomFeatureConfiguration


test_debug = False
IMMUNITY_ENABLE_KEY = "Enable_Immunity"
DECAY_ENABLE_KEY = "Enable_Immune_Decay"
MATERNAL_PROTECTION_ENABLE_KEY = "Enable_Maternal_Protection"
INITIAL_SUSCEPTIBILITY_ENABLE_KEY = "Enable_Initial_Susceptibility_Distribution"

class IdmToolsDtkTest(unittest.TestCase):
    def setUp(self):
        self.config_params = None
        pass

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

    # region Initial Susceptibility

    def test_initial_susceptibility_disabled(self):
        i_s = InitialSusceptibilityFeatureConfiguration(enable=False)
        self.config_params = i_s.get_config_params()
        self.assertEqual(1, len(self.config_params))
        self.assertIn(INITIAL_SUSCEPTIBILITY_ENABLE_KEY, self.config_params,
                      f"key {INITIAL_SUSCEPTIBILITY_ENABLE_KEY} should be in params. Instead {self.config_params}.")
        config_value = self.config_params[INITIAL_SUSCEPTIBILITY_ENABLE_KEY]
        self.assertFalse(config_value, f"{INITIAL_SUSCEPTIBILITY_ENABLE_KEY} should be set to False. Got {config_value}.")
        pass

    def test_initial_susceptibility_simple_specified(self):
        good_distro_params = {
            'distro_flag' : 3,
            'distro_param1' : 0.4,
            'distro_param2' : 0.1
        }
        i_s = InitialSusceptibilityFeatureConfiguration(
            enable=True,
            distribution_type=SusceptibilityDistributionKeys.enum_options.simple,
            simple_distro_params=good_distro_params
        )
        self.config_params = i_s.get_config_params()
        self.assertEqual(2, len(self.config_params))
        config_value = self.config_params[INITIAL_SUSCEPTIBILITY_ENABLE_KEY]
        self.assertTrue(config_value, "Initial Susceptibility Distribution should be enabled.")
        output_demo_params = i_s.get_demographics_params()
        for k in good_distro_params:
            self.assertIn(k, output_demo_params, f"Key {k} should be found in demo params. Had {output_demo_params}.")
            self.assertEqual(good_distro_params[k], output_demo_params[k], f"Values for {k} should be equal.")
        pass

    def test_initial_susceptibility_complex_specified(self):
        good_complex_tables = {
            'node1_distro' : [[1, 2, 3],[2, 3, 4],[3, 4, 5]],
            'node2_distro' : [[0, 1, 1],[0, 0, 1],[0, 0, 0]],
            'node3_distro' : [[0, 0, 1],[0, 1, 0],[1, 0, 0]]
        }
        i_s = InitialSusceptibilityFeatureConfiguration(
            enable=True,
            distribution_type=SusceptibilityDistributionKeys.enum_options.complex,
            complex_distribution_tables=good_complex_tables
        )
        self.config_params = i_s.get_config_params()
        self.assertEqual(2, len(self.config_params))
        config_value = self.config_params[INITIAL_SUSCEPTIBILITY_ENABLE_KEY]
        self.assertTrue(config_value, "Initial Susceptibility Distribution should be enabled.")
        output_demo_params = i_s.get_demographics_params()
        for k in good_complex_tables:
            self.assertIn(k, output_demo_params, f"Key {k} should be found in demo params. Had {output_demo_params}.")
            self.assertEqual(good_complex_tables[k], output_demo_params[k], f"Values for {k} should be equal.")
        pass

    # endregion

    # region BirthRateTimeDependence

    def test_birthrate_timedependence_none(self):
        t_d = BirthRateNoTimeDependenceFeatureConfiguration()
        self.config_params = t_d.get_config_params()
        self.assertIn(BirthRateTimeDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateTimeDependenceKeys.type_enum]
        self.assertEqual("NONE", config_value)
        missing_keys = [
            BirthRateTimeDependenceKeys.boxcar_end,
            BirthRateTimeDependenceKeys.boxcar_start,
            BirthRateTimeDependenceKeys.boxcar_amplitude,
            BirthRateTimeDependenceKeys.sinusoid_amplitude,
            BirthRateTimeDependenceKeys.sinusiod_phase
        ]
        for k in missing_keys:
            self.assertNotIn(k, self.config_params)
            pass
        pass

    def test_birthrate_timedependence_sinusoid(self):
        expected_phase = 90.1
        expected_amplitude = 12.3
        t_d = BirthRateSinusoidalTimeDependenceFeatureConfiguration(
            amplitude=expected_amplitude,
            phase=expected_phase
        )
        self.config_params = t_d.get_config_params()
        self.assertIn(BirthRateTimeDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateTimeDependenceKeys.type_enum]
        self.assertEqual(BirthRateTimeDependenceKeys.enum_options.sinusoid, config_value)
        self.assertEqual(expected_phase, self.config_params[BirthRateTimeDependenceKeys.sinusiod_phase])
        self.assertEqual(expected_amplitude, self.config_params[BirthRateTimeDependenceKeys.sinusoid_amplitude])
        missing_keys = [
            BirthRateTimeDependenceKeys.boxcar_end,
            BirthRateTimeDependenceKeys.boxcar_start,
            BirthRateTimeDependenceKeys.boxcar_amplitude
        ]
        for k in missing_keys:
            self.assertNotIn(k, self.config_params)
            pass
        pass

    def test_birthrate_timedependence_boxcar(self):
        expected_amplitude = 1.23
        expected_start = 90
        expected_end = 180
        t_d = BirthRateBoxcarTimeDependenceFeatureConfiguration(
            amplitude=expected_amplitude,
            start_time=expected_start,
            end_time=expected_end
        )
        self.config_params = t_d.get_config_params()
        self.assertIn(BirthRateTimeDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateTimeDependenceKeys.type_enum]
        self.assertEqual(BirthRateTimeDependenceKeys.enum_options.boxcar, config_value)
        self.assertEqual(expected_amplitude, self.config_params[BirthRateTimeDependenceKeys.boxcar_amplitude])
        self.assertEqual(expected_start, self.config_params[BirthRateTimeDependenceKeys.boxcar_start])
        self.assertEqual(expected_end, self.config_params[BirthRateTimeDependenceKeys.boxcar_end])
        missing_keys = [
            BirthRateTimeDependenceKeys.sinusoid_amplitude,
            BirthRateTimeDependenceKeys.sinusiod_phase
        ]
        for k in missing_keys:
            self.assertNotIn(k, self.config_params)
            pass
        pass

    # endregion

    # region BirthRateDependence

    def test_brd_fixed(self):
        brd = BirthRateDependenceFeatureConfiguration(enum_setting=BirthRateDependenceKeys.enum_options.fixed)
        self.config_params = brd.get_config_params()
        self.assertIn(BirthRateDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateDependenceKeys.type_enum]
        self.assertEqual(BirthRateDependenceKeys.enum_options.fixed, config_value)
        pass

    def test_brd_population_dependent(self):
        brd = BirthRateDependenceFeatureConfiguration(enum_setting=BirthRateDependenceKeys.enum_options.pop_dependent)
        self.config_params = brd.get_config_params()
        self.assertIn(BirthRateDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateDependenceKeys.type_enum]
        self.assertEqual(BirthRateDependenceKeys.enum_options.pop_dependent, config_value)
        pass

    def test_brd_demographic_dependent(self):
        brd = BirthRateDependenceFeatureConfiguration(enum_setting=BirthRateDependenceKeys.enum_options.demo_depdendent)
        self.config_params = brd.get_config_params()
        self.assertIn(BirthRateDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateDependenceKeys.type_enum]
        self.assertEqual(BirthRateDependenceKeys.enum_options.demo_depdendent, config_value)
        pass

    def test_brd_individual_pregancies(self):
        brd = BirthRateDependenceFeatureConfiguration(enum_setting=BirthRateDependenceKeys.enum_options.ind_pregnancies)
        self.config_params = brd.get_config_params()
        self.assertIn(BirthRateDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateDependenceKeys.type_enum]
        self.assertEqual(BirthRateDependenceKeys.enum_options.ind_pregnancies, config_value)
        pass

    def test_brd_indidividual_pregancies_age_year(self):
        brd = BirthRateDependenceFeatureConfiguration(
            enum_setting=BirthRateDependenceKeys.enum_options.ind_pregnancies_age_and_year)
        self.config_params = brd.get_config_params()
        self.assertIn(BirthRateDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateDependenceKeys.type_enum]
        self.assertEqual(BirthRateDependenceKeys.enum_options.ind_pregnancies_age_and_year, config_value)
        pass

    # endregion

    # region MaternalTransmission

    def test_maternal_transmission_enabled_default(self):
        test_probability = 0.0
        bc = BirthFeatureConfiguration(
            enable=True,
            maternal_transmission=True
        )
        self.config_params = bc.get_config_params()
        self.assertTrue(self.config_params[BirthKeys.maternal_transmission])
        self.assertTrue(self.config_params[BirthKeys.enable])
        self.assertIn(
            BirthKeys.maternal_transmission_probability,
            self.config_params
        )
        found_probability = self.config_params[BirthKeys.maternal_transmission_probability]
        self.assertEqual(test_probability, found_probability)
        pass

    def test_maternal_transmission_enabled_custom(self):
        test_probability = 0.3
        bc = BirthFeatureConfiguration(
            enable=True,
            maternal_transmission=True,
            maternal_transmission_probability=test_probability
        )
        self.config_params = bc.get_config_params()
        self.assertTrue(self.config_params[BirthKeys.maternal_transmission])
        self.assertIn(
            BirthKeys.maternal_transmission_probability,
            self.config_params
        )
        found_probability = self.config_params[BirthKeys.maternal_transmission_probability]
        self.assertEqual(test_probability, found_probability)
        pass

    # endregion

    # region Birth

    def test_birth_disabled(self):
        bf = BirthFeatureConfiguration(
            enable=False
        )
        self.config_params = bf.get_config_params()
        self.assertFalse(
            self.config_params[BirthKeys.enable]
        )
        self.assertEqual(
            len(self.config_params),
            1
        )
        pass

    def test_birth_defaults(self):
        expected_multiplier = 1.0
        expected_demographics_birth = False
        expected_maternal_transmission = False
        expected_time_dependence = BirthRateTimeDependenceKeys.enum_options.none
        bf = BirthFeatureConfiguration(
            enable=True
        )
        self.config_params = bf.get_config_params()
        self.assertEqual(
            len(self.config_params),
            5 # enable, multiplier, time dependence, demographics, maternal txn
        )
        self.assertIn(
            BirthKeys.x_birth,
            self.config_params
        )
        observed_multiplier = self.config_params[BirthKeys.x_birth]
        self.assertEqual(
            expected_multiplier,
            observed_multiplier
        )
        self.assertEqual(
            expected_demographics_birth,
            self.config_params[BirthKeys.demographics_birth]
        )
        self.assertEqual(
            expected_maternal_transmission,
            self.config_params[BirthKeys.maternal_transmission]
        )
        self.assertEqual(
            expected_time_dependence,
            self.config_params[BirthKeys.time_dependence]
        )
        self.assertNotIn(
            BirthKeys.maternal_transmission_probability,
            self.config_params
        )
        pass

    def test_birth_multiplier_custom(self):
        test_multiplier = 1.3
        bf = BirthFeatureConfiguration(
            enable=True,
            x_birth=test_multiplier
        )
        self.config_params = bf.get_config_params()
        self.assertIn(
            BirthKeys.x_birth,
            self.config_params
        )
        observed_multiplier = self.config_params[BirthKeys.x_birth]
        self.assertEqual(
            test_multiplier,
            observed_multiplier
        )
        pass

    def test_demographics_birth(self):
        bf = BirthFeatureConfiguration(
            enable=True,
            demographics_birth=True
        )
        self.config_params = bf.get_config_params()
        self.assertEqual(
            len(self.config_params),
            5 # enable, multiplier, time dependence, demographics, maternal txn
        )
        self.assertIn(
            BirthKeys.demographics_birth,
            self.config_params
        )
        self.assertTrue(
            self.config_params[BirthKeys.demographics_birth]
        )
        # Not sure what this even does
        # schema "Controls whether or not newborns have identical or heterogeneous characteristics."
        pass

    # endregion

    # region NaturalMortality(death)

    def test_disable_death(self):
        df = DeathFeatureConfiguration(enable=False)
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            1
        )
        self.assertFalse(
            self.config_params[DeathKeys.enable]
        )
        pass

    def test_enable_death(self):
        expected_multiplier = 1.0
        df = DeathFeatureConfiguration(enable=True)
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertTrue(
            self.config_params[DeathKeys.enable]
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.none
        )
        pass

    def test_enable_death_multiplier(self):
        expected_multiplier = 1.5
        df = DeathFeatureConfiguration(enable=True,
                                       x_death=expected_multiplier)
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.none
        )
        pass

    def test_disable_death_multiplier(self):
        expected_multiplier = 1.5
        df = DeathFeatureConfiguration(enable=False,
                                       x_death=expected_multiplier)
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            1
        )
        self.assertFalse(
            self.config_params[DeathKeys.enable]
        )
        pass

    def test_enable_death_age_gender(self):
        expected_multiplier = 1.0
        expected_demo_params = {
            'some_ages': [10, 100, 1000],
            'some_genders': {
                'male' : [0.2, 0.7, 0.9],
                'female' : [0.3, 0.4, 0.7]
            }
        }
        df = DeathAgeAndGenderFeatureConfiguration(
            demographics_params=expected_demo_params
        )
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertTrue(
            self.config_params[DeathKeys.enable]
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.age_and_gender
        )
        found_demo_params = df.demographics_params
        self.assertEqual(
            expected_demo_params,
            found_demo_params
        )
        pass

    def test_enable_death_age_gender_multiplier(self):
        expected_multiplier = 0.9
        df = DeathAgeAndGenderFeatureConfiguration(
            x_death=expected_multiplier
        )
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertTrue(
            self.config_params[DeathKeys.enable]
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.age_and_gender
        )
        pass

    def test_enable_death_year_age_gender(self):
        expected_multiplier = 1.0
        expected_demo_params = {
            'some_ages': [10, 100, 1000],
            'some_genders': {
                'male' : [0.2, 0.7, 0.9],
                'female' : [0.3, 0.4, 0.7]
            },
            'some_years' : [1975, 1999, 2020]
        }
        df = DeathYearAgeGenderFeatureConfiguration(
            demographics_params=expected_demo_params
        )
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertTrue(
            self.config_params[DeathKeys.enable]
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.year_age_gender
        )
        found_demo_params = df.demographics_params
        self.assertEqual(
            expected_demo_params,
            found_demo_params
        )
        pass

    def test_enable_death_year_age_gender_multiplier(self):
        expected_multiplier = 0.9
        df = DeathYearAgeGenderFeatureConfiguration(
            x_death=expected_multiplier
        )
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertTrue(
            self.config_params[DeathKeys.enable]
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.year_age_gender
        )
        pass




        pass

    # death default multiplier

    # endregion

    # region Population Sampling

    def test_sampling_disabled(self):
        sf = IndividualSamplingFeatureConfiguration(
            sample_type=IndividualSamplingKeys.enum_options.all
        )
        self.config_params = sf.get_config_params()
        self.assertEqual(
            1,
            len(self.config_params)
        )
        self.assertEqual(
            IndividualSamplingKeys.enum_options.all,
            self.config_params[IndividualSamplingKeys.type_enum]
        )
        pass

    def test_sampling_fixed_default(self):
        expected_rate=1.0
        sf = IndividualSamplingFixedFeatureConfiguration(
            fixed_rate=expected_rate
        )
        self.config_params = sf.get_config_params()
        self.assertEqual(
            2,
            len(self.config_params)
        )
        self.assertEqual(
            expected_rate,
            self.config_params[IndividualSamplingKeys.base_sample_rate]
        )
        pass

    def test_sampling_fixed_custom(self):
        expected_rate=0.2
        sf = IndividualSamplingFixedFeatureConfiguration(
            fixed_rate=expected_rate
        )
        self.config_params = sf.get_config_params()
        self.assertEqual(
            2,
            len(self.config_params)
        )
        self.assertEqual(
            expected_rate,
            self.config_params[IndividualSamplingKeys.base_sample_rate]
        )
        pass

    def test_sampling_popsize_default(self):
        expected_samples = 100
        sf = IndividualSamplingPopulationSizeFeatureConfiguration(
            max_node_pop_samples = expected_samples
        )
        self.config_params = sf.get_config_params()
        self.assertEqual(
            2,
            len(self.config_params)
        )
        self.assertEqual(
            IndividualSamplingKeys.enum_options.adapt_pop_size,
            self.config_params[IndividualSamplingKeys.type_enum]
        )
        self.assertEqual(
            expected_samples,
            self.config_params[IndividualSamplingKeys.max_node_pop_samples]
        )
        pass

    def test_sampling_popsize_custom(self):
        expected_samples = 333
        sf = IndividualSamplingPopulationSizeFeatureConfiguration(
            max_node_pop_samples = expected_samples
        )
        self.config_params = sf.get_config_params()
        self.assertEqual(
            2,
            len(self.config_params)
        )
        self.assertEqual(
            IndividualSamplingKeys.enum_options.adapt_pop_size,
            self.config_params[IndividualSamplingKeys.type_enum]
        )
        self.assertEqual(
            expected_samples,
            self.config_params[IndividualSamplingKeys.max_node_pop_samples]
        )
        pass

    def test_sampling_agegroup_default(self):
        birth_toddler_rate = 1.0
        toddler_years4_rate = 1.0
        years05_09_rate = 1.0
        years10_14_rate = 1.0
        years15_19_rate = 1.0
        years20_plus_rate = 1.0
        expected_adult_min_age = 15
        expected_atbirth_rate = 1.0
        sf = IndividualSamplingAgeGroupFeatureConfiguration()
        self.config_params = sf.get_config_params()
        self.assertEqual(
            9,
            len(self.config_params)
        )
        self.assertEqual(
            expected_adult_min_age,
            self.config_params[SamplingAgeGroupKeys.min_adult_age]
        )
        self.assertEqual(
            expected_atbirth_rate,
            self.config_params[SamplingAgeGroupKeys.at_birth]
        )
        self.assertEqual(
            IndividualSamplingKeys.enum_options.adapt_age_group,
            self.config_params[IndividualSamplingKeys.type_enum]
        )
        self.assertEqual(
            birth_toddler_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.birth_toddler
            ]
        )
        self.assertEqual(
            toddler_years4_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.toddler_years4
            ]
        )
        self.assertEqual(
            years05_09_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years05_09
            ]
        )
        self.assertEqual(
            years10_14_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years10_14
            ]
        )
        self.assertEqual(
            years15_19_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years15_19
            ]
        )
        self.assertEqual(
            years20_plus_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years20_plus
            ]
        )
        pass

    def test_sampling_agegroup_custom(self):
        birth_toddler_rate = 0.9
        toddler_years4_rate = 0.8
        years05_09_rate = 0.7
        years10_14_rate = 0.6
        years15_19_rate = 0.5
        years20_plus_rate = 0.4
        expected_atbirth_rate = 0.3
        expected_adult_min_age = 42
        sf = IndividualSamplingAgeGroupFeatureConfiguration(
            atbirth=expected_atbirth_rate,
            adult_min_age_years=expected_adult_min_age,
            birth_18months=birth_toddler_rate,
            toddler_years04=toddler_years4_rate,
            years05_years09=years05_09_rate,
            years10_years14=years10_14_rate,
            years15_years19=years15_19_rate,
            years20_older=years20_plus_rate
        )
        self.config_params = sf.get_config_params()
        self.assertEqual(
            9,
            len(self.config_params)
        )
        self.assertEqual(
            expected_adult_min_age,
            self.config_params[SamplingAgeGroupKeys.min_adult_age]
        )
        self.assertEqual(
            expected_atbirth_rate,
            self.config_params[SamplingAgeGroupKeys.at_birth]
        )
        self.assertEqual(
            IndividualSamplingKeys.enum_options.adapt_age_group,
            self.config_params[IndividualSamplingKeys.type_enum]
        )
        self.assertEqual(
            birth_toddler_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.birth_toddler
            ]
        )
        self.assertEqual(
            toddler_years4_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.toddler_years4
            ]
        )
        self.assertEqual(
            years05_09_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years05_09
            ]
        )
        self.assertEqual(
            years10_14_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years10_14
            ]
        )
        self.assertEqual(
            years15_19_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years15_19
            ]
        )
        self.assertEqual(
            years20_plus_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years20_plus
            ]
        )
        pass

    def test_sampling_agegroupsize_defaultagegroup(self):
        expected_pop_samples = 123
        birth_toddler_rate = 1.0
        toddler_years4_rate = 1.0
        years05_09_rate = 1.0
        years10_14_rate = 1.0
        years15_19_rate = 1.0
        years20_plus_rate = 1.0
        expected_adult_min_age = 15
        expected_atbirth_rate = 1.0
        sf = IndividualSamplingAgeGroupSizeFeatureConfiguration(
            max_node_pop_samples=expected_pop_samples
        )
        self.config_params = sf.get_config_params()
        self.assertEqual(
            10,
            len(self.config_params)
        )
        self.assertEqual(
            expected_pop_samples,
            self.config_params[IndividualSamplingKeys.max_node_pop_samples]
        )
        self.assertEqual(
            expected_adult_min_age,
            self.config_params[SamplingAgeGroupKeys.min_adult_age]
        )
        self.assertEqual(
            expected_atbirth_rate,
            self.config_params[SamplingAgeGroupKeys.at_birth]
        )
        self.assertEqual(
            IndividualSamplingKeys.enum_options.adapt_age_group,
            self.config_params[IndividualSamplingKeys.type_enum]
        )
        self.assertEqual(
            birth_toddler_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.birth_toddler
            ]
        )
        self.assertEqual(
            toddler_years4_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.toddler_years4
            ]
        )
        self.assertEqual(
            years05_09_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years05_09
            ]
        )
        self.assertEqual(
            years10_14_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years10_14
            ]
        )
        self.assertEqual(
            years15_19_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years15_19
            ]
        )
        self.assertEqual(
            years20_plus_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years20_plus
            ]
        )
        pass

    def test_sampling_agegroupsize_customagegroup(self):
        expected_pop_samples = 123
        birth_toddler_rate = 0.9
        toddler_years4_rate = 0.8
        years05_09_rate = 0.7
        years10_14_rate = 0.6
        years15_19_rate = 0.5
        years20_plus_rate = 0.4
        expected_atbirth_rate = 0.3
        expected_adult_min_age = 42
        sf = IndividualSamplingAgeGroupSizeFeatureConfiguration(
            max_node_pop_samples=expected_pop_samples,
            atbirth=expected_atbirth_rate,
            adult_min_age_years=expected_adult_min_age,
            birth_18months=birth_toddler_rate,
            toddler_years04=toddler_years4_rate,
            years05_years09=years05_09_rate,
            years10_years14=years10_14_rate,
            years15_years19=years15_19_rate,
            years20_older=years20_plus_rate
        )
        self.config_params = sf.get_config_params()
        self.assertEqual(
            10,
            len(self.config_params)
        )
        self.assertEqual(
            expected_pop_samples,
            self.config_params[IndividualSamplingKeys.max_node_pop_samples]
        )
        self.assertEqual(
            expected_adult_min_age,
            self.config_params[SamplingAgeGroupKeys.min_adult_age]
        )
        self.assertEqual(
            expected_atbirth_rate,
            self.config_params[SamplingAgeGroupKeys.at_birth]
        )
        self.assertEqual(
            IndividualSamplingKeys.enum_options.adapt_age_group,
            self.config_params[IndividualSamplingKeys.type_enum]
        )
        self.assertEqual(
            birth_toddler_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.birth_toddler
            ]
        )
        self.assertEqual(
            toddler_years4_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.toddler_years4
            ]
        )
        self.assertEqual(
            years05_09_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years05_09
            ]
        )
        self.assertEqual(
            years10_14_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years10_14
            ]
        )
        self.assertEqual(
            years15_19_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years15_19
            ]
        )
        self.assertEqual(
            years20_plus_rate,
            self.config_params[
                SamplingAgeGroupKeys.age_groups.years20_plus
            ]
        )
        pass

    def test_sampling_immunestate_default(self):
        expected_threshold = 0.0
        expected_samplerate_immune = 0.01
        base_samplerate = 1.0
        sf = IndividualSamplingImmuneStateFeatureConfiguration(
            immune_threshold_downsampling=expected_threshold,
            relative_sample_rate_immune=expected_samplerate_immune
        )
        self.config_params = sf.get_config_params()
        self.assertEqual(
            4,
            len(self.config_params)
        )
        self.assertEqual(
            IndividualSamplingKeys.enum_options.adapt_immune_state,
            self.config_params[IndividualSamplingKeys.type_enum]
        )
        self.assertEqual(
            expected_threshold,
            self.config_params[IndividualSamplingKeys.immune_threshold]
        )
        self.assertEqual(
            expected_samplerate_immune,
            self.config_params[IndividualSamplingKeys.immune_sample_rate]
        )
        self.assertEqual(
            base_samplerate,
            self.config_params[IndividualSamplingKeys.base_sample_rate]
        )
        pass

    def test_sampling_immunestate_custom(self):
        expected_threshold = 0.3
        expected_samplerate_immune = 0.1
        base_samplerate = 10.0
        sf = IndividualSamplingImmuneStateFeatureConfiguration(
            immune_threshold_downsampling=expected_threshold,
            relative_sample_rate_immune=expected_samplerate_immune,
            base_sample_rate=base_samplerate
        )
        self.config_params = sf.get_config_params()
        self.assertEqual(
            4,
            len(self.config_params)
        )
        self.assertEqual(
            IndividualSamplingKeys.enum_options.adapt_immune_state,
            self.config_params[IndividualSamplingKeys.type_enum]
        )
        self.assertEqual(
            expected_threshold,
            self.config_params[IndividualSamplingKeys.immune_threshold]
        )
        self.assertEqual(
            expected_samplerate_immune,
            self.config_params[IndividualSamplingKeys.immune_sample_rate]
        )
        self.assertEqual(
            base_samplerate,
            self.config_params[IndividualSamplingKeys.base_sample_rate]
        )
        pass

    # endregion

    # region Demographics

    def test_builtin_demographics_default(self):
        expected_torus_size = 10
        expected_node_population = 1000
        df = DemographicsBuiltinFeatureConfiguration()
        self.config_params = df.get_config_params()
        self.assertEqual(
            3,
            len(self.config_params)
        )
        self.assertTrue(
            self.config_params[DemographicsKeys.enable]
        )
        self.assertEqual(
            expected_torus_size,
            self.config_params[DemographicsKeys.builtin_torus_size]
        )
        self.assertEqual(
            expected_node_population,
            self.config_params[DemographicsKeys.builtin_node_population]
        )
        pass

    def test_builtin_demographics_custom(self):
        expected_node_population = 123
        expected_torus_size = 9
        df = DemographicsBuiltinFeatureConfiguration(
            torus_size=expected_torus_size,
            node_population=expected_node_population
        )
        self.config_params = df.get_config_params()
        self.assertEqual(
            3,
            len(self.config_params)
        )
        self.assertTrue(
            self.config_params[DemographicsKeys.enable]
        )
        self.assertEqual(
            expected_torus_size,
            self.config_params[DemographicsKeys.builtin_torus_size]
        )
        self.assertEqual(
            expected_node_population,
            self.config_params[DemographicsKeys.builtin_node_population]
        )
        pass

    def test_demographics_custom_singlefile(self):
        expected_basefile = "cw_demographics.json"
        df = DemographicsCustomFeatureConfiguration(
            demographics_filename=expected_basefile
        )
        self.config_params = df.get_config_params()
        self.assertEqual(
            2,
            len(self.config_params)
        )
        self.assertFalse(
            self.config_params[DemographicsKeys.enable]
        )
        filenames_array = self.config_params[DemographicsKeys.demographics_filenames]
        self.assertEqual(
            1,
            len(filenames_array)
        )
        self.assertEqual(
            expected_basefile,
            filenames_array[0]
        )
        pass

    def test_demographics_custom_two_overlays(self):
        expected_basefile = "cw_demographics.json"
        overlay_one = "it_an_overlay.json"
        overlay_two = "it_anotherone.json"
        df = DemographicsCustomFeatureConfiguration(
            demographics_filename=expected_basefile
        )
        df.add_overlay(overlay_one)
        df.add_overlay(overlay_two)
        self.config_params = df.get_config_params()
        self.assertEqual(
            2,
            len(self.config_params)
        )
        self.assertFalse(
            self.config_params[DemographicsKeys.enable]
        )
        filenames_array = self.config_params[DemographicsKeys.demographics_filenames]
        self.assertEqual(
            3,
            len(filenames_array)
        )
        self.assertEqual(
            expected_basefile,
            filenames_array[0]
        )
        self.assertEqual(
            overlay_one,
            filenames_array[1]
        )
        self.assertEqual(
            overlay_two,
            filenames_array[2]
        )
        pass

    # endregion

    def tearDown(self):
        if test_debug:
            print()
            print(self.id())
            print(self.config_params)
            print()
        pass

