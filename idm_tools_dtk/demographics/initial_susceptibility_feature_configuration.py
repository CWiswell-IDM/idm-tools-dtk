from idm_tools_dtk.utilities.feature_configuration import EnableableFeatureConfiguration

class SusceptibilityDistributionKeys:
    enable = "Enable_Initial_Susceptibility_Distribution"
    type_enum = "Susceptibility_Initialization_Distribution_Type"
    all_keys = [enable, type_enum]
    class enum_options:
        off = "DISTRIBUTION_OFF"
        simple = "DISTRIBUTION_SIMPLE"
        complex = "DISTRIBUTION_COMPLEX"
        pass
    pass

class InitialSusceptibilityFeatureConfiguration(EnableableFeatureConfiguration):
    def __init__(self, enable, distribution_type=None,
                 simple_distro_params=None, complex_distribution_tables=None):
        super().__init__(feature_name="Initial_Susceptiblity_Distribution",
                         enable_parameter=SusceptibilityDistributionKeys.enable,
                         parent_parameter="Enable_Immunity")
        for k in SusceptibilityDistributionKeys.all_keys:
            self.feature_params[k] = None
        self.feature_params[SusceptibilityDistributionKeys.enable] = enable
        self.demographics_params = {}
        if enable:
            self.feature_params[SusceptibilityDistributionKeys.type_enum] = distribution_type
            if distribution_type == SusceptibilityDistributionKeys.enum_options.off:
                pass
            elif distribution_type == SusceptibilityDistributionKeys.enum_options.simple:
                # TODO: how would we set the distribution in demographics?
                # Proposed: store them in an object (demographic_simple_initial_susceptibility_distribution)
                # and set that later.
                for k in simple_distro_params:
                    self.demographics_params[k] = simple_distro_params[k]
                pass
            elif distribution_type == SusceptibilityDistributionKeys.enum_options.complex:
                # TODO: how would we set the complex distributions?
                # There may be many per demographic node.
                # Proposed: Don't do it here. Ask the caller to set the demographics first,
                # and if they do the Susceptibility distribution tables then the demographics object
                # constructs the feature configuration and returns, asking them to
                # add it to their config / simulation
                for k in complex_distribution_tables:
                    self.demographics_params[k] = complex_distribution_tables[k]
                pass
            pass

    def get_demographics_params(self):
        return self.demographics_params
