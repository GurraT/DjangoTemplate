from django.test import TestCase
from .forms import Itemsform


class TestItemsform(TestCase):

    def test_item_name_is_required(self):
        form = Itemsform({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = Itemsform({'name', 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_field_is_explicit_in_metaclass(self):
        form = Itemsform()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
