import time
from uuid import uuid4

import jwt
import requests
from decouple import config
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from users.models import User


class PGritAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.data.get("token")
        credential_url = config("PGRIT_AUTH_URL")
        if credential_url == "":
            raise ValueError("PGRIT_AUTH_URL is not set.")
        res = requests.get(credential_url, headers={"Authorization": f"Bearer {token}"}).json()
        if res.get("error") != None:
            raise PermissionError("token is not valid.")
        users = User.objects.filter(username=res.get("username"))
        if not users.exists():
            user = User.objects.create_user(username=res.get("username"), password=str(uuid4()))
        else:
            user = users.first()
        token = generate_jwt(user)
        return (user, token)

    def authenticate_header(self, request):
        pass


class SessionAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if token == "":
            raise exceptions.AuthenticationFailed("token is not set.")
        secret = config("DJANGO_SECERT_KEY", "")
        try:
            decoded = jwt.decode(token, secret, algorithms="HS256")
        except:
            raise exceptions.AuthenticationFailed("token is not valid.")
        print(decoded, flush=True)
        username = decoded.get("username")
        expired = decoded.get("exp")
        print(expired, int(time.time()), flush=True)
        if expired < int(time.time()):
            raise exceptions.AuthenticationFailed("time is expired")
        users = User.objects.filter(username=username)
        if users.exists():
            user = users.first()
        else:
            raise ValueError("user is not exist.")
        return (user, None)


def generate_jwt(user):
    timestamp = int(time.time()) + 60 * 60 * 24 * 7
    secret = config("DJANGO_SECERT_KEY", "")
    return jwt.encode({"username": user.username, "exp": timestamp}, secret)
