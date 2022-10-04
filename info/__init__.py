import random

from otree.api import *

from . import models


author = 'Your name here'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'info'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(blank=True)
    email = models.StringField(blank=True)
    mf = models.StringField(blank=True)
    age = models.IntegerField()


# FUNCTIONS
# PAGES
class Intro(Page):
    form_model = 'player'


class Who(Page):
    form_model = 'player'
    form_fields = ['name', 'email', 'mf', 'age']


page_sequence = [
    Who,
    Intro,
]
