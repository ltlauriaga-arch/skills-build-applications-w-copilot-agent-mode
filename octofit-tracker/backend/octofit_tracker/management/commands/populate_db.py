from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()


        # Create teams
        Team.objects.create(name='Marvel')
        Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team_name='Marvel'),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team_name='Marvel'),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team_name='DC'),
            User.objects.create(name='Batman', email='batman@dc.com', team_name='DC'),
        ]

        # Create activities
        Activity.objects.create(user_email='spiderman@marvel.com', type='Running', duration=30)
        Activity.objects.create(user_email='ironman@marvel.com', type='Cycling', duration=45)
        Activity.objects.create(user_email='wonderwoman@dc.com', type='Swimming', duration=25)
        Activity.objects.create(user_email='batman@dc.com', type='Yoga', duration=60)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Power Yoga', description='Strength and flexibility', suggested_for='DC')

        # Create leaderboard
        Leaderboard.objects.create(team_name='Marvel', points=100)
        Leaderboard.objects.create(team_name='DC', points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
