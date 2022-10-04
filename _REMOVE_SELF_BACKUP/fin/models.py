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
    name_in_url = 'fin'
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



