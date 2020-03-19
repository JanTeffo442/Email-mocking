import smtplib,unittest
from unittest import TestCase
from mock import MagicMock
from unittest.mock import Mock
from send_inspirational_message import main
import logging
m = MagicMock()

class Sending_email(unittest.TestCase):
    def setUp(self):
        self.emails = []
    def test_get_contacts(self,*args):
        for i in self.emails:
            self.assertTrue(i == main(),'Incorrect')
        s = 'Jan jan.teffo@umuzi.org'
        self.assertEqual(s.split(), ['Jan','jan.teffo@umuzi.org'])
        with self.assertRaises(TypeError):
            s.split(2)
            self.assertEqual(len(s.emails, 2))
            self.assertEqual(s.emails[0].From, 'jan.teffo@umuzi.org')
            self.assertEqual(s.emails[0].to, ['jan.teffo@gmail.com'])
            self.assertEqual(s.emails[0].msg, 'Inspirational Quote')
            self.assertEqual(m.get_contacts, '[mycontacts.py]') == False
    def tearDown(self):
        self.emails = None
if __name__ == '__main__':
    unittest.main()