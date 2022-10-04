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
    name_in_url = 'fin20'
    players_per_group = None
    num_rounds=1

    

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





