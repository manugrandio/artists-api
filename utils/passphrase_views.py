from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .passphrase_serializers import PassphraseSerializer
from .passphrase import count_valid_passphrases


class BasicPassphrase(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PassphraseSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        count = count_valid_passphrases(serializer.validated_data["passphrases"])
        return Response({"count": count})


class AdvancedPassphrase(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PassphraseSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        count = count_valid_passphrases(
            serializer.validated_data["passphrases"], use_advanced=True
        )
        return Response({"count": count})
