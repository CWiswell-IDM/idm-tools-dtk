from idm_tools_dtk.utilities.feature_configuration import EnableableFeatureConfiguration

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
