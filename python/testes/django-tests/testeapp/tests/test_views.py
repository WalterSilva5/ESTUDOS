from django.http import response
from django.test import TestCase
from django.urls import reverse

class PessoaViewTestCase(TestCase):
    def test_status_code_200(self):
        """
            testa se o status code padrão da página é 200
        """
        response = self.client.get(reverse('pessoa'))
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'pessoa.html')
    def test_template(self):
        """
            testa se o template está sendo utilizado
        """
        response = self.client.get(reverse('pessoa'))
        self.assertTemplateUsed(response, 'pessoa.html')