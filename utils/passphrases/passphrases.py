from collections import Counter


def basic_passphrase_is_valid(passphrase):
    """
    A passphrase is valid if it doesn't contain duplicate words.
    """
    words = passphrase.split()
    return len(words) == len(set(words))


def advanced_passphrase_is_valid(passphrase):
    """
    A passphrase is valid if it doesn't contain two words that are anagrams of each other.

    A word is an anagram of another if their counters are the same.
    """
    counters = [Counter(word) for word in passphrase.split()]
    for i, word_counter in enumerate(counters, 1):
        for j in range(i, len(counters)):
            if word_counter == counters[j]:
                return False

    return True


def count_valid_passphrases(passphrases, use_advanced=False):
    is_valid = (
        advanced_passphrase_is_valid if use_advanced else basic_passphrase_is_valid
    )
    passphrases_list = passphrases.split("\n")
    return len([passphrase for passphrase in passphrases_list if is_valid(passphrase)])
