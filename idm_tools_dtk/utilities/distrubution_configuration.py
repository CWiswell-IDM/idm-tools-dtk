from enum import Enum
from feature_configuration import FeatureConfiguration

class DCParams(Enum):
    type_key = "Distribution"
    constant = f"CONSTANT_{type_key.upper()}"
    uniform = f"UNIFORM_{type_key.upper()}"
    gaussian = f"GAUSSIAN_{type_key.upper()}"
    exponential = f"EXPONENTIAL_{type_key.upper()}"
    poisson = f"POISSON_{type_key.upper()}"
    log_normal = f"LOG_NORMAL_{type_key.upper()}"
    dual_constant = f"DUAL_CONSTANT_{type_key.upper()}"
    weibull = f"WEIBULL_{type_key.upper()}"
    dual_exponential = f"DUAL_EXPONENTIAL_{type_key.upper()}"

class DCValues(Enum):
    constant = "Constant"
    exponential = "Exponential"
    gaussian_mean = "Gaussian_Mean"
    gaussian_sigma = "Gaussian_Std_Dev"
    weibull_kappa = "Kappa"
    weibull_lambda = "Lambda"
    uniform_max = "Max"
    uniform_min = "Min"
    log_normal_mu = "Mu"
    log_normal_sigma = "Sigma"
    dual_exponential_mean_1 = "Mean_1"
    dual_exponential_mean_2 = "Mean_2"
    dual_exponential_proportion_1 = "Proportion_1"
    dual_constant_peak_2 = "Peak_2_Value"
    dual_constant_proportion_0 = "Proportion_0"
    poisson_mean = "Poisson_Mean"


class DistributionConfiguration(FeatureConfiguration):
    def __init__(self, model_property):
        super().__init__(feature_name=model_property)
        self.model_property = model_property
        self.distrubution_key = f"{self.model_property}_{DCParams.type_key.value}"
        self.value_params = {}
        pass

    def get_config_params(self):
        # Todo: return something here
        config_params = {}
        config_params[self.distrubution_key] = self.distribution_type
        for k in self.value_params:
            config_params[k] = self.value_params[k]
        return config_params



