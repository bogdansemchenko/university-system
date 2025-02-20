import unittest
import os
from university_storage import UniversityStorage
from models.university_structure import University, Department

class UniversityTestCase(unittest.TestCase):

    def setUp(self):
        self.university = University("МГУ")
        self.university.add_department("Факультет математики")
        self.filename = "test_university_state.pkl"

    def test_save_and_load(self):
        UniversityStorage.save(self.university, self.filename)
        loaded_university = UniversityStorage.load(self.filename)
        self.assertIsNotNone(loaded_university)
        self.assertEqual(loaded_university.name, self.university.name)
        self.assertEqual(len(loaded_university.departments), len(self.university.departments))
        self.assertEqual(loaded_university.departments[0], self.university.departments[0])

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)


