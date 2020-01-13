from feature_configuration import EnableableFeatureConfiguration

class VitalDynamicsKeys:
    enable = "Enable_Vital_Dynamics"
    aging = "Enable_Aging"
    birth = "Enable_Birth"
    natural_mortality = "Enable_Natural_Mortality"
    all_keys = [enable, aging, birth, natural_mortality]
    pass

class VitalDynamicsFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable, aging=False,
                 birth=False, natural_mortality=False):
        super().__init__(feature_name="Vital_Dynamics",
                         enable_parameter=VitalDynamicsKeys.enable)
        for k in VitalDynamicsKeys.all_keys:
            self.feature_params[k] = None
            pass
        self.feature_params[VitalDynamicsKeys.enable] = enable
        if enable:
            self.feature_params[VitalDynamicsKeys.aging] = aging
            self.feature_params[VitalDynamicsKeys.birth] = birth
            self.feature_params[VitalDynamicsKeys.natural_mortality] = natural_mortality
            pass
