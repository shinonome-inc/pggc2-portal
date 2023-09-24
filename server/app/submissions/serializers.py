from rest_framework import serializers

from teams.serializers import TeamSerializer

from .models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    team = serializers.StringRelatedField()
    problem = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        model = Submission
        fields = ("id", "team", "problem", "status", "score")


class SubmissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ("status", "score")
