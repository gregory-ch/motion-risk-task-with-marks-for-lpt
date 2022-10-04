from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Insa(Page):

    form_model = 'player'
    form_fields = ['ins1','ins2','ins3','ins4','ins5','ins6','ins7','ins8','ins9','ins10']

    def vars_for_template(self):
          qw=['комната - положение - река','голова - монарх - солнечный ','подсолнух - солнце - масло','садовая - мозг - пустая','друг - город - круг','дверь - доверие - быстро','долгая - вечер - друзья','болид - квалификация - вооружение','скакалка - пружина - мяч','детство - случай - хорошее']
          qww=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
          n=0
          for x in range(10):
             n=  self.participant.vars['task_rounds'][x]
             qww[x]=qw[n-1]
          return dict(a=qww, c=self.participant.vars['rnd2'],e=self.participant.vars['task_rounds'], f=self.participant.vars['aans2'])

          
class Words(Page):

    form_model = 'player'
    form_fields = ['ans11','ans12','ans13','ans14','ans15','ans16','ans17','ans18','ans19', 'ans110','ans21','ans22','ans23','ans24','ans25','ans26','ans27','ans28','ans29','ans210'  ]


    def vars_for_template(self):
          qw=['комната - положение - река','голова - монарх - солнечный ','подсолнух - солнце - масло','садовая - мозг - пустая','друг - город - круг','дверь - доверие - быстро','долгая - вечер - друзья','болид - квалификация - вооружение','скакалка - пружина - мяч','детство - случай - хорошее']
          qww=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
          n=0
          for x in range(10):
             n=  self.participant.vars['task_rounds'][x]
             qww[x]=qw[n-1]
          
          return dict(a=qww,e=self.participant.vars['task_rounds'], f1=self.participant.vars['aans1'],f2=self.participant.vars['aans2'])
  

    
page_sequence = [
    Insa,
    Words,

]
