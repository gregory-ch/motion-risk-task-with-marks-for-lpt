from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Intro(Page):
    form_model = 'player'


class Who(Page):
    form_model = 'player'
    form_fields = ['name', 'email','mf','age']


page_sequence = [
    Who,
    Intro,

]
