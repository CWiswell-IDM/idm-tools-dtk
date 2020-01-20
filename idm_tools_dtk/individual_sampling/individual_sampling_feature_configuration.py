from idm_tools_dtk.utilities.feature_configuration import EnumeratedFeatureConfiguration

class IndividualSamplingKeys:
    type_enum = "Individual_Sampling_Type"
    base_sample_rate = "Base_Individual_Sample_Rate"
    immune_threshold = "Immune_Threshold_For_Downsampling"
    max_node_pop_samples = "Max_Node_Population_Samples"
    immune_sample_rate = "Relative_Sample_Rate_Immune"
    all_keys = [type_enum, base_sample_rate, immune_threshold, max_node_pop_samples,
                immune_sample_rate]
    class enum_options:
        all = "TRACK_ALL"
        fixed = "FIXED_SAMPLING"
        adapt_pop_size = "ADAPTED_SAMPLING_BY_POPULATION_SIZE"
        adapt_age_group = "ADAPTED_SAMPLING_BY_AGE_GROUP"
        adapt_age_group_size = "ADAPTED_SAMPLING_BY_AGE_GROUP_AND_POP_SIZE"
        adapt_immune_state = "ADAPTED_SAMPLING_BY_IMMUNE_STATE"
        pass
    pass


class SamplingAgeGroupKeys:
    min_adult_age = "Minimum_Adult_Age_Years"
    at_birth = "Sample_Rate_Birth"
    class age_groups:
        birth_toddler = "Sample_Rate_0_18mo"
        toddler_years4 = "Sample_Rate_18mo_4yr"
        years05_09 = "Sample_Rate_5_9"
        years10_14 = "Sample_Rate_10_14"
        years15_19 = "Sample_Rate_15_19"
        years20_plus = "Sample_Rate_20_Plus"
        pass
    pass


class IndividualSamplingFeatureConfiguration(EnumeratedFeatureConfiguration):
    def __init__(self,
                 sample_type=IndividualSamplingKeys.enum_options.all):
        super().__init__(
            "Sampling Type",
            IndividualSamplingKeys.type_enum
        )
        for k in IndividualSamplingKeys.all_keys:
            self.feature_params[k] = None
        self.feature_params[IndividualSamplingKeys.type_enum] = sample_type
        pass
    pass


class IndividualSamplingFixedFeatureConfiguration(IndividualSamplingFeatureConfiguration):
    def __init__(self, fixed_rate:float):
        super().__init__(sample_type=IndividualSamplingKeys.enum_options.fixed)
        self.feature_params[IndividualSamplingKeys.base_sample_rate] = fixed_rate
        pass


class IndividualSamplingPopulationSizeFeatureConfiguration(IndividualSamplingFeatureConfiguration):
    def __init__(self,
                 max_node_pop_samples: int
                 ):
        super().__init__(sample_type=IndividualSamplingKeys.enum_options.adapt_pop_size)
        self.feature_params[IndividualSamplingKeys.max_node_pop_samples] = max_node_pop_samples
        pass
    pass


class IndividualSamplingAgeGroupFeatureConfiguration(IndividualSamplingFeatureConfiguration):
    def __init__(self,
                 adult_min_age_years:float=15,
                 atbirth:float=1.0,
                 birth_18months:float=1.0,
                 toddler_years04:float=1.0,
                 years05_years09:float=1.0,
                 years10_years14:float=1.0,
                 years15_years19:float=1.0,
                 years20_older:float=1.0
                 ):
        super().__init__(sample_type=IndividualSamplingKeys.enum_options.adapt_age_group)
        self.feature_params[SamplingAgeGroupKeys.min_adult_age] = adult_min_age_years
        self.feature_params[SamplingAgeGroupKeys.at_birth] = atbirth
        self.feature_params[SamplingAgeGroupKeys.age_groups.birth_toddler] = birth_18months
        self.feature_params[SamplingAgeGroupKeys.age_groups.toddler_years4] = toddler_years04
        self.feature_params[SamplingAgeGroupKeys.age_groups.years05_09] = years05_years09
        self.feature_params[SamplingAgeGroupKeys.age_groups.years10_14] = years10_years14
        self.feature_params[SamplingAgeGroupKeys.age_groups.years15_19] = years15_years19
        self.feature_params[SamplingAgeGroupKeys.age_groups.years20_plus] = years20_older
        pass
    pass


class IndividualSamplingAgeGroupSizeFeatureConfiguration(IndividualSamplingAgeGroupFeatureConfiguration):
    def __init__(self,
                 max_node_pop_samples: float,
                 adult_min_age_years:float=15,
                 atbirth:float=1.0,
                 birth_18months:float=1.0,
                 toddler_years04:float=1.0,
                 years05_years09:float=1.0,
                 years10_years14:float=1.0,
                 years15_years19:float=1.0,
                 years20_older:float=1.0
                 ):
        super().__init__(
            adult_min_age_years=adult_min_age_years,
            atbirth=atbirth,
            birth_18months=birth_18months,
            toddler_years04=toddler_years04,
            years05_years09=years05_years09,
            years10_years14=years10_years14,
            years15_years19=years15_years19,
            years20_older=years20_older
        )
        self.feature_params[IndividualSamplingKeys.max_node_pop_samples] = max_node_pop_samples
        pass
    pass


class IndividualSamplingImmuneStateFeatureConfiguration(IndividualSamplingFeatureConfiguration):
    def __init__(self,
                 relative_sample_rate_immune:float,
                 immune_threshold_downsampling:float,
                 base_sample_rate:float=1.0
                 ):
        super().__init__(sample_type=IndividualSamplingKeys.enum_options.adapt_immune_state)
        self.feature_params[IndividualSamplingKeys.immune_threshold] = immune_threshold_downsampling
        self.feature_params[IndividualSamplingKeys.immune_sample_rate] = relative_sample_rate_immune
        self.feature_params[IndividualSamplingKeys.base_sample_rate] = base_sample_rate
        pass
    pass

