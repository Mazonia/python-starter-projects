import unittest
from starter_suite import (
    caesar_cipher, change_email_domain, calculate_subnets,
    generate_password, pig_latin_translate, is_palindrome,
    is_leap_year, calculate_grade, count_frequency,
    count_digits, elevator_simulate, team_matchup
)

class StarterProjectsTests(unittest.TestCase):
    def test_caesar_cipher(self):
        encoded = caesar_cipher("Hello World!", 3, 'encode')
        self.assertEqual(encoded, "Khoor Zruog!")
        decoded = caesar_cipher(encoded, 3, 'decode')
        self.assertEqual(decoded, "Hello World!")

    def test_change_email_domain(self):
        updated = change_email_domain("user@oldcompany.com", "oldcompany.com", "newcompany.com")
        self.assertEqual(updated, "user@newcompany.com")
        unchanged = change_email_domain("user@gmail.com", "oldcompany.com", "newcompany.com")
        self.assertEqual(unchanged, "user@gmail.com")

    def test_calculate_subnets(self):
        res = calculate_subnets("192.168.1.0/24", [50, 20])
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0]["required_hosts"], 50)

    def test_generate_password(self):
        pwd = generate_password(16)
        self.assertEqual(len(pwd), 16)

    def test_pig_latin(self):
        self.assertEqual(pig_latin_translate("apple"), "appleway")
        self.assertEqual(pig_latin_translate("hello"), "ellohay")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("Python"))

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2024))
        self.assertFalse(is_leap_year(2023))
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900))

    def test_calculate_grade(self):
        self.assertEqual(calculate_grade(85), "A")
        self.assertEqual(calculate_grade(55), "D")
        self.assertEqual(calculate_grade(40), "F")

    def test_frequency_count(self):
        freq = count_frequency(["apple", "banana", "apple", "cherry"])
        self.assertEqual(freq["apple"], 2)
        self.assertEqual(freq["banana"], 1)

    def test_digit_counter(self):
        self.assertEqual(count_digits(12345), 5)
        self.assertEqual(count_digits(-9876), 4)

    def test_elevator(self):
        log = elevator_simulate(1, [4, 2])
        self.assertEqual(len(log), 2)
        self.assertIn("Ascending", log[0])
        self.assertIn("Descending", log[1])

if __name__ == '__main__':
    unittest.main()
