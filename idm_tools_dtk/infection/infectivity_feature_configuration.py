from idm_tools_dtk.utilities.distrubution_configuration import DCParams, DCValues, DistributionConfiguration
from idm_tools_dtk.utilities.feature_configuration import EnableableFeatureConfiguration

class InfectivityKeys:
    updates_per_timestep = "Infection_Updates_Per_Timestep"
    symptomatic_offset = "Symptomatic_Infectious_Offset"
    pass

class InfectivityConfiguration(DistributionConfiguration):
    def __init__(self, duration_type,
                 updates_per_timestep:int=None,
                 symptomatic_offset_days:int=None):
        super().__init__("Base_Infectivity")
        self.distribution_type = duration_type
        if updates_per_timestep is None:
            updates_per_timestep = 1
            self.assumptions[InfectivityKeys.updates_per_timestep] = updates_per_timestep
        if symptomatic_offset_days is None:
            symptomatic_offset_days = 0
            self.assumptions[InfectivityKeys.symptomatic_offset] = symptomatic_offset_days
        self.value_params[InfectivityKeys.updates_per_timestep] = updates_per_timestep
        self.value_params[InfectivityKeys.symptomatic_offset] = symptomatic_offset_days
        # TODO: symptomatic offset is Generic_Sim only. Should handle this later.
        pass
    pass

class InfectivityConfigurationConstant(InfectivityConfiguration):
    def __init__(self, constant_infectivity:float=3.5,
                 updates_per_timestep:int=1,
                 symptomatic_offset_days:int=0):
        super().__init__(DCParams.constant.value,
                         updates_per_timestep=updates_per_timestep,
                         symptomatic_offset_days=symptomatic_offset_days)
        constant_distribution_key = f"{self.model_property}_{DCValues.constant.value}"
        self.value_params[constant_distribution_key] = constant_infectivity
        pass
    pass

class InfectivityConfigurationGaussian(InfectivityConfiguration):
    def __init__(self, gaussian_mean_infectivity:float,
                 gaussian_sigma:float=0.5,
                 updates_per_timestep:int=1,
                 symptomatic_offset_days:int=0):
        super().__init__(DCParams.gaussian.value,
                         updates_per_timestep=updates_per_timestep,
                         symptomatic_offset_days=symptomatic_offset_days)
        gaussian_mean_key = f"{self.model_property}_{DCValues.gaussian_mean.value}"
        gaussian_sigma_key = f"{self.model_property}_{DCValues.gaussian_sigma.value}"
        self.value_params[gaussian_mean_key] = gaussian_mean_infectivity
        self.value_params[gaussian_sigma_key] = gaussian_sigma
    pass

class InfectivityConfigurationExponential(InfectivityConfiguration):
    def __init__(self, exponential_mean_infectivity:float,
                 updates_per_timestep:int=1,
                 symptomatic_offset_days:int=0):
        super().__init__(DCParams.exponential.value,
                         updates_per_timestep=updates_per_timestep,
                         symptomatic_offset_days=symptomatic_offset_days)
        exponential_mean_key = f"{self.model_property}_{DCValues.exponential.value}"
        self.value_params[exponential_mean_key] = exponential_mean_infectivity
    pass

class InfectivityConfigurationUniform(InfectivityConfiguration):
    def __init__(self, uniform_min_infectivity:float,
                 uniform_max_infectivity:float,
                 updates_per_timestep:int=1,
                 symptomatic_offset_days:int=0):
        super().__init__(DCParams.uniform.value,
                         updates_per_timestep=updates_per_timestep,
                         symptomatic_offset_days=symptomatic_offset_days)
        uniform_max_key = f"{self.model_property}_{DCValues.uniform_max.value}"
        uniform_min_key = f"{self.model_property}_{DCValues.uniform_min.value}"
        self.value_params[uniform_max_key] = uniform_max_infectivity
        self.value_params[uniform_min_key] = uniform_min_infectivity
    pass

class InfectivityScalingKeys:
    enable = "Enable_Infectivity_Scaling"
    density = "Enable_Infectivity_Scaling_Density"
    exponential = "Enable_Infectivity_Scaling_Exponential"
    boxcar = "Enable_Infectivity_Scaling_Boxcar"
    climate = "Enable_Infectivity_Scaling_Climate"
    sinousoid = "Enable_Infectivity_Scaling_Sinusoid"
    pass

class InfectivityScalingDensityKeys:
    enable = InfectivityScalingKeys.density
    halfmax = "Infectivity_Population_Density_HalfMax"
    pass

class InfectivityScalingExponentialKeys:
    enable = InfectivityScalingKeys.exponential
    baseline = "Infectivity_Exponential_Baseline"
    delay = "Infectivity_Exponential_Delay"
    rate = "Infectivity_Exponential_Rate"
    pass

class InfectivityScalingFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable:bool=False,
                 boxcar:bool=False,
                 climate:bool=False,
                 sinusoid:bool=False
                 ):
        super().__init__(feature_name="Infectivity Scaling",
                         enable_parameter=InfectivityScalingKeys.enable)
        self.feature_params[InfectivityScalingKeys.enable] = enable
        if enable:
            self.feature_params[InfectivityScalingKeys.boxcar] = boxcar
            self.feature_params[InfectivityScalingKeys.climate] = climate
            self.feature_params[InfectivityScalingKeys.sinousoid] = sinusoid
            pass
        pass
    pass

class InfectivityScalingDensityFeatureConfiguration(InfectivityScalingFeatureConfiguration):
    def __init__(self, halfmax:float=10):
        super().__init__(enable=True)
        self.feature_params[InfectivityScalingDensityKeys.enable] = True
        self.feature_params[InfectivityScalingDensityKeys.halfmax] = halfmax
        pass
    pass

class InfectivityScalingExponentialFeatureConfiguration(InfectivityScalingFeatureConfiguration):
    def __init__(self, baseline:float=0.0,
                 delay:float=0.0,
                 rate:float=0.0):
        super().__init__(enable=True)
        self.feature_params[InfectivityScalingExponentialKeys.enable] = True
        self.feature_params[InfectivityScalingExponentialKeys.baseline] = baseline
        self.feature_params[InfectivityScalingExponentialKeys.delay] = delay
        self.feature_params[InfectivityScalingExponentialKeys.rate] = rate
        pass
    pass


