from copy import deepcopy
import json
from incubation_period_configuration import IncubationConfiguration, IncubationConfigurationGaussian
from infectious_period_configuration import InfectiousConfiguration, InfectiousConfigurationExponential

params = None
with open("minimum_default_config.json") as infile:
    params = json.load(infile)


def get_default_config(inc_config=None, inf_config=None):
    local_params = deepcopy(params)
    with open("Assumptions.txt","w") as outfile:
        if inc_config == None:
            inc_config = IncubationConfigurationGaussian()
            outfile.write(f"Incubation Configuration Params: {inc_config.get_config_params()}\n")
        incubation_params = inc_config.get_config_params()

        if inf_config == None:
            inf_config = InfectiousConfigurationExponential()
            outfile.write(f"Infectious Period Params: {inf_config.get_config_params()}\n")
        infectious_params = inf_config.get_config_params()

        epi_params = {**incubation_params, **infectious_params}
        print(epi_params)
        for k in epi_params:
            local_params['parameters'][k] = epi_params[k]
    return local_params

