from pgrit.auth import SessionAuthentication, AdminAuthentication
from users.models import User
from teams.models import Team
from rest_framework import generics

from django.db.models import Q

from .models import Clarification
from .serializers import ClarificationUpdateSerializer


class ClarificationListView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        user = User.objects.get(username=self.request.user.username)
        return Clarification.objects.filter(Q(team=user.team) | Q(is_public=True))


class AdminClarificationListView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, AdminAuthentication]
    queryset = Clarification.objects.all()


class ClarificationCreateView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication]
    queryset = Clarification.objects.all()


class ClarificationRetrieveView(generics.RetrieveAPIView):
    authentication_classes = [SessionAuthentication, AdminAuthentication]
    queryset = Clarification.objects.prefetch_related("team", "problem").all()


class ClarificationUpdateView(generics.UpdateAPIView):
    authentication_classes = [SessionAuthentication, AdminAuthentication]
    queryset = Clarification.objects.prefetch_related("team", "problem").all()
    serializer_class = ClarificationUpdateSerializer


class ClarificationDeleteView(generics.DestroyAPIView):
    authentication_classes = [SessionAuthentication, AdminAuthentication]
    queryset = Clarification.objects.all()
