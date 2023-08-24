from django.test import TestCase
from django.contrib.auth.models import User


class TestBasicPassphrase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("john", "john@mail.com", "password")

    def test_basic_passphrase(self):
        self.client.login(username="john", password="password")

        passphrases = "aa bb cc\naa bb aa\naa bb dd"

        response = self.client.post("/passphrase/basic/", {"passphrases": passphrases})

        self.assertEqual(response.json()["count"], 2)


class TestAdvancedPassphrase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("john", "john@mail.com", "password")

    def test_advanced_passphrase(self):
        self.client.login(username="john", password="password")

        passphrases = (
            "abcde fghij\n"  # Valid
            "abcde xyz ecdab\n"  # Invalid
            "a ab abc abd abf abj\n"  # Valid
            "iiii oiii ooii oooi oooo"  # Valid
        )

        response = self.client.post(
            "/passphrase/advanced/", {"passphrases": passphrases}
        )

        self.assertEqual(response.json()["count"], 3)
