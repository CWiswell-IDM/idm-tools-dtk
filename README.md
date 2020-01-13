# idm-tools-dtk

Tools for the creation of EMOD simulation configuration files through python classes.

Known limitations
- only works with generic model
- no classes or functions are commented
- all classes and functions are hand-coded, cannot be schema generated at this time
- no migration files are handled currently
- does no work for other files, including Demographics Files, Migration Files, and Campaign Files
- not all assumptions are currently captured in the resulting configuration file

Example:
From the tests folder, run the file try_emod_sim.py.
> python try_emod_sim.py

This will produce a file in that folder called "config.json".  Take a current build of the DtkTrunk master branch, and consume the file like so:
> Eradication.exe -C config.json

Expected results: This should run a 365 day simulation against default demographics with no infections.  The configuration file should contain a list of assumptions in the building of the configuration file.

Each parameter in the generic model is contained within a class. For example:



    class StrainTrackingKeys:
        enable = "Enable_Strain_Tracking"
        num_clades = "Number_of_Clades"
        log2_genomes_per_clade = "Log2_Number_of_Genomes_per_Clade"
        pass


    class StrainTrackingFeatureConfiguration(EnableableFeatureConfiguration):
        def __init__(self, enable,
                     num_clades:int=1,
                     log2_genomes_per_clade:int=0):
            super().__init__(feature_name="Strain Tracking",
                             enable_parameter=StrainTrackingKeys.enable)
            self.feature_params[StrainTrackingKeys.enable] = enable
            if enable:
                self.feature_params[StrainTrackingKeys.num_clades] = num_clades,
                self.feature_params[StrainTrackingKeys.log2_genomes_per_clade] = log2_genomes_per_clade
                pass
            pass
        pass


