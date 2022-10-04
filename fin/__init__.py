import random

from otree.api import *

from . import models


author = 'Your name here'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'fin'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ins1 = models.StringField(blank=True)
    ins2 = models.StringField(blank=True)
    ins3 = models.StringField(blank=True)
    ins4 = models.StringField(blank=True)
    ins5 = models.StringField(blank=True)
    ins6 = models.StringField(blank=True)
    ins7 = models.StringField(blank=True)
    ins8 = models.StringField(blank=True)
    ins9 = models.StringField(blank=True)
    ins10 = models.StringField(blank=True)
    ans11 = models.StringField(blank=True)
    ans12 = models.StringField(blank=True)
    ans13 = models.StringField(blank=True)
    ans14 = models.StringField(blank=True)
    ans15 = models.StringField(blank=True)
    ans16 = models.StringField(blank=True)
    ans17 = models.StringField(blank=True)
    ans18 = models.StringField(blank=True)
    ans19 = models.StringField(blank=True)
    ans110 = models.StringField(blank=True)
    ans21 = models.StringField(blank=True)
    ans22 = models.StringField(blank=True)
    ans23 = models.StringField(blank=True)
    ans24 = models.StringField(blank=True)
    ans25 = models.StringField(blank=True)
    ans26 = models.StringField(blank=True)
    ans27 = models.StringField(blank=True)
    ans28 = models.StringField(blank=True)
    ans29 = models.StringField(blank=True)
    ans210 = models.StringField(blank=True)


# FUNCTIONS
# PAGES
class Insa(Page):
    form_model = 'player'
    form_fields = ['ins1', 'ins2', 'ins3', 'ins4', 'ins5', 'ins6', 'ins7', 'ins8', 'ins9', 'ins10']

    @staticmethod
    def vars_for_template(player: Player):
        qw = [
            'комната - положение - река',
            'голова - монарх - солнечный ',
            'подсолнух - солнце - масло',
            'садовая - мозг - пустая',
            'друг - город - круг',
            'дверь - доверие - быстро',
            'долгая - вечер - друзья',
            'болид - квалификация - вооружение',
            'скакалка - пружина - мяч',
            'детство - случай - хорошее',
        ]
        qww = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        n = 0
        for x in range(10):
            n = player.participant.vars['task_rounds'][x]
            qww[x] = qw[n - 1]
        return dict(
            a=qww,
            cu=player.participant.vars['rnd2'],
            e=player.participant.vars['task_rounds'],
            f=player.participant.vars['aans2'],
        )


class Words(Page):
    form_model = 'player'
    form_fields = [
        'ans11',
        'ans12',
        'ans13',
        'ans14',
        'ans15',
        'ans16',
        'ans17',
        'ans18',
        'ans19',
        'ans110',
        'ans21',
        'ans22',
        'ans23',
        'ans24',
        'ans25',
        'ans26',
        'ans27',
        'ans28',
        'ans29',
        'ans210',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        qw = [
            'комната - положение - река',
            'голова - монарх - солнечный ',
            'подсолнух - солнце - масло',
            'садовая - мозг - пустая',
            'друг - город - круг',
            'дверь - доверие - быстро',
            'долгая - вечер - друзья',
            'болид - квалификация - вооружение',
            'скакалка - пружина - мяч',
            'детство - случай - хорошее',
        ]
        qww = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        n = 0
        for x in range(10):
            n = player.participant.vars['task_rounds'][x]
            qww[x] = qw[n - 1]
        return dict(
            a=qww,
            e=player.participant.vars['task_rounds'],
            f1=player.participant.vars['aans1'],
            f2=player.participant.vars['aans2'],
        )


page_sequence = [
    Insa,
    Words,
]
