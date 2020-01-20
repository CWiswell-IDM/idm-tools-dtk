import unittest
__unittest = True
from idm_tools_dtk.individual_sampling.individual_sampling_feature_configuration import IndividualSamplingKeys, \
    SamplingAgeGroupKeys, \
    IndividualSamplingFeatureConfiguration, \
    IndividualSamplingFixedFeatureConfiguration, \
    IndividualSamplingAgeGroupFeatureConfiguration, \
    IndividualSamplingAgeGroupSizeFeatureConfiguration, \
    IndividualSamplingPopulationSizeFeatureConfiguration, \
    IndividualSamplingImmuneStateFeatureConfiguration

from idm_tools_dtk.emod_simulation_configuration import EmodSimulationConfiguration


from idm_tools_dtk.test_idm_tools_dtk import IdmToolsDtkTest

class IndividualSamplingFeatureTest(IdmToolsDtkTest):

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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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
        emod_sim = EmodSimulationConfiguration(individual_sampling_config=sf)
        self.config_params = emod_sim.get_parameters()
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


