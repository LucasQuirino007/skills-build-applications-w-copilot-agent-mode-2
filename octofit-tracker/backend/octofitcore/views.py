from rest_framework import viewsets

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout
from .serializers import (
	ActivitySerializer,
	LeaderboardEntrySerializer,
	TeamSerializer,
	UserProfileSerializer,
	WorkoutSerializer,
)


class TeamViewSet(viewsets.ModelViewSet):
	queryset = Team.objects.all().order_by('name')
	serializer_class = TeamSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
	queryset = UserProfile.objects.select_related('team').all().order_by('alias')
	serializer_class = UserProfileSerializer


class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.select_related('user', 'team').all().order_by('-created_at')
	serializer_class = ActivitySerializer


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
	queryset = LeaderboardEntry.objects.select_related('user', 'team').all().order_by('rank_position')
	serializer_class = LeaderboardEntrySerializer


class WorkoutViewSet(viewsets.ModelViewSet):
	queryset = Workout.objects.select_related('user').all().order_by('-workout_date')
	serializer_class = WorkoutSerializer
