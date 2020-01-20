from os import makedirs
from shutil import rmtree

import idm_tools_dtk.emod_simulation_configuration as emod

sim = emod.EmodSimulationConfiguration()
sim.write_config_file("DEBUG_config.json")

from idm_tools_dtk.dtk_simulation.dtk_simulation_configuration import SimulationConfiguration as dtk_sim, SimulationKeys
from idm_tools_dtk.demographics.demographics_feature_configuration import DemographicsBuiltinFeatureConfiguration as d_builtin

node_populations = [100, 500, 1000]
my_folder = "DEBUG_example_sims/node_population_sweep"
rmtree(my_folder, ignore_errors=True)
makedirs(my_folder)
for pop in node_populations:
    demog = d_builtin(node_population=pop)
    cfg_name = f"builtin_nodepop_{pop}_config.json"
    my_sim = dtk_sim(sim_type=SimulationKeys.sim_types_enum.generic,
                     config_name=cfg_name)
    sim = emod.EmodSimulationConfiguration(demo_config=demog,
                                           sim_config=my_sim)
    sim.write_config_file(config_filename=cfg_name,
                          config_path=my_folder)
    pass

from idm_tools_dtk.dtk_simulation.simulation_miscellaneous_configs import PopulationScalingFeatureConfiguration as scale_cfg
scale_factors = [1.0, 2.0, 5.0]
my_folder = "DEBUG_example_sims/scale_factor_sweep"
rmtree(my_folder, ignore_errors=True)
makedirs(my_folder)
for sf in scale_factors:
    cfg_name = f"scalefactor_{sf}_config.json"
    my_scaling = scale_cfg(multiplier=sf)
    my_sim = dtk_sim(sim_type=SimulationKeys.sim_types_enum.generic,
                     config_name=cfg_name, population_scaling_config=my_scaling)
    sim = emod.EmodSimulationConfiguration(sim_config=my_sim)
    sim.write_config_file(config_filename=cfg_name,
                          config_path=my_folder)
    pass
pass

from idm_tools_dtk.individual_sampling.individual_sampling_feature_configuration import IndividualSamplingFixedFeatureConfiguration as fixed_sampling
sample_rates = [1.0, 0.8, 0.5, 0.1]
my_folder = "DEBUG_example_sims/sampling_rate_population_sweep"
rmtree(my_folder, ignore_errors=True)
makedirs(my_folder)

for sr in sample_rates:
    for pop in node_populations:
        cfg_name = f"samplerate_{sr}_nodepop_{pop}_config.json"
        my_sampling = fixed_sampling(fixed_rate=sr)
        my_demog = d_builtin(node_population=pop)
        my_sim = dtk_sim(sim_type=SimulationKeys.sim_types_enum.generic,
                         config_name=cfg_name)
        sim = emod.EmodSimulationConfiguration(demo_config=my_demog,
                                               individual_sampling_config=my_sampling,
                                               sim_config=my_sim)
        sim.write_config_file(config_filename=cfg_name,
                              config_path=my_folder)
        pass
    pass




