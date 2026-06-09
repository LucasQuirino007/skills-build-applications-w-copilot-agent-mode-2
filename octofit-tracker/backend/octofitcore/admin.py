from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'universe', 'points')
	search_fields = ('name', 'universe')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('alias', 'full_name', 'email', 'team', 'joined_at')
	list_filter = ('team',)
	search_fields = ('alias', 'full_name', 'email')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('activity_type', 'user', 'team', 'duration_minutes', 'points', 'created_at')
	list_filter = ('team', 'activity_type')
	search_fields = ('activity_type', 'user__alias', 'team__name')


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
	list_display = ('rank_position', 'user', 'team', 'score', 'updated_at')
	list_filter = ('team',)
	ordering = ('rank_position',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
	list_display = ('title', 'user', 'duration_minutes', 'calories', 'workout_date')
	list_filter = ('workout_date',)
	search_fields = ('title', 'user__alias')
