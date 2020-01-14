from feature_configuration import EnableableFeatureConfiguration, EnumeratedFeatureConfiguration
from vital_dynamics_configuration import VitalDynamicsKeys

class DeathKeys:
    enable = VitalDynamicsKeys.natural_mortality
    dependence = "Death_Rate_Dependence"
    x_death = "x_Other_Mortality"
    all_keys = [enable, dependence, x_death]
    pass


class DeathRateDependenceKeys:
    type_enum = DeathKeys.dependence
    all_keys = [type_enum]
    class enum_options:
        none = "NOT_INITIALIZED"
        age_and_gender = "NONDISEASE_MORTALITY_BY_AGE_AND_GENDER"
        year_age_gender = "NONDISEASE_MORTALITY_BY_YEAR_AND_AGE_FOR_EACH_GENDER"
        pass
    pass


class DeathFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable: bool,
                 x_death: float=1.0,
                 rate_dependence=DeathRateDependenceKeys.enum_options.none):
        super().__init__(feature_name="Death",
                         enable_parameter=DeathKeys.enable,
                         parent_parameter=VitalDynamicsKeys.enable)
        for k in DeathKeys.all_keys:
            self.feature_params[k] = None
            pass
        self.feature_params[DeathKeys.enable] = enable
        self.demographics_params = {}
        if enable:
            self.feature_params[DeathKeys.x_death] = x_death
            self.feature_params[DeathKeys.dependence] = rate_dependence
            pass
        pass
    pass


class DeathAgeAndGenderFeatureConfiguration(DeathFeatureConfiguration):
    def __init__(self, x_death: float=1.0,
                 demographics_params: dict=None):
        super().__init__(enable=True,
                         x_death=x_death,
                         rate_dependence=DeathRateDependenceKeys.enum_options.age_and_gender)
        if demographics_params:
            self.demographics_params = demographics_params
        pass
    pass


class DeathYearAgeGenderFeatureConfiguration(DeathFeatureConfiguration):
    def __init__(self, x_death:float=1.0,
                 demographics_params:dict=None):
        super().__init__(enable=True,
                         x_death=x_death,
                         rate_dependence=DeathRateDependenceKeys.enum_options.year_age_gender)
        if demographics_params:
            self.demographics_params = demographics_params
        pass
    pass

