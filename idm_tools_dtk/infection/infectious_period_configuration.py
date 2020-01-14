from idm_tools_dtk.utilities.distrubution_configuration import DCParams, DCValues, DistributionConfiguration

class InfectiousConfiguration(DistributionConfiguration):
    def __init__(self, duration_type, infectivity=3.5):
        super().__init__("Infectious_Period")
        self.distribution_type = duration_type


class InfectiousConfigurationGaussian(InfectiousConfiguration):
    def __init__(self, gaussian_mean=10, gaussian_sigma=2):
        super().__init__(DCParams.gaussian.value)
        gaussian_mean_key = f"{self.model_property}_{DCValues.gaussian_mean.value}"
        gaussian_sigma_key = f"{self.model_property}_{DCValues.gaussian_sigma.value}"
        self.value_params[gaussian_mean_key] = gaussian_mean
        self.value_params[gaussian_sigma_key] = gaussian_sigma


class InfectiousConfigurationExponential(InfectiousConfiguration):
    def __init__(self, exponential_mean=3):
        super().__init__(DCParams.exponential.value)
        exponential_mean_key = f"{self.model_property}_{DCValues.exponential.value}"
        self.value_params[exponential_mean_key] = exponential_mean


class InfectiousConfigurationConstant(InfectiousConfiguration):
    def __init__(self, constant_duration=3):
        super().__init__(DCParams.constant.value)
        constant_duration_key = f"{self.model_property}_{DCValues.constant.value}"
        self.value_params[constant_duration_key] = constant_duration


class InfectiousConfigurationUniform(InfectiousConfiguration):
    def __init__(self, uniform_min=2, uniform_max=10):
        super().__init__(DCParams.uniform.value)
        uniform_max_key = f"{self.model_property}_{DCValues.uniform_max.value}"
        uniform_min_key = f"{self.model_property}_{DCValues.uniform_min.value}"
        self.value_params[uniform_max_key] = uniform_max
        self.value_params[uniform_min_key] = uniform_min

