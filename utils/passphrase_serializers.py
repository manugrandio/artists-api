from rest_framework.serializers import Serializer, CharField


class PassphraseSerializer(Serializer):
    passphrases = CharField(allow_blank=False)
