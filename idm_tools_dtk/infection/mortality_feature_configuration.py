from feature_configuration import EnableableFeatureConfiguration

class DiseaseMortalityKeys:
    enable = "Enable_Disease_Mortality"
    time_course = "Mortality_Time_Course"
    base_probability = "Base_Mortality"

    class time_course_options:
        daily = "DAILY_MORTALITY"
        post_infectious = "MORTALITY_AFTER_INFECTIOUS"
        pass
    pass

class DiseaseMortalityFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable,
                 timecourse:DiseaseMortalityKeys.time_course_options=None,
                 base_probability:float=0.001):
        super().__init__(feature_name="Disease Mortality",
                         enable_parameter=DiseaseMortalityKeys.enable)
        self.feature_params[DiseaseMortalityKeys.enable] = enable
        if enable:
            self.feature_params[DiseaseMortalityKeys.time_course] = timecourse
            self.feature_params[DiseaseMortalityKeys.base_probability] = base_probability
            pass
        pass
    pass

