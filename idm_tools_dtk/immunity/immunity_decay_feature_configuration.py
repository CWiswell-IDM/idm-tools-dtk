from idm_tools_dtk.utilities.feature_configuration import EnableableFeatureConfiguration
from idm_tools_dtk.immunity.immunity_feature_configuration import ImmunityFeatureConfiguration, ImmunityFeatureKeys

class ImmuneDecayKeys:
    enable = "Enable_Immune_Decay"
    acquisition_rate = "Acquisition_Blocking_Immunity_Decay_Rate"
    acquisition_duration_before_decay = "Acquisition_Blocking_Immunity_Duration_Before_Decay"
    mortality_rate = "Mortality_Blocking_Immunity_Decay_Rate"
    mortality_duration_before_decay = "Mortality_Blocking_Immunity_Duration_Before_Decay"
    transmission_rate = "Transmission_Blocking_Immunity_Decay_Rate"
    transmission_duration_before_decay = "Transmission_Blocking_Immunity_Duration_Before_Decay"
    all_keys = [enable, acquisition_rate, acquisition_duration_before_decay,
                mortality_rate, mortality_duration_before_decay,
                transmission_rate, transmission_duration_before_decay]

class ImmuneDecayFeatureConfiguration(ImmunityFeatureConfiguration):
    def __init__(self, immunity_config:ImmunityFeatureConfiguration=None,
                 acquisition_rate=None,
                 acquisition_duration_before=None,
                 mortality_rate=None,
                 mortality_duration_before=None,
                 transmission_rate=None,
                 transmission_duration_before=None):
        super().__init__("Immune_Decay", ImmuneDecayKeys.enable, "Enable_Immunity")
        if not immunity_config:
            immunity_config = ImmunityFeatureConfiguration(
                enable_immunity=True,
                acquisition_multiplier=0.2,
                mortality_mutliplier=0.1,
                transmission_multiplier=0.3
            )
            self.assumptions[immunity_config.feature_name] = immunity_config.get_config_params()
            pass
        immunity_params = immunity_config.get_config_params()
        for k in immunity_params:
            self.feature_params[k] = immunity_params[k]
        for k in ImmuneDecayKeys.all_keys:
            self.feature_params[k] = None
        if immunity_params[ImmunityFeatureKeys.enable]:
            if acquisition_rate:
                self.feature_params[ImmuneDecayKeys.acquisition_rate] = acquisition_rate
                self.feature_params[ImmuneDecayKeys.acquisition_duration_before_decay] = acquisition_duration_before
                pass
            if mortality_rate:
                self.feature_params[ImmuneDecayKeys.mortality_rate] = mortality_rate
                self.feature_params[ImmuneDecayKeys.mortality_duration_before_decay] = mortality_duration_before
                pass
            if transmission_rate:
                self.feature_params[ImmuneDecayKeys.transmission_rate] = transmission_rate
                self.feature_params[ImmuneDecayKeys.transmission_duration_before_decay] = transmission_duration_before
        pass

