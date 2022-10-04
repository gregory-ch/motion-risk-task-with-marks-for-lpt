import random

from otree.api import *

from . import models


author = 'Your name here'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'fin20'
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
    ins11 = models.StringField(blank=True)
    ins12 = models.StringField(blank=True)
    ins13 = models.StringField(blank=True)
    ins14 = models.StringField(blank=True)
    ins15 = models.StringField(blank=True)
    ins16 = models.StringField(blank=True)
    ins17 = models.StringField(blank=True)
    ins18 = models.StringField(blank=True)
    ins19 = models.StringField(blank=True)
    ins20 = models.StringField(blank=True)


# FUNCTIONS
# PAGES
class Insa(Page):
    form_model = 'player'
    form_fields = [
        'ins1',
        'ins2',
        'ins3',
        'ins4',
        'ins5',
        'ins6',
        'ins7',
        'ins8',
        'ins9',
        'ins10',
        'ins11',
        'ins12',
        'ins13',
        'ins14',
        'ins15',
        'ins16',
        'ins17',
        'ins18',
        'ins19',
        'ins20',
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
            'каракатица - фиолетовый - писать',
            'клетка - лист - обложка',
            'кисть - безымянный - кольцо',
            'трудное - истекло - золото',
            'день - заяц - цвет',
            'календарь - светит - ночь',
            'олень - ветвистый - изобилие',
            'вечерняя - бумага - стенная',
            'горький - молочный - крем',
            'бледная - спутник -круглая',
        ]
        qww = [
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
            ' ',
        ]
        n = 0
        for x in range(20):
            n = player.participant.vars['task_rounds'][x]
            qww[x] = qw[n - 1]
        return dict(
            a=qww,
            cu=player.participant.vars['rnd2'],
            e=player.participant.vars['task_rounds'],
            f=player.participant.vars['aans2'],
        )


page_sequence = [
    Insa,
]
