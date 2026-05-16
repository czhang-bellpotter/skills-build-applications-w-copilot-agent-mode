
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        users = [
            User(email='tony@stark.com', username='ironman', team=marvel),
            User(email='steve@rogers.com', username='captainamerica', team=marvel),
            User(email='bruce@wayne.com', username='batman', team=dc),
            User(email='clark@kent.com', username='superman', team=dc),
        ]
        for user in users:
            user.set_password('password')
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, calories=300)
        Activity.objects.create(user=users[1], type='cycle', duration=45, calories=400)
        Activity.objects.create(user=users[2], type='swim', duration=60, calories=500)
        Activity.objects.create(user=users[3], type='yoga', duration=50, calories=200)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=1000)
        Leaderboard.objects.create(user=users[1], score=900)
        Leaderboard.objects.create(user=users[2], score=950)
        Leaderboard.objects.create(user=users[3], score=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
