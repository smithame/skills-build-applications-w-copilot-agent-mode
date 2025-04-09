from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe")
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha")
        team1.members.add(user1, user2)

        # Create test activities
        Activity.objects.create(user=user1, description="Running 5km")
        Activity.objects.create(user=user2, description="Cycling 10km")

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, score=150)

        # Create test workouts
        Workout.objects.create(user=user1, duration=30)
        Workout.objects.create(user=user2, duration=45)

        self.stdout.write(self.style.SUCCESS('Test data successfully populated.'))
