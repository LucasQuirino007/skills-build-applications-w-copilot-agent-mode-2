from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ActivityViewSet,
    LeaderboardEntryViewSet,
    TeamViewSet,
    UserProfileViewSet,
    WorkoutViewSet,
)

app_name = 'octofitcore'

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'leaderboard', LeaderboardEntryViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('', include(router.urls)),
]
