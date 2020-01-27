import unittest
__unittest = True

from idm_tools_dtk.test_idm_tools_dtk import IdmToolsDtkTest

from idm_tools_dtk.infection.incubation_period_configuration import IncubationConfigurationConstant, \
    IncubationConfigurationExponential, IncubationConfigurationGaussian, IncubationConfigurationUniform
from idm_tools_dtk.infection.infectivity_feature_configuration import InfectivityConfigurationConstant, \
    InfectivityConfigurationGaussian, InfectivityConfigurationExponential, InfectivityConfigurationUniform, \
    InfectivityKeys
from idm_tools_dtk.emod_simulation_configuration import EmodSimulationConfiguration


class InfectionFeatureTest(IdmToolsDtkTest):

    # region incubation period
    def test_incubation_constant_default(self):
        ic = IncubationConfigurationConstant()
        self.assertEqual(
            2,
            len(ic.get_config_params())
        )
        emod_sim = EmodSimulationConfiguration(incubation_config=ic)
        self.config_params = emod_sim.get_parameters()

    # endregion

    # region infectious period

    # endregion

    # region infectivity

    def verify_updates_and_offset(self, expected_updates:int=1,
                                  expected_offset:int=0):
        found_offset = self.config_params[InfectivityKeys.symptomatic_offset]
        found_updates = self.config_params[InfectivityKeys.updates_per_timestep]
        self.assertEqual(expected_offset,
                         found_offset,
                         msg=f"Expected symptomatic offset of: {expected_offset} got: {found_offset}.\n")
        self.assertEqual(expected_updates,
                         found_updates,
                         msg=f"Expected updates per timestep: {expected_updates} got: {found_updates}\n")

    def test_infectivity_constant_default(self):
        duration_expected = 3.5
        ic = InfectivityConfigurationConstant()
        self.config_params = ic.get_config_params()
        self.assertEqual(
            4,
            len(self.config_params),
            msg=f"Should be 5 params (distribution_type, distribution_constant, updates_per_timestep, symptomatic_offset) got these: {self.config_params}"
        )
        self.verify_updates_and_offset()
        pass

    def test_infectivity_constant_specified(self):
        duration_expected = 5.1
        expected_updates = 8
        expected_symptomatic_offset = 2
        ic = InfectivityConfigurationConstant(constant_infectivity=5.1,
                                              updates_per_timestep=expected_updates,
                                              symptomatic_offset_days=expected_symptomatic_offset)
        self.config_params = ic.get_config_params()
        self.assertEqual(
            4,
            len(self.config_params),
            msg=f"Should be 5 params (distribution_type, distribution_constant, updates_per_timestep, symptomatic_offset) got these: {self.config_params}"
        )
        self.assertEqual(
            duration_expected,
            self.config_params["Base_Infectivity_Constant"]
        )
        self.verify_updates_and_offset(expected_updates=expected_updates,
                                       expected_offset=expected_symptomatic_offset)
        pass

    def test_infectivity_gaussian_default(self):
        mean_expected = 3.5
        sig_expected = 0.5
        ic = InfectivityConfigurationGaussian(
            gaussian_mean_infectivity=mean_expected,
            gaussian_sigma=sig_expected
        )
        self.config_params = ic.get_config_params()
        self.assertEqual(
            5,
            len(self.config_params)
        )
        self.assertEqual(
            mean_expected,
            self.config_params["Base_Infectivity_Gaussian_Mean"]
        )
        self.assertEqual(
            sig_expected,
            self.config_params["Base_Infectivity_Gaussian_Std_Dev"]
        )
        self.verify_updates_and_offset()
        pass

    def test_infectivity_gaussian_specified(self):
        expected_updates = 12
        expected_symptomatic_offset = 3
        mean_expected = 25.2
        sig_expected = 2
        ic = InfectivityConfigurationGaussian(
            gaussian_mean_infectivity=mean_expected,
            gaussian_sigma=sig_expected,
            updates_per_timestep=expected_updates,
            symptomatic_offset_days=expected_symptomatic_offset
        )
        self.config_params = ic.get_config_params()
        self.assertEqual(
            5,
            len(self.config_params)
        )
        self.assertEqual(
            mean_expected,
            self.config_params["Base_Infectivity_Gaussian_Mean"]
        )
        self.assertEqual(
            sig_expected,
            self.config_params["Base_Infectivity_Gaussian_Std_Dev"]
        )
        self.verify_updates_and_offset(expected_updates=expected_updates,
                                       expected_offset=expected_symptomatic_offset)
        pass

    def test_infectivity_exponential_default(self):
        duration_expected = 5.1
        ic = InfectivityConfigurationExponential(
            exponential_mean_infectivity=duration_expected
        )
        self.config_params = ic.get_config_params()
        self.assertEqual(
            4,
            len(self.config_params),
            msg=f"Should be 5 params (distribution_type, distribution_exponential, updates_per_timestep, symptomatic_offset) got these: {self.config_params}"
        )
        self.assertEqual(
            duration_expected,
            self.config_params["Base_Infectivity_Exponential"]
        )
        self.verify_updates_and_offset()
        pass

    def test_infectivity_exponential_specified(self):
        duration_expected = 5.1
        expected_updates = 8
        expected_symptomatic_offset = 2
        ic = InfectivityConfigurationExponential(
            exponential_mean_infectivity=duration_expected,
            symptomatic_offset_days=expected_symptomatic_offset,
            updates_per_timestep=expected_updates
        )
        self.config_params = ic.get_config_params()
        self.assertEqual(
            4,
            len(self.config_params),
            msg=f"Should be 5 params (distribution_type, distribution_constant, updates_per_timestep, symptomatic_offset) got these: {self.config_params}"
        )
        self.assertEqual(
            duration_expected,
            self.config_params["Base_Infectivity_Exponential"]
        )
        self.verify_updates_and_offset(expected_updates=expected_updates,
                                       expected_offset=expected_symptomatic_offset)
        pass

    def test_infectivity_uniform_default(self):
        min_expected = 2.1
        max_expected = 15
        ic = InfectivityConfigurationUniform(
            uniform_min_infectivity=min_expected,
            uniform_max_infectivity=max_expected
        )
        self.config_params = ic.get_config_params()
        self.assertEqual(
            5,
            len(self.config_params)
        )
        self.assertEqual(
            min_expected,
            self.config_params["Base_Infectivity_Min"]
        )
        self.assertEqual(
            max_expected,
            self.config_params["Base_Infectivity_Max"]
        )
        self.verify_updates_and_offset()
        pass

    def test_infectivity_uniform_specified(self):
        expected_updates = 12
        expected_symptomatic_offset = 3
        min_expected = 12
        max_expected = 20.1
        ic = InfectivityConfigurationUniform(
            uniform_min_infectivity=min_expected,
            uniform_max_infectivity=max_expected,
            updates_per_timestep=expected_updates,
            symptomatic_offset_days=expected_symptomatic_offset
        )
        self.config_params = ic.get_config_params()
        self.assertEqual(
            5,
            len(self.config_params)
        )
        self.assertEqual(
            min_expected,
            self.config_params["Base_Infectivity_Min"]
        )
        self.assertEqual(
            max_expected,
            self.config_params["Base_Infectivity_Max"]
        )
        self.verify_updates_and_offset(
            expected_updates=expected_updates,
            expected_offset=expected_symptomatic_offset
        )
        pass


    # endregion

    # region disease mortality

    # endregion

    # region strain tracking

    # endregion