import json
from teams.models import Team
from problems.models import Problem
from pgrit.auth import SessionAuthentication
from rest_framework import generics
from rest_framework.response import Response

from .models import Submission, Status
from .serializers import SubmissionSerializer, SubmissionUpdateSerializer


class SubmissionListView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication]
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.prefetch_related("team", "problem", "status").all()


class SubmissionCreateView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        Submission.objects.create(
            team=Team.objects.get(pk=data.get("team")),
            problem=Problem.objects.get(pk=data.get("problem")),
            status=Status.objects.get(pk=data.get("status"))
        )
        return Response({"message":"created"})


class SubmissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [SessionAuthentication]
    queryset = Submission.objects.prefetch_related("team", "problem", "status").all()
    serializer_class = SubmissionSerializer
