from bson import ObjectId
from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class ObjectIdSafeModelSerializer(serializers.ModelSerializer):
    """Converte qualquer ObjectId para string na serializacao."""

    id = serializers.CharField(source='pk', read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            if isinstance(value, ObjectId):
                data[key] = str(value)
        return data


class TeamSerializer(ObjectIdSafeModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'universe', 'points']


class UserProfileSerializer(ObjectIdSafeModelSerializer):
    team_id = serializers.CharField(read_only=True)
    team_name = serializers.CharField(source='team.name', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'full_name', 'alias', 'email', 'team', 'team_id', 'team_name', 'joined_at']


class ActivitySerializer(ObjectIdSafeModelSerializer):
    user_id = serializers.CharField(read_only=True)
    team_id = serializers.CharField(read_only=True)

    class Meta:
        model = Activity
        fields = [
            'id',
            'user',
            'user_id',
            'team',
            'team_id',
            'activity_type',
            'duration_minutes',
            'points',
            'created_at',
        ]


class LeaderboardEntrySerializer(ObjectIdSafeModelSerializer):
    user_id = serializers.CharField(read_only=True)
    team_id = serializers.CharField(read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'user_id', 'team', 'team_id', 'score', 'rank_position', 'updated_at']


class WorkoutSerializer(ObjectIdSafeModelSerializer):
    user_id = serializers.CharField(read_only=True)

    class Meta:
        model = Workout
        fields = ['id', 'user', 'user_id', 'title', 'duration_minutes', 'calories', 'workout_date']
