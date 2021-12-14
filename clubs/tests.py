from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(
            '@ali',
            first_name='ali',
            last_name='tan',
            password='Password123',
            bio='Hello',
            personalstatement='Chess player',
            experiencelevel='Amateur',
            email='ali@gmail.com'
        )

    def test_valid_user(self):
        self._assert_valid()

    def _assert_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def _assert_valid(self):
            try:
                self.user.full_clean()
            except (ValidationError):
                self.fail('Make user valid')

    def test_username_blank(self):
        self.user.username=''
        self._assert_invalid()

    def test_username_atstart(self):
        self.user.username='ali'
        self._assert_invalid()

    def test_username_under_30_chars(self):
        self.user.username='@ '+ 'x' * 30
        self._assert_invalid()

    def test_username_can_be_30_chars(self):
        self.user.username='@ '+ 'x' * 29
        self._assert_invalid()

    def test_username_has_alphanumericals_onlyafterat(self):
        self.user.username='@al!i'
        self._assert_invalid()

    def test_username_contains_atleast_3_chars(self):
        self.user.username='@al'
        self._assert_invalid()

    def test_username_may_have_numbers(self):
        self.user.username='@ali2'
        self._assert_valid()

    def test_username_has_one_at(self):
        self.user.username='@@ali'
        self._assert_invalid()

    def test_username_unique(self):
        User.objects.create_user(
            '@aleem',
            first_name='aleem',
            last_name='tan',
            password='Password123',
            bio='Hello i am aleem',
            personalstatement='Chess player extraordinary',
            experiencelevel='Pro',
            email='aleem@gmail.com'
        )
        self.user.username='@aleem'
        self._assert_invalid()

    def test_firstname_must_not_be_blank(self):
        self.user.first_name=''
        self._assert_invalid()

    def test_firstname_must_not_be_morethen_50chars(self):
        self.user.first_name='x'*51
        self._assert_invalid()

    def test_firstname_can_be_50chars(self):
        self.user.first_name='x'*50
        self._assert_valid()

    def test_lastname_must_not_be_blank(self):
        self.user.last_name=''
        self._assert_invalid()

    def test_lastname_must_not_be_morethen_50chars(self):
        self.user.last_name='x'*51
        self._assert_invalid()

    def test_lastname_can_be_50chars(self):
        self.user.last_name='x'*50
        self._assert_valid()

    def _create_second_user(self):
        user= User.objects.create_user(
            '@aleem',
            first_name='aleem',
            last_name='tan',
            password='Password123',
            bio='Hello i am aleem',
            personalstatement='Chess player extraordinary',
            experiencelevel='Pro',
            email='aleem@gmail.com'
        )
        return user

    def test_firstname_may_not_be_unique(self):
        second_user=self._create_second_user()
        self.user.first_name=second_user.first_name
        self._assert_valid()

    def test_lastname_may_not_be_unique(self):
        second_user=self._create_second_user()
        self.user.last_name=second_user.last_name
        self._assert_valid()

    def test_email_must_not_be_blank(self):
        self.user.email=''
        self._assert_invalid()

    def test_email_has_one_at(self):
        self.user.email='ali.example.org'
        self._assert_invalid()

    def test_email_has_username(self):
        self.user.email='@example.org'
        self._assert_invalid()

    def test_email_has_domain_name(self):
        self.user.email='ali@.org'
        self._assert_invalid()

    def test_email_has_domain(self):
        self.user.email='ali@example'
        self._assert_invalid()

    def test_email_does_not_have_more_then_one_at(self):
        self.user.email='ali@example@.org'
        self._assert_invalid()

    def test_email_must_be_unique(self):
        second_user=self._create_second_user()
        self.user.email=second_user.email
        self._assert_invalid()

    def test_bio_must_not_be_morethen_520chars(self):
        self.user.bio='x'*521
        self._assert_invalid()

    def test_bio_can_be_520chars(self):
        self.user.bio = 'x'*520
        self._assert_valid()

    def test_bio_may_not_be_unique(self):
        second_user=self._create_second_user()
        self.user.bio=second_user.bio
        self._assert_valid()

    def test_experiencelevel_cannot_be_blank(self):
        self.user.experiencelevel=''
        self._assert_invalid()

    def test_experiencelevel_must_not_be_morethen_50chars(self):
        self.user.experiencelevel='x'*51
        self._assert_invalid()

    def test_experiencelevel_can_be_50chars(self):
        self.user.experiencelevel = 'x'*50
        self._assert_valid()

    def test_experiencelevel_may_not_be_unique(self):
        second_user=self._create_second_user()
        self.user.experiencelevel=second_user.experiencelevel
        self._assert_valid()

    def test_bio_may_be_blank(self):
        self.user.bio=''
        self._assert_valid()

    def test_personalstatement_may_be_blank(self):
        self.user.personalstatement=''
        self._assert_valid()

    def test_personalstatement_must_not_be_morethen_520chars(self):
        self.user.personalstatement='x'*521
        self._assert_invalid()

    def test_personalstatement_can_be_520chars(self):
        self.user.personalstatement = 'x'*520
        self._assert_valid()

    def test_personalstatement_may_not_be_unique(self):
        second_user=self._create_second_user()
        self.user.personalstatement=second_user.personalstatement
        self._assert_valid()
