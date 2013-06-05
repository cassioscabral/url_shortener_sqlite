# -*- coding: utf-8 -*-
from django.test import TestCase
from url_shortener.models import Url

class UrlTestCase(TestCase):

    def setUp(self):
        self.google = Url.objects.create(url_original="https://www.google.com.br/")

    def test_google_ecziste(self):
        self.assertTrue(self.google)

    def test_numero_clicks(self):
        self.assertEqual(self.google.numero_clicks, 0)

    def test_url_modificada_nao_vazia(self):
        self.assertIsNot(len(self.google.url_modificada), 0, "A url modificada é vazia")
 
    def test_url_modificada_menor_que_original(self):
        self.assertLess(len(self.google.url_modificada), len(self.google.url_original), "Url modificada não é menor que a original ")

        