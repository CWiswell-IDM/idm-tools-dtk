from idm_tools_dtk.utilities.distrubution_configuration import DCParams, DistributionConfiguration
from idm_tools_dtk.utilities.feature_configuration import EnableableFeatureConfiguration

class InfectivityKeys:
    base = "Base_Infectivity"
    updates_per_timestep = "Infection_Updates_Per_Timestep"
    symptomatic_offset = "Symptomatic_Infectious_Offset"
    pass

class InfectivityConfiguration(DistributionConfiguration):
    def __init__(self, duration_type,
                 updates_per_timestep:int=1,
                 symptomatic_offset_days:int=0):
        super().__init__("Infectivity")
        self.distribution_type = duration_type
        self.value_params[InfectivityKeys.updates_per_timestep] = updates_per_timestep
        self.value_params[InfectivityKeys.symptomatic_offset] = symptomatic_offset_days
        # TODO: symptomatic offset is Generic_Sim only. Should handle this later.
        pass
    pass

class InfectivityConfigurationConstant(InfectivityConfiguration):
    def __init__(self, base_infectivity:float=3.5):
        super().__init__(DCParams.constant.value)
        self.value_params[InfectivityKeys.base] = base_infectivity
        pass
    pass

class InfectivityConfigurationGaussian(InfectivityConfiguration):
    def __init__(self):
        super().__init__(DCParams.gaussian.value)
        raise NotImplementedError("this feature isn't available yet")
    pass

class InfectivityConfigurationExponential(InfectivityConfiguration):
    def __init__(self):
        super().__init__(DCParams.exponential.value)
        raise NotImplementedError("this feature isn't available yet")
    pass

class InfectivityConfigurationUniform(InfectivityConfiguration):
    def __init__(self):
        super().__init__(DCParams.uniform.value)
        raise NotImplementedError("this feature isn't available yet")
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


