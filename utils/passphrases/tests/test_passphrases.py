from unittest import TestCase

from ..passphrases import (
    basic_passphrase_is_valid,
    advanced_passphrase_is_valid,
    count_valid_passphrases,
)


class TestBasicPassphrase(TestCase):
    def test_basic_passphrase_is_valid_ko(self):
        passphrase = "aa bb cc dd aa"

        is_valid = basic_passphrase_is_valid(passphrase)

        self.assertFalse(is_valid)

    def test_basic_passphrase_is_valid_ok(self):
        passphrase = "aa bb cc dd ee"

        is_valid = basic_passphrase_is_valid(passphrase)

        self.assertTrue(is_valid)

    def test_basic_passphrase_is_valid_empty_string(self):
        """
        Our basic policy doesn't state anything about empty passphrases for the moment
        """

        passphrase = ""

        is_valid = basic_passphrase_is_valid(passphrase)

        self.assertTrue(is_valid)

    def test_count_valid_basic_passphrases(self):
        passphrases = (
            "aa bb cc dd ee\n"  # Valid
            "aa bb cc dd aa\n"  # Invalid
            "aa bb cc dd aaa"  # Valid
        )

        count = count_valid_passphrases(passphrases)

        self.assertEqual(count, 2)

    def test_count_valid_basic_passphrases_2(self):
        passphrases = (
            "aa bb cc bb ee\n"  # Invalid
            "aa bb cc aa ee\n"  # Invalid
            "aaa bbb ccc ddd bbb"  # Invalid
        )

        count = count_valid_passphrases(passphrases)

        self.assertEqual(count, 0)

    def test_count_valid_basic_passphrases_empty_ones(self):
        """
        Our basic policy doesn't state anything about empty passphrases for the moment
        """
        passphrases = "\n\n"

        count = count_valid_passphrases(passphrases)

        self.assertEqual(count, 3)


class TestAdvancedPassphrase(TestCase):
    def test_advanced_passphrase_is_valid_ok(self):
        passphrase = "abcde fghij"

        is_valid = advanced_passphrase_is_valid(passphrase)

        self.assertTrue(is_valid)

    def test_advanced_passphrase_is_valid_ok_2(self):
        passphrase = "a ab abc abd abf abj"

        is_valid = advanced_passphrase_is_valid(passphrase)

        self.assertTrue(is_valid)

    def test_advanced_passphrase_is_valid_ok_3(self):
        passphrase = "iiii oiii ooii oooi oooo"

        is_valid = advanced_passphrase_is_valid(passphrase)

        self.assertTrue(is_valid)

    def test_advanced_passphrase_is_valid_ko(self):
        passphrase = "abcde xyz ecdab"

        is_valid = advanced_passphrase_is_valid(passphrase)

        self.assertFalse(is_valid)

    def test_count_valid_advanced_passphrases(self):
        passphrases = (
            "abcde fghij\n"  # Valid
            "abcde xyz ecdab\n"  # Invalid
            "a ab abc abd abf abj\n"  # Valid
            "iiii oiii ooii oooi oooo"  # Valid
        )

        count = count_valid_passphrases(passphrases, use_advanced=True)

        self.assertEqual(count, 3)
