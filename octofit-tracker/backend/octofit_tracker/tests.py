from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create(name='Test User', email='test@user.com', team_name=team.name)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.team_name, 'Test Team')

    def test_activity_creation(self):
        user = User.objects.create(name='Test User', email='test@user.com', team_name='Test Team')
        activity = Activity.objects.create(user_email=user.email, type='Running', duration=30)
        self.assertEqual(activity.type, 'Running')
        self.assertEqual(activity.duration, 30)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Desc', suggested_for='Test Team')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team_name='Test Team', points=50)
        self.assertEqual(leaderboard.team_name, 'Test Team')
        self.assertEqual(leaderboard.points, 50)
