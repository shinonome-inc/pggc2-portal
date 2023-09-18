from rest_framework import generics

from .models import Submission
from .serializer import SubmissionUpdateSerializer


class SubmissionListView(generics.ListAPIView):
    queryset = Submission.objects.all()


class SubmissionCreateView(generics.CreateAPIView):
    queryset = Submission.objects.all()


class SubmissionRetrieveView(generics.RetrieveAPIView):
    queryset = Submission.objects.all()


class SubmissionUpdateView(generics.UpdateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionUpdateSerializer


class SubmissionDeleteView(generics.DestroyAPIView):
    queryset = Submission.objects.all()
