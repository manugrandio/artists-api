from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .passphrase import count_valid_basic_passphrases


class BasicPassphrase(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        count = count_valid_basic_passphrases(self.request.data["passphrases"])
        return Response({"count": count})