import unittest
__unittest = True

from test_idm_tools_dtk import IdmToolsDtkTest
from demographics_feature_configuration import DemographicsKeys, \
    DemographicsBuiltinFeatureConfiguration, \
    DemographicsCustomFeatureConfiguration


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

