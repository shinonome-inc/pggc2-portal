from rest_framework import serializers

from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()

    class Meta:
        model = Team
        fields = ("id", "name", "role")
