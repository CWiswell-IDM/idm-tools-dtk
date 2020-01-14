from feature_configuration import EnableableFeatureConfiguration

class ImmunityFeatureKeys:
    enable = "Enable_Immunity"
    acquisition_multiplier = "Post_Infection_Acquisition_Multiplier"
    mortality_multiplier = "Post_Infection_Mortality_Multiplier"
    transmission_multiplier = "Post_Infection_Transmission_Multiplier"
    all_keys = [enable, acquisition_multiplier,
                mortality_multiplier, transmission_multiplier]


class ImmunityFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable_immunity,
                 acquisition_multiplier: float=1.0,

                 mortality_mutliplier=None,
                 transmission_multiplier=None):
        super().__init__("Immunity", ImmunityFeatureKeys.enable)
        self.master_parameter_value = enable_immunity
        for k in ImmunityFeatureKeys.all_keys:
            self.feature_params[k] = None
        self.feature_params[self.master_parameter] = enable_immunity
        if enable_immunity:
            self.feature_params[ImmunityFeatureKeys.acquisition_multiplier] = acquisition_multiplier
            self.feature_params[ImmunityFeatureKeys.mortality_multiplier] = mortality_mutliplier
            self.feature_params[ImmunityFeatureKeys.transmission_multiplier] = transmission_multiplier
        pass
