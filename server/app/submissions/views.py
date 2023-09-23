from pgrit.auth import SessionAuthentication
from rest_framework import generics

from .models import Submission
from .serializers import SubmissionSerializer, SubmissionUpdateSerializer


class SubmissionListView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.prefetch_related("team", "problem", "status").all()


class SubmissionCreateView(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer


class SubmissionRetrieveView(generics.RetrieveAPIView):
    queryset = Submission.objects.prefetch_related("team", "problem", "status").all()
    serializer_class = SubmissionSerializer


class SubmissionUpdateView(generics.UpdateAPIView):
    queryset = Submission.objects.prefetch_related("team", "problem", "status").all()
    serializer_class = SubmissionUpdateSerializer


class SubmissionDeleteView(generics.DestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
