from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'info'
    players_per_group = None
    num_rounds=1

    

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(blank=True)
    email = models.StringField(blank=True)
    mf = models.StringField(blank=True)
    age = models.IntegerField()



