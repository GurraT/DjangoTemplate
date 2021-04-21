from django.test import TestCase
from .models import Items


class TestModel(TestCase):

    def test_done_default_to_false(self):
        item = Items.objects.create(name='Test todo Item')
        self.assertFalse(item.done)

    def test_item_str_methods_retun_name(self):
        item = Items.objects.create(name='Test todo Item')
        self.assertEqual(str(item),'Test todo Item')