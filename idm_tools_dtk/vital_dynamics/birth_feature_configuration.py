from idm_tools_dtk.utilities.feature_configuration import EnableableFeatureConfiguration, EnumeratedFeatureConfiguration
from idm_tools_dtk.vital_dynamics.vital_dynamics_configuration import VitalDynamicsKeys

class BirthKeys:
    enable = VitalDynamicsKeys.birth
    dependence = "Birth_Rate_Dependence"
    time_dependence = "Birth_Rate_Time_Dependence"
    demographics_birth = "Enable_Demographics_Birth"
    maternal_transmission = "Enable_Maternal_Infection_Transmission"
    maternal_transmission_probability = "Maternal_Infection_Transmission_Probability"
    x_birth = "x_Birth"
    all_keys = [enable, time_dependence, demographics_birth,
                maternal_transmission, x_birth]
    pass


class BirthRateDependenceKeys:
    type_enum = BirthKeys.dependence
    all_keys = [type_enum]
    class enum_options:
        fixed = "FIXED_BIRTH_RATE"
        pop_dependent = "POPULATION_DEP_RATE"
        demo_depdendent = "DEMOGRAPHIC_DEP_RATE"
        ind_pregnancies = "INDIVIDUAL_PREGNANCIES"
        ind_pregnancies_age_and_year = "INDIVIDUAL_PREGNANCIES_BY_AGE_AND_YEAR"
        pass
    pass

class BirthRateTimeDependenceKeys:
    type_enum = BirthKeys.time_dependence
    sinusoid_amplitude = "Birth_Rate_Sinusoidal_Forcing_Amplitude"
    sinusiod_phase = "Birth_Rate_Sinusoidal_Forcing_Phase"
    boxcar_amplitude = "Birth_Rate_Boxcar_Forcing_Amplitude"
    boxcar_start = "Birth_Rate_Boxcar_Forcing_End_Time"
    boxcar_end = "Birth_Rate_Boxcar_Forcing_Start_Time"
    all_keys = [type_enum, sinusoid_amplitude, sinusiod_phase,
                boxcar_start, boxcar_end, boxcar_amplitude]
    class enum_options:
        none = "NONE"
        sinusoid = "SINUSOIDAL_FUNCTION_OF_TIME"
        boxcar = "ANNUAL_BOXCAR_FUNCTION"
        pass
    pass


class BirthFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable: bool, x_birth: float=1.0,
                 time_dependence=BirthRateTimeDependenceKeys.enum_options.none,
                 demographics_birth:bool=False,
                 maternal_transmission:bool=False,
                 maternal_transmission_probability:float=0.0
                 ):
        super().__init__(feature_name="Birth",
                         enable_parameter=BirthKeys.enable,
                         parent_parameter=VitalDynamicsKeys.enable)
        # TODO: Figure out how to roll the various birth features in here, and collect assumptions
        for k in BirthKeys.all_keys:
            self.feature_params[k] = None
            pass
        self.feature_params[BirthKeys.enable] = enable
        self.demographics_params = {}
        if enable:
            self.feature_params[BirthKeys.x_birth] = x_birth
            self.feature_params[BirthKeys.time_dependence] = time_dependence
            self.feature_params[BirthKeys.demographics_birth] = demographics_birth
            self.feature_params[BirthKeys.maternal_transmission] = maternal_transmission
            if maternal_transmission:
                self.feature_params[BirthKeys.maternal_transmission_probability] = \
                    maternal_transmission_probability
            pass
        pass
    pass

# region timedependence

class BirthRateTimeDependenceFeatureConfiguration(EnumeratedFeatureConfiguration):
    def __init__(self, enum_setting):
        super().__init__("BirthRateTimeDependence", BirthRateTimeDependenceKeys.type_enum,
                         parent_parameter=BirthKeys.enable)
        self.feature_params[BirthRateTimeDependenceKeys.type_enum] = enum_setting
        pass
    pass

class BirthRateNoTimeDependenceFeatureConfiguration(BirthRateTimeDependenceFeatureConfiguration):
    def __init__(self):
        super().__init__(enum_setting=BirthRateTimeDependenceKeys.enum_options.none)
        pass
    pass

class BirthRateSinusoidalTimeDependenceFeatureConfiguration(BirthRateTimeDependenceFeatureConfiguration):
    def __init__(self, amplitude: float, phase: float):
        super().__init__(enum_setting=BirthRateTimeDependenceKeys.enum_options.sinusoid)
        self.feature_params[BirthRateTimeDependenceKeys.sinusiod_phase] = phase
        self.feature_params[BirthRateTimeDependenceKeys.sinusoid_amplitude] = amplitude
        pass
    pass

class BirthRateBoxcarTimeDependenceFeatureConfiguration(BirthRateTimeDependenceFeatureConfiguration):
    def __init__(self, amplitude: float, start_time: float, end_time: float):
        super().__init__(enum_setting=BirthRateTimeDependenceKeys.enum_options.boxcar)
        self.feature_params[BirthRateTimeDependenceKeys.boxcar_amplitude] = amplitude
        self.feature_params[BirthRateTimeDependenceKeys.boxcar_start] = start_time
        self.feature_params[BirthRateTimeDependenceKeys.boxcar_end] = end_time
        pass
    pass

# endregion

# region birth_rate_dependence
class BirthRateDependenceFeatureConfiguration(EnumeratedFeatureConfiguration):
    def __init__(self, enum_setting):
        super().__init__("BirthRateDependence", BirthRateDependenceKeys.type_enum,
                         parent_parameter=BirthKeys.enable)
        self.feature_params[BirthRateDependenceKeys.type_enum] = enum_setting
        pass
    pass

# endregion

# region demographics_birth

class BirthDemographicsFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable: bool):
        super().__init__(feature_name="DemographicsBirth", enable_parameter=BirthKeys.demographics_birth,
                         parent_parameter=BirthKeys.enable)
        self.feature_params[BirthKeys.demographics_birth] = enable

# endregion

# region maternal_infection_transmission

class BirthMaternalTransmissionFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable: bool, probability: float=0.0):
        super().__init__(feature_name="MaternalTransmission",
                         enable_parameter=BirthKeys.maternal_transmission,
                         parent_parameter=BirthKeys.enable)
        self.feature_params[BirthKeys.maternal_transmission] = enable
        if enable:
            self.feature_params[BirthKeys.maternal_transmission_probability] = probability
            pass
        pass
    pass


# endregion


