from rest_framework import generics

from .models import Clarification
from .serializer import ClarificationUpdateSerializer


class ClarificationListView(generics.ListAPIView):
    queryset = Clarification.objects.all()


class ClarificationCreateView(generics.CreateAPIView):
    queryset = Clarification.objects.all()


class ClarificationRetrieveView(generics.RetrieveAPIView):
    queryset = Clarification.objects.all()


class ClarificationUpdateView(generics.UpdateAPIView):
    queryset = Clarification.objects.all()
    serializer_class = ClarificationUpdateSerializer


class ClarificationDeleteView(generics.DestroyAPIView):
    queryset = Clarification.objects.all()
