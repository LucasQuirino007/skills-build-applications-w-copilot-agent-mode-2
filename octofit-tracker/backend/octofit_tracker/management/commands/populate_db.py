from datetime import date

from django.core.management.base import BaseCommand
from django.db import transaction

from octofitcore.models import Activity, LeaderboardEntry, Team, UserProfile, Workout


class Command(BaseCommand):
    help = 'Popular o banco de dados octofit_db com dados de teste'

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Limpando colecoes existentes...')
        Activity.objects.all().delete()
        LeaderboardEntry.objects.all().delete()
        Workout.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write('Criando equipes...')
        marvel = Team.objects.create(name='Equipe Marvel', universe='Marvel', points=620)
        dc = Team.objects.create(name='Equipe DC', universe='DC', points=580)

        self.stdout.write('Criando usuarios...')
        users = [
            UserProfile.objects.create(full_name='Peter Parker', alias='Homem-Aranha', email='spiderman@marvel.com', team=marvel),
            UserProfile.objects.create(full_name='Tony Stark', alias='Homem de Ferro', email='ironman@marvel.com', team=marvel),
            UserProfile.objects.create(full_name='Bruce Wayne', alias='Batman', email='batman@dc.com', team=dc),
            UserProfile.objects.create(full_name='Diana Prince', alias='Mulher-Maravilha', email='wonderwoman@dc.com', team=dc),
        ]

        self.stdout.write('Criando treinos e atividades...')
        workout_defs = [
            ('Treino de Agilidade', 45, 420),
            ('Treino de Forca', 60, 560),
            ('Treino Funcional Heroico', 50, 500),
            ('Treino de Resistencia', 55, 530),
        ]
        activity_defs = [
            ('Corrida urbana', 40, 140),
            ('Sessao de combate', 50, 170),
            ('Escalada tatica', 35, 120),
            ('Treino de reflexo', 30, 110),
        ]

        for index, user in enumerate(users):
            title, duration, calories = workout_defs[index]
            Workout.objects.create(
                user=user,
                title=title,
                duration_minutes=duration,
                calories=calories,
                workout_date=date.today(),
            )

            activity_type, activity_duration, points = activity_defs[index]
            Activity.objects.create(
                user=user,
                team=user.team,
                activity_type=activity_type,
                duration_minutes=activity_duration,
                points=points,
            )

        self.stdout.write('Criando leaderboard...')
        ranking = sorted(users, key=lambda item: item.team.points, reverse=True)
        for position, user in enumerate(ranking, start=1):
            LeaderboardEntry.objects.create(
                user=user,
                team=user.team,
                score=user.team.points + (5 - position) * 10,
                rank_position=position,
            )

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com sucesso.'))
