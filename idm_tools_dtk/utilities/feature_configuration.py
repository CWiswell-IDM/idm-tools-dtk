class FeatureConfiguration():
    def __init__(self, feature_name):
        self.feature_name = feature_name
        self.master_parameter = None
        self.master_parameter_value = None
        self.feature_params = {}
        self.config_keys = {}
        pass

    def get_config_params(self):
        config_params = {}
        for k in self.feature_params:
            config_value = self.feature_params[k]
            if type(config_value) == bool:
                if config_value:
                    config_value = 1
                else:
                    config_value = 0
            if config_value is not None:
                config_params[k] = config_value
        return config_params


class EnableableFeatureConfiguration(FeatureConfiguration):
    def __init__(self, feature_name, enable_parameter, parent_parameter=None):
        super().__init__(feature_name=feature_name)
        self.master_parameter = enable_parameter
        self.master_parameter_value = True
        self.parent_parameter = parent_parameter
        pass
    pass

class EnumeratedFeatureConfiguration(FeatureConfiguration):
    def __init__(self, feature_name, type_enum_parameter, parent_parameter=None):
        super().__init__(feature_name=feature_name)
        self.master_parameter = type_enum_parameter

#TODO: something smart about master parameters.
# either when "get_config_params" is called it checks (not sure what to check) or
# put the responsibility on the caller that if they set a non-master feature...
# they need to set the master feature as well.