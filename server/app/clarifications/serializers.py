from rest_framework import serializers

from .models import Clarification


class ClarificationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clarification
        fields = ("answer", "is_public")
