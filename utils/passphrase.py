def basic_passphrase_is_valid(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))


def count_valid_basic_passphrases(passphrases):
    passphrases_list = passphrases.split("\n")
    return len(
        [
            passphrase
            for passphrase in passphrases_list
            if basic_passphrase_is_valid(passphrase)
        ]
    )
