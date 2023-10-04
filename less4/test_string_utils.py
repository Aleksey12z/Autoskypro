import unittest
from string_utils import StringUtils

class StringUtilsTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.str_utils = StringUtils()

    def test_capitalize(self):
        self.assertEqual(self.str_utils.capitilize("skypro"), "Skypro")
        self.assertEqual(self.str_utils.capitilize("SKYPRO"), "Skypro") 
        self.assertEqual(self.str_utils.capitilize(""), "")

    def test_trim(self):
        self.assertEqual(self.str_utils.trim("   skypro"), "skypro")
        self.assertEqual(self.str_utils.trim("skypro   "), "skypro   ")
        self.assertEqual(self.str_utils.trim(""), "")

    def test_to_list(self):
        self.assertEqual(self.str_utils.to_list("a,b,c,d"), ["a", "b", "c", "d"])
        self.assertEqual(self.str_utils.to_list("1:2:3", ":"), ["1", "2", "3"])
        self.assertEqual(self.str_utils.to_list("", ":"), [])

    def test_contains(self):
        self.assertTrue(self.str_utils.contains("SkyPro", "S"))
        self.assertFalse(self.str_utils.contains("SkyPro", "U"))
        self.assertFalse(self.str_utils.contains("", "S"))

    def test_delete_symbol(self):
        self.assertEqual(self.str_utils.delete_symbol("SkyPro", "k"), "SyPro")
        self.assertEqual(self.str_utils.delete_symbol("SkyPro", "Pro"), "Sky")
        self.assertEqual(self.str_utils.delete_symbol("SkyPro", "U"), "SkyPro")
        
    def test_starts_with(self):
        self.assertTrue(self.str_utils.starts_with("SkyPro", "S"))
        self.assertFalse(self.str_utils.starts_with("SkyPro", "P"))
        self.assertFalse(self.str_utils.starts_with("", "S"))

    def test_end_with(self):
        self.assertTrue(self.str_utils.end_with("SkyPro", "o"))
        self.assertFalse(self.str_utils.end_with("SkyPro", "y"))
        self.assertFalse(self.str_utils.end_with("", "S"))

    def test_is_empty(self):
        self.assertTrue(self.str_utils.is_empty(""))
        self.assertTrue(self.str_utils.is_empty(" "))
        self.assertFalse(self.str_utils.is_empty("SkyPro"))

    def test_list_to_string(self):
        self.assertEqual(self.str_utils.list_to_string([1,2,3,4]), "1, 2, 3, 4")
        self.assertEqual(self.str_utils.list_to_string(["Sky", "Pro"]), "Sky, Pro")
        self.assertEqual(self.str_utils.list_to_string(["Sky", "Pro"], "-"), "Sky-Pro")
        self.assertEqual(self.str_utils.list_to_string([], "-"), "")

if __name__ == '__main__':
    unittest.main()
