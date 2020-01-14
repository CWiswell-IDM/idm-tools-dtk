import unittest
__unittest = True

from test_idm_tools_dtk import IdmToolsDtkTest

from birth_feature_configuration import BirthKeys, \
    BirthRateTimeDependenceKeys, \
    BirthFeatureConfiguration, \
    BirthRateSinusoidalTimeDependenceFeatureConfiguration, \
    BirthRateBoxcarTimeDependenceFeatureConfiguration, \
    BirthRateNoTimeDependenceFeatureConfiguration, \
    BirthRateDependenceFeatureConfiguration, BirthRateDependenceKeys
from death_feature_configuration import DeathKeys, \
    DeathFeatureConfiguration, \
    DeathRateDependenceKeys, \
    DeathAgeAndGenderFeatureConfiguration, \
    DeathYearAgeGenderFeatureConfiguration


class VitalDynamicsFeatureTest(IdmToolsDtkTest):

    # region BirthRateTimeDependence

    def test_birthrate_timedependence_none(self):
        t_d = BirthRateNoTimeDependenceFeatureConfiguration()
        self.config_params = t_d.get_config_params()
        self.assertIn(BirthRateTimeDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateTimeDependenceKeys.type_enum]
        self.assertEqual("NONE", config_value)
        missing_keys = [
            BirthRateTimeDependenceKeys.boxcar_end,
            BirthRateTimeDependenceKeys.boxcar_start,
            BirthRateTimeDependenceKeys.boxcar_amplitude,
            BirthRateTimeDependenceKeys.sinusoid_amplitude,
            BirthRateTimeDependenceKeys.sinusiod_phase
        ]
        for k in missing_keys:
            self.assertNotIn(k, self.config_params)
            pass
        pass

    def test_birthrate_timedependence_sinusoid(self):
        expected_phase = 90.1
        expected_amplitude = 12.3
        t_d = BirthRateSinusoidalTimeDependenceFeatureConfiguration(
            amplitude=expected_amplitude,
            phase=expected_phase
        )
        self.config_params = t_d.get_config_params()
        self.assertIn(BirthRateTimeDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateTimeDependenceKeys.type_enum]
        self.assertEqual(BirthRateTimeDependenceKeys.enum_options.sinusoid, config_value)
        self.assertEqual(expected_phase, self.config_params[BirthRateTimeDependenceKeys.sinusiod_phase])
        self.assertEqual(expected_amplitude, self.config_params[BirthRateTimeDependenceKeys.sinusoid_amplitude])
        missing_keys = [
            BirthRateTimeDependenceKeys.boxcar_end,
            BirthRateTimeDependenceKeys.boxcar_start,
            BirthRateTimeDependenceKeys.boxcar_amplitude
        ]
        for k in missing_keys:
            self.assertNotIn(k, self.config_params)
            pass
        pass

    def test_birthrate_timedependence_boxcar(self):
        expected_amplitude = 1.23
        expected_start = 90
        expected_end = 180
        t_d = BirthRateBoxcarTimeDependenceFeatureConfiguration(
            amplitude=expected_amplitude,
            start_time=expected_start,
            end_time=expected_end
        )
        self.config_params = t_d.get_config_params()
        self.assertIn(BirthRateTimeDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateTimeDependenceKeys.type_enum]
        self.assertEqual(BirthRateTimeDependenceKeys.enum_options.boxcar, config_value)
        self.assertEqual(expected_amplitude, self.config_params[BirthRateTimeDependenceKeys.boxcar_amplitude])
        self.assertEqual(expected_start, self.config_params[BirthRateTimeDependenceKeys.boxcar_start])
        self.assertEqual(expected_end, self.config_params[BirthRateTimeDependenceKeys.boxcar_end])
        missing_keys = [
            BirthRateTimeDependenceKeys.sinusoid_amplitude,
            BirthRateTimeDependenceKeys.sinusiod_phase
        ]
        for k in missing_keys:
            self.assertNotIn(k, self.config_params)
            pass
        pass

    # endregion

    # region BirthRateDependence

    def test_brd_fixed(self):
        brd = BirthRateDependenceFeatureConfiguration(enum_setting=BirthRateDependenceKeys.enum_options.fixed)
        self.config_params = brd.get_config_params()
        self.assertIn(BirthRateDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateDependenceKeys.type_enum]
        self.assertEqual(BirthRateDependenceKeys.enum_options.fixed, config_value)
        pass

    def test_brd_population_dependent(self):
        brd = BirthRateDependenceFeatureConfiguration(enum_setting=BirthRateDependenceKeys.enum_options.pop_dependent)
        self.config_params = brd.get_config_params()
        self.assertIn(BirthRateDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateDependenceKeys.type_enum]
        self.assertEqual(BirthRateDependenceKeys.enum_options.pop_dependent, config_value)
        pass

    def test_brd_demographic_dependent(self):
        brd = BirthRateDependenceFeatureConfiguration(enum_setting=BirthRateDependenceKeys.enum_options.demo_depdendent)
        self.config_params = brd.get_config_params()
        self.assertIn(BirthRateDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateDependenceKeys.type_enum]
        self.assertEqual(BirthRateDependenceKeys.enum_options.demo_depdendent, config_value)
        pass

    def test_brd_individual_pregancies(self):
        brd = BirthRateDependenceFeatureConfiguration(enum_setting=BirthRateDependenceKeys.enum_options.ind_pregnancies)
        self.config_params = brd.get_config_params()
        self.assertIn(BirthRateDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateDependenceKeys.type_enum]
        self.assertEqual(BirthRateDependenceKeys.enum_options.ind_pregnancies, config_value)
        pass

    def test_brd_indidividual_pregancies_age_year(self):
        brd = BirthRateDependenceFeatureConfiguration(
            enum_setting=BirthRateDependenceKeys.enum_options.ind_pregnancies_age_and_year)
        self.config_params = brd.get_config_params()
        self.assertIn(BirthRateDependenceKeys.type_enum, self.config_params)
        config_value = self.config_params[BirthRateDependenceKeys.type_enum]
        self.assertEqual(BirthRateDependenceKeys.enum_options.ind_pregnancies_age_and_year, config_value)
        pass

    # endregion

    # region MaternalTransmission

    def test_maternal_transmission_enabled_default(self):
        test_probability = 0.0
        bc = BirthFeatureConfiguration(
            enable=True,
            maternal_transmission=True
        )
        self.config_params = bc.get_config_params()
        self.assertTrue(self.config_params[BirthKeys.maternal_transmission])
        self.assertTrue(self.config_params[BirthKeys.enable])
        self.assertIn(
            BirthKeys.maternal_transmission_probability,
            self.config_params
        )
        found_probability = self.config_params[BirthKeys.maternal_transmission_probability]
        self.assertEqual(test_probability, found_probability)
        pass

    def test_maternal_transmission_enabled_custom(self):
        test_probability = 0.3
        bc = BirthFeatureConfiguration(
            enable=True,
            maternal_transmission=True,
            maternal_transmission_probability=test_probability
        )
        self.config_params = bc.get_config_params()
        self.assertTrue(self.config_params[BirthKeys.maternal_transmission])
        self.assertIn(
            BirthKeys.maternal_transmission_probability,
            self.config_params
        )
        found_probability = self.config_params[BirthKeys.maternal_transmission_probability]
        self.assertEqual(test_probability, found_probability)
        pass

    # endregion

    # region Birth

    def test_birth_disabled(self):
        bf = BirthFeatureConfiguration(
            enable=False
        )
        self.config_params = bf.get_config_params()
        self.assertFalse(
            self.config_params[BirthKeys.enable]
        )
        self.assertEqual(
            len(self.config_params),
            1
        )
        pass

    def test_birth_defaults(self):
        expected_multiplier = 1.0
        expected_demographics_birth = False
        expected_maternal_transmission = False
        expected_time_dependence = BirthRateTimeDependenceKeys.enum_options.none
        bf = BirthFeatureConfiguration(
            enable=True
        )
        self.config_params = bf.get_config_params()
        self.assertEqual(
            len(self.config_params),
            5 # enable, multiplier, time dependence, demographics, maternal txn
        )
        self.assertIn(
            BirthKeys.x_birth,
            self.config_params
        )
        observed_multiplier = self.config_params[BirthKeys.x_birth]
        self.assertEqual(
            expected_multiplier,
            observed_multiplier
        )
        self.assertEqual(
            expected_demographics_birth,
            self.config_params[BirthKeys.demographics_birth]
        )
        self.assertEqual(
            expected_maternal_transmission,
            self.config_params[BirthKeys.maternal_transmission]
        )
        self.assertEqual(
            expected_time_dependence,
            self.config_params[BirthKeys.time_dependence]
        )
        self.assertNotIn(
            BirthKeys.maternal_transmission_probability,
            self.config_params
        )
        pass

    def test_birth_multiplier_custom(self):
        test_multiplier = 1.3
        bf = BirthFeatureConfiguration(
            enable=True,
            x_birth=test_multiplier
        )
        self.config_params = bf.get_config_params()
        self.assertIn(
            BirthKeys.x_birth,
            self.config_params
        )
        observed_multiplier = self.config_params[BirthKeys.x_birth]
        self.assertEqual(
            test_multiplier,
            observed_multiplier
        )
        pass

    def test_demographics_birth(self):
        bf = BirthFeatureConfiguration(
            enable=True,
            demographics_birth=True
        )
        self.config_params = bf.get_config_params()
        self.assertEqual(
            len(self.config_params),
            5 # enable, multiplier, time dependence, demographics, maternal txn
        )
        self.assertIn(
            BirthKeys.demographics_birth,
            self.config_params
        )
        self.assertTrue(
            self.config_params[BirthKeys.demographics_birth]
        )
        # Not sure what this even does
        # schema "Controls whether or not newborns have identical or heterogeneous characteristics."
        pass

    # endregion

    # region NaturalMortality(death)

    def test_disable_death(self):
        df = DeathFeatureConfiguration(enable=False)
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            1
        )
        self.assertFalse(
            self.config_params[DeathKeys.enable]
        )
        pass

    def test_enable_death(self):
        expected_multiplier = 1.0
        df = DeathFeatureConfiguration(enable=True)
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertTrue(
            self.config_params[DeathKeys.enable]
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.none
        )
        pass

    def test_enable_death_multiplier(self):
        expected_multiplier = 1.5
        df = DeathFeatureConfiguration(enable=True,
                                       x_death=expected_multiplier)
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.none
        )
        pass

    def test_disable_death_multiplier(self):
        expected_multiplier = 1.5
        df = DeathFeatureConfiguration(enable=False,
                                       x_death=expected_multiplier)
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            1
        )
        self.assertFalse(
            self.config_params[DeathKeys.enable]
        )
        pass

    def test_enable_death_age_gender(self):
        expected_multiplier = 1.0
        expected_demo_params = {
            'some_ages': [10, 100, 1000],
            'some_genders': {
                'male': [0.2, 0.7, 0.9],
                'female': [0.3, 0.4, 0.7]
            }
        }
        df = DeathAgeAndGenderFeatureConfiguration(
            demographics_params=expected_demo_params
        )
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertTrue(
            self.config_params[DeathKeys.enable]
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.age_and_gender
        )
        found_demo_params = df.demographics_params
        self.assertEqual(
            expected_demo_params,
            found_demo_params
        )
        pass

    def test_enable_death_age_gender_multiplier(self):
        expected_multiplier = 0.9
        df = DeathAgeAndGenderFeatureConfiguration(
            x_death=expected_multiplier
        )
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertTrue(
            self.config_params[DeathKeys.enable]
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.age_and_gender
        )
        pass

    def test_enable_death_year_age_gender(self):
        expected_multiplier = 1.0
        expected_demo_params = {
            'some_ages': [10, 100, 1000],
            'some_genders': {
                'male': [0.2, 0.7, 0.9],
                'female': [0.3, 0.4, 0.7]
            },
            'some_years': [1975, 1999, 2020]
        }
        df = DeathYearAgeGenderFeatureConfiguration(
            demographics_params=expected_demo_params
        )
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertTrue(
            self.config_params[DeathKeys.enable]
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.year_age_gender
        )
        found_demo_params = df.demographics_params
        self.assertEqual(
            expected_demo_params,
            found_demo_params
        )
        pass

    def test_enable_death_year_age_gender_multiplier(self):
        expected_multiplier = 0.9
        df = DeathYearAgeGenderFeatureConfiguration(
            x_death=expected_multiplier
        )
        self.config_params = df.get_config_params()
        self.assertEqual(
            len(self.config_params),
            3
        )
        self.assertTrue(
            self.config_params[DeathKeys.enable]
        )
        self.assertEqual(
            self.config_params[DeathKeys.x_death],
            expected_multiplier
        )
        self.assertEqual(
            self.config_params[DeathKeys.dependence],
            DeathRateDependenceKeys.enum_options.year_age_gender
        )
        pass

    # endregion

    # region death default multiplier

    # endregion
