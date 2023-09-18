from rest_framework import serializers

from .models import Submission


class SubmissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ("status", "score")
