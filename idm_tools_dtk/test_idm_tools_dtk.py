import unittest
__unittest = True

test_debug = False

class IdmToolsDtkTest(unittest.TestCase):
    def setUp(self):
        self.config_params = None
        pass

    def tearDown(self):
        if test_debug:
            print()
            print(self.id())
            print(self.config_params)
            print()
        pass

