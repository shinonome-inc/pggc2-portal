from rest_framework.response import Response
from rest_framework.views import APIView

from .auth import PGritAuthentication


class LoginView(APIView):
    authentication_classes = [PGritAuthentication]

    def post(self, request, *args, **kwargs):
        return Response({"token": str(request.auth)})
