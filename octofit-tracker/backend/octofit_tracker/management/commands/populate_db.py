from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        marvel_members = ['Tony Stark', 'Peter Parker', 'Steve Rogers']
        dc_members = ['Bruce Wayne', 'Clark Kent', 'Diana Prince']

        Team.objects.create(name='marvel', members=marvel_members)
        Team.objects.create(name='dc', members=dc_members)

        User.objects.create(name='Tony Stark', email='tony@marvel.com', team='marvel', is_superhero=True)
        User.objects.create(name='Peter Parker', email='peter@marvel.com', team='marvel', is_superhero=True)
        User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='marvel', is_superhero=True)
        User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc', is_superhero=True)
        User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc', is_superhero=True)
        User.objects.create(name='Diana Prince', email='diana@dc.com', team='dc', is_superhero=True)

        Activity.objects.create(user='Tony Stark', activity_type='Running', duration=30, date='2026-02-09')
        Activity.objects.create(user='Bruce Wayne', activity_type='Cycling', duration=45, date='2026-02-09')
        Activity.objects.create(user='Clark Kent', activity_type='Swimming', duration=60, date='2026-02-09')

        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
