from datetime import date

from django.test import TestCase
from rest_framework.test import APIClient

from .models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class OctoFitApiTests(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.team = Team.objects.create(name='Octo Squad', universe='Marvel', points=125)
		self.user = UserProfile.objects.create(
			full_name='Carol Danvers',
			alias='captain-marvel',
			email='carol@example.com',
			team=self.team,
		)
		self.activity = Activity.objects.create(
			user=self.user,
			team=self.team,
			activity_type='Run',
			duration_minutes=45,
			points=80,
		)
		self.leaderboard_entry = LeaderboardEntry.objects.create(
			user=self.user,
			team=self.team,
			score=320,
			rank_position=1,
		)
		self.workout = Workout.objects.create(
			user=self.user,
			title='Interval Training',
			duration_minutes=30,
			calories=260,
			workout_date=date(2026, 6, 9),
		)

	def test_root_redirects_to_api(self):
		response = self.client.get('/')

		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, '/api/')

	def test_api_root_lists_available_collections(self):
		response = self.client.get('/api/')

		self.assertEqual(response.status_code, 200)
		self.assertIn('users', response.data)
		self.assertIn('teams', response.data)
		self.assertIn('activities', response.data)
		self.assertIn('leaderboard', response.data)
		self.assertIn('workouts', response.data)

	def test_user_collection_returns_related_team_fields(self):
		response = self.client.get('/api/users/')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.data), 1)
		self.assertEqual(response.data[0]['alias'], 'captain-marvel')
		self.assertEqual(response.data[0]['team_name'], 'Octo Squad')
		self.assertEqual(response.data[0]['team_id'], str(self.team.pk))

	def test_activity_leaderboard_and_workout_collections(self):
		activity_response = self.client.get('/api/activities/')
		leaderboard_response = self.client.get('/api/leaderboard/')
		workout_response = self.client.get('/api/workouts/')

		self.assertEqual(activity_response.status_code, 200)
		self.assertEqual(activity_response.data[0]['user_id'], str(self.user.pk))
		self.assertEqual(leaderboard_response.status_code, 200)
		self.assertEqual(leaderboard_response.data[0]['rank_position'], 1)
		self.assertEqual(workout_response.status_code, 200)
		self.assertEqual(workout_response.data[0]['title'], 'Interval Training')
