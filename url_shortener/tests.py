from django.test import TestCase
from url_shortener.models import Url

class UrlTestCase(TestCase):

    def setUp(self):
        self.google = Url.objects.create(url_original="https://www.google.com.br/")

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_google_ecziste(self):
        self.assertTrue(self.google)

    def test_numero_clicks(self):
        self.assertEqual(self.google.numero_clicks, 0)
        