import json

from vital_dynamics_configuration import VitalDynamicsFeatureConfiguration
from demographics_feature_configuration import DemographicsFeatureConfiguration, DemographicsBuiltinFeatureConfiguration
from immunity_feature_configuration import ImmunityFeatureConfiguration
from infectious_period_configuration import InfectiousConfiguration, InfectiousConfigurationConstant
from incubation_period_configuration import IncubationConfiguration, IncubationConfigurationConstant
from mortality_feature_configuration import DiseaseMortalityFeatureConfiguration
from individual_sampling_feature_configuration import IndividualSamplingFeatureConfiguration
from dtk_simulation_configuration import SimulationConfiguration
from infectivity_feature_configuration import InfectivityConfiguration, InfectivityConfigurationConstant, InfectivityScalingFeatureConfiguration
from straintracking_feature_configuration import StrainTrackingFeatureConfiguration


class EmodSimulationConfiguration(object):
    def __init__(self,
                 demo_config:DemographicsFeatureConfiguration=None,
                 vital_config:VitalDynamicsFeatureConfiguration=None,
                 immunity_config:ImmunityFeatureConfiguration=None,
                 infectious_config:InfectiousConfiguration=None,
                 infectivity_config:InfectivityConfiguration=None,
                 infectivity_scaling_conifig:InfectivityScalingFeatureConfiguration=None,
                 incubation_config:IncubationConfiguration=None,
                 mortality_config:DiseaseMortalityFeatureConfiguration=None,
                 individual_sampling_config:IndividualSamplingFeatureConfiguration=None,
                 straintracking_config:StrainTrackingFeatureConfiguration=None,
                 sim_config:SimulationConfiguration=None):
        self.parameters = {}
        self.assumptions = [] # TODO: The assumptions object isn't great as a list. refactor as a dictionary.
        self.demo_config = demo_config
        self.vital_config = vital_config
        self.immunity_config = immunity_config
        self.infectious_config = infectious_config
        self.infectivity_config = infectivity_config
        self.infectivity_scaling_config = infectivity_scaling_conifig
        self.incubation_config = incubation_config
        self.disease_mortality_config = mortality_config
        self.straintracking_config = straintracking_config
        self.individual_sampling_config = individual_sampling_config
        self.sim_config = sim_config
        pass

    def populate_feature_configs(self):
        # TODO: Call default constructors for any features not configured
        # TODO: Populate assumptions along the way
        if not self.demo_config:
            tmp_config = DemographicsBuiltinFeatureConfiguration()
            self.assumptions.append(f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}.")
            self.demo_config = tmp_config
        if not self.vital_config:
            tmp_config = VitalDynamicsFeatureConfiguration(enable=False)
            self.assumptions.append(f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}.")
            self.vital_config = tmp_config
        if not self.immunity_config:
            tmp_config = ImmunityFeatureConfiguration(enable_immunity=False)
            self.assumptions.append(f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}.")
            self.immunity_config = tmp_config
        if not self.infectious_config:
            tmp_config = InfectiousConfigurationConstant()
            self.assumptions.append(f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}.")
            self.infectious_config = tmp_config
        if not self.infectivity_config:
            tmp_config = InfectivityConfigurationConstant()
            self.assumptions.append(f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}.")
            self.infectivity_config = tmp_config
        if not self.infectivity_scaling_config:
            tmp_config = InfectivityScalingFeatureConfiguration()
            self.assumptions.append(f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}.")
            self.infectivity_scaling_config = tmp_config
        if not self.incubation_config:
            tmp_config = IncubationConfigurationConstant()
            self.assumptions.append(f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}.")
            self.incubation_config = tmp_config
        if not self.disease_mortality_config:
            tmp_config = DiseaseMortalityFeatureConfiguration(enable=False)
            self.assumptions.append((f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}."))
            self.disease_mortality_config = tmp_config
        if not self.straintracking_config:
            tmp_config = StrainTrackingFeatureConfiguration(enable=False)
            self.assumptions.append((f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}."))
            self.straintracking_config = tmp_config
        if not self.individual_sampling_config:
            tmp_config = IndividualSamplingFeatureConfiguration()
            self.assumptions.append(f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}.")
            self.individual_sampling_config = tmp_config
        if not self.sim_config:
            tmp_config = SimulationConfiguration("GENERIC_SIM")
            self.assumptions.append(f"{tmp_config.feature_name} assumptions: {tmp_config.get_config_params()}.")
            self.sim_config = tmp_config
        pass

    def build_parameters(self):
        # call populate_feature_configs if something is missing
        if not (self.demo_config and
                self.vital_config and
                self.immunity_config and
                self.infectious_config and
                self.incubation_config and
                self.disease_mortality_config and
                self.individual_sampling_config and
                self.sim_config):
            self.populate_feature_configs()
            pass

        # TODO: add to parameter sets one at a time, checking for contradictions
        self.parameters = {}
        # demo config
        self.parameters = {**self.parameters, **self.demo_config.get_config_params()}

        # vital config
        self.parameters = {**self.parameters, **self.vital_config.get_config_params()}

        # immunity config
        self.parameters = {**self.parameters, **self.immunity_config.get_config_params()}

        # infectious config
        self.parameters = {**self.parameters, **self.infectious_config.get_config_params()}

        # infectivity config
        self.parameters = {**self.parameters, **self.infectivity_config.get_config_params()}

        # infectivity_scaling config
        self.parameters = {**self.parameters, **self.infectivity_scaling_config.get_config_params()}

        # incubation config
        self.parameters = {**self.parameters, **self.incubation_config.get_config_params()}

        # disease mortality config
        self.parameters = {**self.parameters, **self.disease_mortality_config.get_config_params()}

        # strain tracking config
        self.parameters = {**self.parameters, **self.straintracking_config.get_config_params()}

        # individual sampling config
        self.parameters = {**self.parameters, **self.individual_sampling_config.get_config_params()}

        # sim config
        self.parameters = {**self.parameters, **self.sim_config.get_config_params()}

        # TODO: for example, if BirthRateTimeDependence is set but EnableVitalDynamics is False
        # TODO: assemble a list of contradictions / error conditions and write them out to file
        # TODO: then raise a ValueException
        pass

    def write_config_file(self, config_filename:str="config.json"):
        # TODO: build_parameters if not done yet
        if not self.parameters:
            self.build_parameters()
        my_json = {}
        my_json["parameters"] = self.parameters
        my_json["assumptions"] = self.assumptions
        my_json["notes"] = "Generated from prototype idm-tools-dtk code"
        with open(config_filename, 'w') as outfile:
            json.dump(my_json, outfile, indent=4, sort_keys=True)

