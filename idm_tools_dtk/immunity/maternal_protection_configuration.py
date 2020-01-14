from idm_tools_dtk.utilities.feature_configuration import EnableableFeatureConfiguration


class MaternalProtectionKeys:
    enable = "Enable_Maternal_Protection"
    type_enum = "Maternal_Protection_Type"
    sigmoid_halfmax = "Maternal_Sigmoid_HalfMaxAge"
    sigmoid_steepness_factor = "Maternal_Sigmoid_SteepFac"
    sigmoid_initial_susceptibility = "Maternal_Sigmoid_SusInit"
    linear_slope = "Maternal_Linear_SusZero"
    linear_suszero = "Maternal_Linear_Slope"
    all_keys = [enable, type_enum, sigmoid_halfmax,
                sigmoid_steepness_factor, sigmoid_initial_susceptibility,
                linear_slope, linear_suszero]
    class enum_options:
        sigmoid = "SIGMOID"
        linear = "LINEAR"

class MaternalProtectionConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable, maternal_protection_type=None):
        super().__init__(feature_name="Maternal_Protection",
                         enable_parameter=MaternalProtectionKeys.enable)
        for k in MaternalProtectionKeys.all_keys:
            self.feature_params[k] = None
        self.feature_params[MaternalProtectionKeys.enable] = enable
        if enable:
            self.feature_params[MaternalProtectionKeys.type_enum] = maternal_protection_type

class MaternalProtectionConfigurationSigmoid(MaternalProtectionConfiguration):
    def __init__(self, halfmax_age, steepness_factor, initial_susceptibility):
        super().__init__(enable=True,
                         maternal_protection_type=MaternalProtectionKeys.enum_options.sigmoid)
        self.feature_params[MaternalProtectionKeys.sigmoid_halfmax] = halfmax_age
        self.feature_params[MaternalProtectionKeys.sigmoid_steepness_factor] = steepness_factor
        self.feature_params[MaternalProtectionKeys.sigmoid_initial_susceptibility] = initial_susceptibility

class MaternalProtectionConfigurationLinear(MaternalProtectionConfiguration):
    def __init__(self, slope, sus_zero):
        super().__init__(enable=True,
                         maternal_protection_type=MaternalProtectionKeys.enum_options.linear)
        self.feature_params[MaternalProtectionKeys.linear_slope] = slope
        self.feature_params[MaternalProtectionKeys.linear_suszero] = sus_zero

