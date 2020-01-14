import json
from os import path, getcwd

from idm_tools_dtk.vital_dynamics.vital_dynamics_configuration import VitalDynamicsFeatureConfiguration
from idm_tools_dtk.demographics.demographics_feature_configuration import DemographicsFeatureConfiguration, DemographicsBuiltinFeatureConfiguration
from idm_tools_dtk.immunity.immunity_feature_configuration import ImmunityFeatureConfiguration
from idm_tools_dtk.infection.infectious_period_configuration import InfectiousConfiguration, InfectiousConfigurationConstant
from idm_tools_dtk.infection.incubation_period_configuration import IncubationConfiguration, IncubationConfigurationConstant
from idm_tools_dtk.infection.mortality_feature_configuration import DiseaseMortalityFeatureConfiguration
from idm_tools_dtk.individual_sampling.individual_sampling_feature_configuration import IndividualSamplingFeatureConfiguration
from idm_tools_dtk.dtk_simulation.dtk_simulation_configuration import SimulationConfiguration
from idm_tools_dtk.infection.infectivity_feature_configuration import InfectivityConfiguration, InfectivityConfigurationConstant, InfectivityScalingFeatureConfiguration
from idm_tools_dtk.infection.straintracking_feature_configuration import StrainTrackingFeatureConfiguration


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
        self.assumptions = {}
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
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.demo_config = tmp_config
        if not self.vital_config:
            tmp_config = VitalDynamicsFeatureConfiguration(enable=False)
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.vital_config = tmp_config
        if not self.immunity_config:
            tmp_config = ImmunityFeatureConfiguration(enable_immunity=False)
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.immunity_config = tmp_config
        if not self.infectious_config:
            tmp_config = InfectiousConfigurationConstant()
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.infectious_config = tmp_config
        if not self.infectivity_config:
            tmp_config = InfectivityConfigurationConstant()
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.infectivity_config = tmp_config
        if not self.infectivity_scaling_config:
            tmp_config = InfectivityScalingFeatureConfiguration()
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.infectivity_scaling_config = tmp_config
        if not self.incubation_config:
            tmp_config = IncubationConfigurationConstant()
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.incubation_config = tmp_config
        if not self.disease_mortality_config:
            tmp_config = DiseaseMortalityFeatureConfiguration(enable=False)
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.disease_mortality_config = tmp_config
        if not self.straintracking_config:
            tmp_config = StrainTrackingFeatureConfiguration(enable=False)
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.straintracking_config = tmp_config
        if not self.individual_sampling_config:
            tmp_config = IndividualSamplingFeatureConfiguration()
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.individual_sampling_config = tmp_config
        if not self.sim_config:
            tmp_config = SimulationConfiguration("GENERIC_SIM")
            self.assumptions[tmp_config.feature_name] = tmp_config.get_config_params()
            self.sim_config = tmp_config
        else:
            self.assumptions[self.sim_config.feature_name] = self.sim_config.assumptions
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

    def get_parameters(self):
        if not self.parameters:
            self.build_parameters()
            pass
        return self.parameters

    def write_config_file(self, config_filename:str="config.json",
                          config_path:str=None):
        # TODO: build_parameters if not done yet
        if not self.parameters:
            self.build_parameters()
        my_json = {}
        my_json["parameters"] = self.parameters
        my_json["assumptions"] = self.assumptions
        my_json["notes"] = "Generated from prototype idm_tools_dtk code"
        if not config_path:
            config_path = getcwd()
        fullpath = path.join(config_path, config_filename)
        with open(fullpath, 'w') as outfile:
            json.dump(my_json, outfile, indent=4, sort_keys=True)

