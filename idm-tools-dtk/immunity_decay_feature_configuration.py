from feature_configuration import EnableableFeatureConfiguration

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

class ImmuneDecayFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable_decay,
                 acquisition_rate=None,
                 acquisition_duration_before=None,
                 mortality_rate=None,
                 mortality_duration_before=None,
                 transmission_rate=None,
                 transmission_duration_before=None):
        super().__init__("Immune_Decay", ImmuneDecayKeys.enable, "Enable_Immunity")
        self.master_parameter_value = enable_decay
        for k in ImmuneDecayKeys.all_keys:
            self.feature_params[k] = None
        self.feature_params[self.master_parameter] = enable_decay
        if enable_decay:
            self.feature_params[ImmuneDecayKeys.acquisition_rate] = acquisition_rate
            self.feature_params[ImmuneDecayKeys.acquisition_duration_before_decay] = acquisition_duration_before
            self.feature_params[ImmuneDecayKeys.mortality_rate] = mortality_rate
            self.feature_params[ImmuneDecayKeys.mortality_duration_before_decay] = mortality_duration_before
            self.feature_params[ImmuneDecayKeys.transmission_rate] = transmission_rate
            self.feature_params[ImmuneDecayKeys.transmission_duration_before_decay] = transmission_duration_before
        pass

