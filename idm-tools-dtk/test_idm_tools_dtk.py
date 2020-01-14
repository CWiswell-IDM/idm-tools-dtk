import unittest
__unittest = True
from maternal_protection_configuration import MaternalProtectionConfiguration,\
    MaternalProtectionConfigurationLinear, MaternalProtectionConfigurationSigmoid,\
    MaternalProtectionKeys
from initial_susceptibility_feature_configuration import SusceptibilityDistributionKeys, \
    InitialSusceptibilityFeatureConfiguration
from individual_sampling_feature_configuration import IndividualSamplingKeys, \
    SamplingAgeGroupKeys, \
    IndividualSamplingFeatureConfiguration, \
    IndividualSamplingFixedFeatureConfiguration, \
    IndividualSamplingAgeGroupFeatureConfiguration, \
    IndividualSamplingAgeGroupSizeFeatureConfiguration, \
    IndividualSamplingPopulationSizeFeatureConfiguration, \
    IndividualSamplingImmuneStateFeatureConfiguration


test_debug = False
MATERNAL_PROTECTION_ENABLE_KEY = "Enable_Maternal_Protection"
INITIAL_SUSCEPTIBILITY_ENABLE_KEY = "Enable_Initial_Susceptibility_Distribution"

class IdmToolsDtkTest(unittest.TestCase):
    def setUp(self):
        self.config_params = None
        pass

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


    def tearDown(self):
        if test_debug:
            print()
            print(self.id())
            print(self.config_params)
            print()
        pass

