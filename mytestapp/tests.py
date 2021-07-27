from django.test import TestCase

from mytestapp.models import ModelA, ModelB
from mytestapp.helpers import add_number


class TestModelA(TestCase):
    def setUp(self):
        ModelA.objects.using("default").create(name='Hello', name_two='Hello_there')

    def test_model_a(self):
        obj = ModelA.objects.first()
        self.assertEqual(obj.name, 'Hello')


class TestHelper(TestCase):
    def test_add_sum(self):
        test_cases = [
            (1, 2, 3),
            (100, 200, 300),
            (1.4, 2.2, 3.6)
        ]
        for a, b, sum in test_cases:
            result = add_number(a, b)
            self.assertEqual(result, sum)
