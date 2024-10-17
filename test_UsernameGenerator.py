# Username Generator V.0.1

from datetime import datetime
current_year = datetime.now().year
from io import StringIO
import sys
import unittest
from unittest.mock import patch

from UsernameGenerator import create_user_name, user_campus, user_details

class username_generator_test(unittest.TestCase):
    @patch("sys.stdin", StringIO(f"Chand3er\nChandler\nJacobs\n{current_year}\nDurban"))
    def test_invalid_name(self):
        """
            Testing invalid prompt for first name
        """
        output = StringIO()
        sys.stdout = output

        user_details()
        self.assertEqual(output.getvalue(), f"""Insert your first name
Invalid first name
Insert your first name
Insert your last name
Insert your cohort
Insert the campus you will be attending in
lerjac{current_year}DBN\n""")


    @patch("sys.stdin", StringIO(f"Lekau\nMamabo3o\nMamabolo\n{current_year}\nCape Town"))
    def test_invalid_surname(self):
        """
            Testing invalid prompt for last name
        """
        output = StringIO()
        sys.stdout = output

        user_details()
        self.assertEqual(output.getvalue(), f"""Insert your first name
Insert your last name
Invalid last name
Insert your last name
Insert your cohort
Insert the campus you will be attending in
kaumam{current_year}CPT\n""")


    @patch("sys.stdin", StringIO(f"Joshua\nOverton\n2020\n2021\n{current_year}\nPhokeng"))
    def test_invalid_cohort(self):
        """
            Testing invalid prompt for cohort
        """
        output = StringIO()
        sys.stdout = output

        user_details()
        self.assertEqual(output.getvalue(), f"""Insert your first name
Insert your last name
Insert your cohort
Invalid cohort
Insert your cohort
Invalid cohort
Insert your cohort
Insert the campus you will be attending in
huaove{current_year}PHO\n""")


    @patch("sys.stdin", StringIO(f"Sandiselwe\nZwane\n{current_year}\nPretoria\nJohannesburg"))
    def test_invalid_campus(self):
        """
            Testing invalid prompt for campus
        """
        output = StringIO()
        sys.stdout = output

        user_details()
        self.assertEqual(output.getvalue(), f"""Insert your first name
Insert your last name
Insert your cohort
Insert the campus you will be attending in
Invalid campus
Insert the campus you will be attending in
lwezwa{current_year}JHB\n""")


    @patch("sys.stdin", StringIO(f"\nThandeka\nMngomezulu\n{current_year}\nPhokeng"))
    def test_empty_first_name(self):
        """
            Testing empty first name
        """
        output = StringIO()
        sys.stdout = output

        user_details()
        self.assertEqual(output.getvalue(), f"""Insert your first name
Invalid first name
Insert your first name
Insert your last name
Insert your cohort
Insert the campus you will be attending in
ekamng{current_year}PHO\n""")


    def test_name_extractions(self):
        """
            Testing if the first three letters of the username 
            are the last three letters of the first name and if the first
            three letters of the last name are extracted
        """
        username = create_user_name("Zenani", "Zwane", "2020", "Durban")
        self.assertEqual(username[:3], "ani")
        self.assertEqual(username[3:6], "zwa")

    def test_user_details_first_name_longer_than_3_letters(self):
        """
            Testing extraction of first name longer than three letters
        """
        username = create_user_name("Abdur-Raheem", "Lee", "2022", "Cape Town")
        self.assertEqual(username[:3], "eem")


    def test_user_details_first_name_shorter_than_3_letters(self):
        """
            Testing generation of first name shorter than three letters
        """
        username = create_user_name("Ab", "Lee", "2022", "Cape Town")
        self.assertEqual(username[:3], "abo")

    
    def test_user_details_first_name_shorter_than_3_letters_2(self):
        """
            Testing generation of first name shorter than three letters
        """
        username = create_user_name("A", "Lee", "2022", "Cape Town")
        self.assertEqual(username[:3], "aoo")


    def test_user_details_last_name_longer_than_3_letters(self):
        """
            Testing extraction of last name longer than three letters
        """
        username = create_user_name("Abdur-Raheem", "Lee", "2022", "Cape Town")
        self.assertEqual(username[3:6], "lee")


    def test_user_details_last_name_shorter_than_3_letters(self):
        """
            Testing generation of last name shorter than three letters
        """
        username = create_user_name("Abdur-Raheem", "Le", "2022", "Cape Town")
        self.assertEqual(username[3:6], "leo")


    def test_user_details_last_name_shorter_than_3_letters_2(self):
        """
            Testing generation of last name shorter than three letters
        """
        username = create_user_name("Abdur-Raheem", "L", "2022", "Cape Town")
        self.assertEqual(username[3:6], "loo")


    def test_user_campus(self):
        """
            Testing campus abbreviation translations
        """
        self.assertEqual(user_campus("johannesburg"), "JHB")
        self.assertEqual(user_campus("cape town"), "CPT")
        self.assertEqual(user_campus("durban"), "DBN")
        self.assertEqual(user_campus("phokeng"), "PHO")


    @patch("sys.stdin", StringIO(f"Corban\nLoots\n{current_year}\nDurban"))
    def test_username(self):
        """
            Testing long way if correct username is generated
        """
        output = StringIO()
        sys.stdout = output

        user_details()
        self.assertEqual(output.getvalue(), f"""Insert your first name
Insert your last name
Insert your cohort
Insert the campus you will be attending in
banloo{current_year}DBN\n""")

if __name__ == '__main__':
    unittest.main()
