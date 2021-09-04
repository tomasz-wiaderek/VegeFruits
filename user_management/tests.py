from django.test import TestCase

from .models import UserType

# Create your tests here.


class UserTypeModelTest(TestCase):

    def setUp(self) -> None:
        UserType.objects.create(type='admin')
        UserType.objects.create(type='producer')
        UserType.objects.create(type='customer')

    def test_if_type_can_be_empty_str(self):
        user = UserType.objects.get(type='admin')
        self.assertEqual(user.type, 'admin')
