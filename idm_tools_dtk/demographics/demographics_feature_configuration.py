from feature_configuration import EnableableFeatureConfiguration

class DemographicsKeys:
    enable = "Enable_Demographics_Builtin"
    builtin_torus_size = "Default_Geography_Torus_Size"
    builtin_node_population = "Default_Geography_Initial_Node_Population"
    demographics_filenames = "Demographics_Filenames"
    enable_hint = "Enable_Heterogeneous_Intranode_Transmission"
    infectivity_reservoir = "Enable_Infectivity_Reservoir"
    initial_prevalence = "Enable_Initial_Prevalence"
    node_grid_size = "Node_Grid_Size"
    all_keys = [enable, builtin_node_population,
                builtin_torus_size, demographics_filenames,
                infectivity_reservoir, initial_prevalence]
    pass

class MigrationModelKeys:
    type_enum = "Migration_Model"

    class enum_options:
        none = "NO_MIGRATION"
        fixed = "FIXED_RATE_MIGRATION"
        pass

    pass


class MigrationPatternKeys:
    type_enum = "Migration_Pattern"

    class enum_options:
        random_walk = "RANDOM_WALK_DIFFUSION"
        single_roundtrips = "SINGLE_ROUND_TRIPS"
        waypoints_home = "WAYPOINTS_HOME"


class MigrationFeatureConfiguration(object):
    # TODO: Figure this out. Should be dependent on DemographicsCustom
    # TODO: If MigrationPattern == FIXED_RATE_MIGRATION then fill out pattern and filenames
    pass

class AgeInitializationKeys:
    type_enum = "Age_Initialization_Distribution_Type"

    class enum_options:
        off = "DISTRIBUTION_OFF"
        simple = "DISTRIBUTION_SIMPLE"
        complex = "DISTRIBUTION_COMPLEX"
        pass
    pass


class DemographicsFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable,
                 age_initialization_type:AgeInitializationKeys.enum_options=AgeInitializationKeys.enum_options.off,
                 node_grid_size:float=0.004167,
                 enable_hint:bool=False,
                 enable_reservoir:bool=False,
                 enable_initial_prevalence:bool=False):
        super().__init__(
            feature_name="Demographics Configuration",
            enable_parameter=DemographicsKeys.enable
        )
        for k in DemographicsKeys.all_keys:
            self.feature_params[k] = None
            pass
        self.feature_params[DemographicsKeys.enable] = enable
        self.feature_params[MigrationModelKeys.type_enum] = MigrationModelKeys.enum_options.none
        self.feature_params[AgeInitializationKeys.type_enum] = age_initialization_type
        self.feature_params[DemographicsKeys.enable_hint] = enable_hint
        self.feature_params[DemographicsKeys.initial_prevalence] = enable_initial_prevalence
        self.feature_params[DemographicsKeys.infectivity_reservoir] = enable_reservoir
        self.feature_params[DemographicsKeys.node_grid_size] = node_grid_size
        pass
    pass

class DemographicsBuiltinFeatureConfiguration(DemographicsFeatureConfiguration):
    def __init__(self,
                 torus_size:int=10,
                 node_population:int=1000):
        super().__init__(enable=True)
        self.feature_params[DemographicsKeys.builtin_torus_size] = torus_size
        self.feature_params[DemographicsKeys.builtin_node_population] = node_population
        pass
    pass

class DemographicsCustomFeatureConfiguration(DemographicsFeatureConfiguration):
    def __init__(self,
                 demographics_filename
                 ):
        super().__init__(enable=False)
        self.feature_params[DemographicsKeys.demographics_filenames] = [demographics_filename]
        #TODO: here is where we'd want to load the demographics file somewhere
        pass

    def add_overlay(self, overlay_filename):
        self.feature_params[DemographicsKeys.demographics_filenames].append(overlay_filename)
        pass
    pass



