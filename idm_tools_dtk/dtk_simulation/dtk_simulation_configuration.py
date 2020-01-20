from idm_tools_dtk.utilities.feature_configuration import FeatureConfiguration, EnableableFeatureConfiguration, EnumeratedFeatureConfiguration
from idm_tools_dtk.dtk_simulation.simulation_miscellaneous_configs import SimulationDurationFeatureConfiguration, \
    PopulationScalingFeatureConfiguration

class SimulationKeys:
    type_enum = "Simulation_Type"
    config_name = "Config_Name"
    custom_coordinator_events = "Custom_Coordinator_Events" # array
    custom_individual_events = "Custom_Individual_Events" # array
    custom_node_events = "Custom_Node_Events" # array
    load_balance_filename = "Load_Balance_Filename"
    random_seed = "Run_Number"
    enable_interventions = "Enable_Interventions"
    campaign_filename = "Campaign_Filename"
    class sim_types_enum:
        generic = "GENERIC_SIM"
        vector = "VECTOR_SIM"
        dengue = "DENGUE_SIM"
        malaria = "MALARIA_SIM"
        sti = "STI_SIM"
        hiv = "HIV_SIM"
        tbhiv = "TBHIV_SIM"
        environmental = "ENVIRONMENTAL_SIM"
        typhoid = "TYPHOID_SIM"
        airborne = "AIRBORNE_SIM"
        all_types = [generic, vector, dengue, malaria,
                     sti, hiv, tbhiv, environmental, typhoid,
                     airborne]
        pass
    pass


class EventRecorderKeys:
    coordinator = "Report_Coordinator_Event_Recorder"
    event = "Report_Event_Recorder"
    node = "Report_Node_Event_Recorder"
    surveillance = "Report_Surveillance_Event_Recorder"
    # TODO: there are also individual property keys for all of these but I'm not sure how they work
    class event_keys:
        events = "Report_Event_Recorder_Events"
        ignore_flag = "Report_Event_Recorder_Ignore_Events_In_List"
        pass
    class coordinator_keys:
        events = "Report_Coordinator_Event_Recorder_Events"
        ignore_flag ="Report_Coordinator_Event_Recorder_Ignore_Events_In_List"
        pass
    class node_keys:
        events = "Report_Node_Event_Recorder_Events"
        ignore_flag = "Report_Node_Event_Recorder_Ignore_Events_In_List"
        pass
    class surveillance_keys:
        events = "Report_Surveillance_Event_Recorder_Events"
        ignore_flag = "Report_Surveillance_Event_Recorder_Ignore_Events_In_List"
        pass
    pass

class ReportEventsFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable, ignore_events:bool=False, events:list=None):
        super().__init__(feature_name="Report Event Recorder",
                         enable_parameter=EventRecorderKeys.event)
        self.feature_params[EventRecorderKeys.event] = enable
        if enable:
            self.feature_params[EventRecorderKeys.event_keys.events] = events
            self.feature_params[EventRecorderKeys.event_keys.ignore_flag] = ignore_events
            pass
        pass
    pass

class ReportCoordinatorEventsFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable, ignore_events:bool=False, events:list=None):
        super().__init__(feature_name="Report Coordinator Event Recorder",
                         enable_parameter=EventRecorderKeys.coordinator)
        self.feature_params[EventRecorderKeys.coordinator] = enable
        if enable:
            self.feature_params[EventRecorderKeys.coordinator_keys.events] = events
            self.feature_params[EventRecorderKeys.coordinator_keys.ignore_flag] = ignore_events
            pass
        pass
    pass

class ReportNodeEventsFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable, ignore_events:bool=False, events:list=None):
        super().__init__(feature_name="Report Node Event Recorder",
                         enable_parameter=EventRecorderKeys.node)
        self.feature_params[EventRecorderKeys.node] = enable
        if enable:
            self.feature_params[EventRecorderKeys.node_keys.events] = events
            self.feature_params[EventRecorderKeys.node_keys.ignore_flag] = ignore_events
            pass
        pass
    pass


class ReportSurveillanceEventsFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable, ignore_events:bool=False, events:list=None):
        super().__init__(feature_name="Report Surveillance Event Recorder",
                         enable_parameter=EventRecorderKeys.surveillance)
        self.feature_params[EventRecorderKeys.surveillance] = enable
        if enable:
            self.feature_params[EventRecorderKeys.surveillance_keys.events] = events
            self.feature_params[EventRecorderKeys.surveillance_keys.ignore_flag] = ignore_events
            pass
        pass
    pass


class ReportingKeys:
    inset_chart = "Enable_Default_Reporting"
    demographics = "Enable_Demographics_Reporting"
    individual_properties = "Enable_Property_Output"
    spatial_output = "Enable_Spatial_Output"
    all_boolean_keys = [inset_chart, demographics, individual_properties, spatial_output]
    spatial_channel_list = "Spatial_Output_Channels"
    custom_reports_filename = "Custom_Reports_Filename"
    class spatial_channels:
        climate_air_temp = "Air_Temperature"
        climate_land_temp = "Land_Temperature"
        climate_rainfall = "Rainfall"
        climate_relative_humidity = "Relative_Humidity"
        demog_births = "Births"
        demog_population = "Population"
        epi_disease_deaths = "Disease_Deaths"
        epi_human_infectious_reservoir = "Human_Infectious_Reservoir"
        epi_infection_rate = "Infection_Rate"
        epi_new_infections = "New_Infections"
        epi_new_reported_infections = "New_Reported_Infections"
        epi_prevalence = "Prevalence"
        sim_campaign_cost = "Campaign_Cost"
        all_channels = [climate_air_temp, climate_land_temp, climate_rainfall,
                        climate_relative_humidity, demog_births, demog_population,
                        epi_disease_deaths, epi_human_infectious_reservoir, epi_infection_rate,
                        epi_new_infections, epi_new_reported_infections, epi_prevalence,
                        sim_campaign_cost]
        pass
    pass


class ReportingConfiguration(FeatureConfiguration):
    def __init__(self,
                 enable_inset_chart:bool=True,
                 enable_demographics_summary:bool=False,
                 enable_property_report:bool=False,
                 enable_custom_reports:bool=False,
                 enable_spatial_output:bool=False,
                 custom_reports_filename:str="RunAllCustomReports",
                 spatial_channel_list:list=None,
                 report_events:ReportEventsFeatureConfiguration=None,
                 report_coordinator_events:ReportCoordinatorEventsFeatureConfiguration=None,
                 report_node_events:ReportNodeEventsFeatureConfiguration=None,
                 report_surveillance_events:ReportSurveillanceEventsFeatureConfiguration=None):
        super().__init__(
            feature_name="Simulation Reporting"
        )
        for k in ReportingKeys.all_boolean_keys:
            self.feature_params[k] = False
            pass
        if enable_inset_chart:
            self.feature_params[ReportingKeys.inset_chart] = True
        if enable_demographics_summary:
            self.feature_params[ReportingKeys.demographics] = True
        if enable_property_report:
            self.feature_params[ReportingKeys.individual_properties] = True

        if not enable_custom_reports:
            self.feature_params[ReportingKeys.custom_reports_filename] = ""
        else:
            self.feature_params[ReportingKeys.custom_reports_filename] = custom_reports_filename

        if not report_events:
            report_events = ReportEventsFeatureConfiguration(enable=False)
            pass
        report_event_params = report_events.get_config_params()
        self.feature_params = {**self.feature_params, **report_event_params}

        if not report_coordinator_events:
            report_coordinator_events = ReportCoordinatorEventsFeatureConfiguration(enable=False)
            pass
        report_coordinator_event_params = report_coordinator_events.get_config_params()
        self.feature_params = {**self.feature_params, **report_coordinator_event_params}

        if not report_node_events:
            report_node_events = ReportNodeEventsFeatureConfiguration(enable=False)
            pass
        report_node_event_params = report_node_events.get_config_params()
        self.feature_params = {**self.feature_params, **report_node_event_params}

        if not report_surveillance_events:
            report_surveillance_events = ReportSurveillanceEventsFeatureConfiguration(enable=False)
            pass
        report_surveillance_event_params = report_surveillance_events.get_config_params()
        self.feature_params = {**self.feature_params, **report_surveillance_event_params}

        if enable_spatial_output:
            self.feature_params[ReportingKeys.spatial_output] = True
            self.channels_to_report = []
            for c in spatial_channel_list:
                if c in ReportingKeys.spatial_channels.all_channels:
                    self.channels_to_report.append(c)
                else:
                    raise ValueError(f"Attempted to add channels {spatial_channel_list} to spatial reports,"
                                     f" only channels in this list {ReportingKeys.spatial_channels.all_channels} "
                                     f"are valid. {c} is not in that list.\n")
                pass
            self.feature_params[ReportingKeys.spatial_channel_list] = self.channels_to_report

class SerializationKeys:
    type_enum = "Serialization_Type"
    timesteps = "Serialization_Time_Steps"
    times = "Serialization_Times"
    class enum_options:
        none = "NONE"
        steps = "TIMESTEP"
        times = "TIME"
        pass
    pass


class SerializationConfiguration(EnumeratedFeatureConfiguration):
    def __init__(self, serial_type:str,
                 times:list=None):
        super().__init__(feature_name="Serialization",
                         type_enum_parameter=SerializationKeys.type_enum)
        self.feature_params[SerializationKeys.type_enum] = serial_type
        if not serial_type == SerializationKeys.enum_options.none:
            if not times:
                times = []
                pass
            pass
            if serial_type == SerializationKeys.enum_options.steps:
                self.feature_params[SerializationKeys.timesteps] = times
                pass
            if serial_type == SerializationKeys.enum_options.times:
                self.feature_params[SerializationKeys.times] = times
                pass
            pass
        pass
    pass

class SimulationConfiguration(FeatureConfiguration):
    def __init__(self,
                 sim_type:str,
                 run_number:int=1,
                 config_name:str=None,
                 coordinator_events:list=None,
                 individual_events:list=None,
                 node_events:list=None,
                 load_balance_filename:str=None,
                 reporting_config:ReportingConfiguration=None,
                 duration_config:SimulationDurationFeatureConfiguration=None,
                 population_scaling_config:PopulationScalingFeatureConfiguration=None,
                 serialization_config:SerializationConfiguration=None,
                 campaign_filename:str=None):
        super().__init__(
            feature_name="DTK Simulation"
        )
        self.assumptions = {} # TODO: roll up these assumptions into the EMOD configuration object

        if sim_type in SimulationKeys.sim_types_enum.all_types:
            self.feature_params[SimulationKeys.type_enum] = sim_type
        else:
            raise ValueError(f"Sim type {sim_type} not found in valid types {SimulationKeys.sim_types_enum.all_types}.\n")
        self.feature_params[SimulationKeys.random_seed] = run_number
        if not config_name:
            config_name = f"{sim_type}_run_number_{run_number}"
        self.feature_params[SimulationKeys.config_name] = config_name
        if not coordinator_events:
            coordinator_events = []
        self.feature_params[SimulationKeys.custom_coordinator_events] = coordinator_events
        if not individual_events:
            individual_events = []
        self.feature_params[SimulationKeys.custom_individual_events] = individual_events
        if not node_events:
            node_events = []
        self.feature_params[SimulationKeys.custom_node_events] = node_events
        if not load_balance_filename:
            load_balance_filename = ""
        self.feature_params[SimulationKeys.load_balance_filename] = load_balance_filename
        if not campaign_filename:
            self.feature_params[SimulationKeys.enable_interventions] = False
        else:
            self.feature_params[SimulationKeys.enable_interventions] = True
            self.feature_params[SimulationKeys.campaign_filename] = campaign_filename
            pass

        if not reporting_config:
            reporting_config = ReportingConfiguration()
            self.assumptions[reporting_config.feature_name] = reporting_config.get_config_params()
            pass
        self.reporting_config = reporting_config

        if not duration_config:
            duration_config = SimulationDurationFeatureConfiguration(365)
            self.assumptions[duration_config.feature_name] = duration_config.get_config_params()
            pass
        self.duration_config = duration_config

        if not population_scaling_config:
            population_scaling_config = PopulationScalingFeatureConfiguration()
            self.assumptions[population_scaling_config.feature_name] = population_scaling_config.get_config_params()
            pass
        self.scaling_config = population_scaling_config

        if not serialization_config:
            serialization_config = SerializationConfiguration(serial_type=SerializationKeys.enum_options.none)
            self.assumptions[serialization_config.feature_name] = serialization_config.get_config_params()
            pass
        self.serialization_config = serialization_config

        self.feature_params = {**self.feature_params,
                               **self.reporting_config.get_config_params(),
                               **self.duration_config.get_config_params(),
                               **self.scaling_config.get_config_params(),
                               **self.serialization_config.get_config_params()}

        # TODO: add comments. These are parameters that the software needs but science doesn't
