import unittest
__unittest = True

from idm_tools_dtk.test_idm_tools_dtk import IdmToolsDtkTest
from idm_tools_dtk.demographics.demographics_feature_configuration import DemographicsKeys, \
    DemographicsBuiltinFeatureConfiguration, \
    DemographicsCustomFeatureConfiguration
from idm_tools_dtk.demographics.initial_susceptibility_feature_configuration import SusceptibilityDistributionKeys, \
    InitialSusceptibilityFeatureConfiguration


INITIAL_SUSCEPTIBILITY_ENABLE_KEY = SusceptibilityDistributionKeys.enable

class DemographicsFeatureTest(IdmToolsDtkTest):

    # region Demographics

    def test_builtin_demographics_default(self):
        expected_torus_size = 10
        expected_node_population = 1000
        df = DemographicsBuiltinFeatureConfiguration()
        self.config_params = df.get_config_params()
        self.assertEqual(
            9,
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
            9,
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
            8,
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
            8,
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

