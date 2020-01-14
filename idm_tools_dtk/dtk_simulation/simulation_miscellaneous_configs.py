from feature_configuration import FeatureConfiguration, EnableableFeatureConfiguration, EnumeratedFeatureConfiguration

class PopulationScalingKeys:
    type_enum = "Population_Scale_Type"
    population_multiplier = "x_Base_Population"
    class enum_options:
        input_file = "USE_INPUT_FILE"
        fixed = "FIXED_SCALING"

class PopulationScalingFeatureConfiguration(EnumeratedFeatureConfiguration):
    def __init__(self, multiplier:float=1.0):
        super().__init__(feature_name="Population Scaling",
                         type_enum_parameter=PopulationScalingKeys.type_enum)
        if multiplier != 1.0:
            self.feature_params[PopulationScalingKeys.type_enum] = PopulationScalingKeys.enum_options.fixed
            self.feature_params[PopulationScalingKeys.population_multiplier] = multiplier
        else:
            self.feature_params[PopulationScalingKeys.type_enum] = PopulationScalingKeys.enum_options.input_file
            pass
        pass
    pass

class SimulationDurationKeys:
    timestep_count = "Simulation_Duration"
    timestep_size = "Simulation_Timestep"
    timestep_start = "Start_Time"
    enable_zero_infectivity_termination = "Enable_Termination_On_Zero_Total_Infectivity"
    min_end_time = "Minimum_End_Time"
    enable_skipping = "Enable_Skipping"
    all_keys = [timestep_size, timestep_count, timestep_start,
                enable_zero_infectivity_termination,
                min_end_time,
                enable_skipping]


class ZeroInfectivityTerminationKeys:
    enable = "Enable_Termination_On_Zero_Total_Infectivity"
    min_end_time = "Minimum_End_Time"


class ZeroInfectivityTerminationFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable,
                 min_end_timestep:int=50):
        super().__init__(feature_name="Zero Infectivity Termination",
                         enable_parameter=SimulationDurationKeys.enable_zero_infectivity_termination)
        self.feature_params[SimulationDurationKeys.enable_zero_infectivity_termination] = enable
        if enable:
            self.feature_params[SimulationDurationKeys.min_end_time] = min_end_timestep

    pass


class SimulationDurationFeatureConfiguration(FeatureConfiguration):
    def __init__(self,
                 ts_count:int,
                 ts_size:float=1.0,
                 ts_start:int=0,
                 enable_skipping:bool=False,
                 infectivity_termination:ZeroInfectivityTerminationFeatureConfiguration=None):
        super().__init__(feature_name="Simulation Duration")
        for k in SimulationDurationKeys.all_keys:
            self.feature_params[k] = None
            pass
        self.feature_params[SimulationDurationKeys.timestep_count] = ts_count
        self.feature_params[SimulationDurationKeys.timestep_size] = ts_size
        self.feature_params[SimulationDurationKeys.timestep_start] = ts_start
        self.feature_params[SimulationDurationKeys.enable_skipping] = enable_skipping
        if not infectivity_termination:
            self.feature_params[SimulationDurationKeys.enable_zero_infectivity_termination] = False
        else:
            zi_params = infectivity_termination.get_config_params()
            self.feature_params = {**self.feature_params, **zi_params}
