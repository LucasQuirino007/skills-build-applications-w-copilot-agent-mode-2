from django.db import models


class Team(models.Model):
	name = models.CharField(max_length=64, unique=True)
	universe = models.CharField(max_length=16)
	points = models.IntegerField(default=0)

	class Meta:
		db_table = 'teams'
		ordering = ['name']

	def __str__(self):
		return self.name


class UserProfile(models.Model):
	full_name = models.CharField(max_length=120)
	alias = models.CharField(max_length=64)
	email = models.EmailField(unique=True)
	team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='users')
	joined_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'users'
		ordering = ['alias']

	def __str__(self):
		return f'{self.alias} ({self.email})'


class Workout(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
	title = models.CharField(max_length=100)
	duration_minutes = models.PositiveIntegerField()
	calories = models.PositiveIntegerField()
	workout_date = models.DateField()

	class Meta:
		db_table = 'workouts'
		ordering = ['-workout_date', 'title']

	def __str__(self):
		return f'{self.title} - {self.user.alias}'


class Activity(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='activities')
	activity_type = models.CharField(max_length=64)
	duration_minutes = models.PositiveIntegerField()
	points = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'activities'
		ordering = ['-created_at']

	def __str__(self):
		return f'{self.activity_type} - {self.user.alias}'


class LeaderboardEntry(models.Model):
	user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entries')
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard_entries')
	score = models.IntegerField(default=0)
	rank_position = models.PositiveIntegerField()
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'leaderboard'
		ordering = ['rank_position', '-score']
		unique_together = ('user', 'rank_position')

	def __str__(self):
		return f'#{self.rank_position} {self.user.alias}'
