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
    name_in_url = 'tfmri'
    players_per_group = None
    speed= 0.01
    num_rounds=16

    

class Subsession(BaseSubsession):
    def creating_session(self):
       if self.round_number==1:
           for p in self.get_players(): 
             round_numbers = list(range(1,Constants.num_rounds+1))
             random.shuffle(round_numbers) 
             round_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

             p.participant.vars['task_rounds']=round_numbers
             p.participant.vars['rnd2']=[0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0]
             p.participant.vars['aans1']=['-','-','-','-','-','-','-','-','-','-', '-','-','-','-','-','-','-','-','-','-']
             p.participant.vars['aans2']=['-','-','-','-','-','-','-','-','-','-', '-','-','-','-','-','-','-','-','-','-']
             p.participant.vars['traindone']=0
             p.participant.vars['trainwin']=0
             p.participant.vars['qwin']=0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    randomTime = models.FloatField()
    difficulty = models.IntegerField()
    task = models.IntegerField(choices=[(0, 'Lost'),(1, 'Won')])
    difficulty1 = models.IntegerField()
    task1 = models.IntegerField(choices=[(0, 'Lost'),(1, 'Won')])
    difficulty2 = models.IntegerField()
    task2 = models.IntegerField(choices=[(0, 'Lost'),(1, 'Won')])
    difficulty0 = models.IntegerField()
    task0 = models.IntegerField(choices=[(0, 'Lost'),(1, 'Won')])
    difficulty01 = models.IntegerField()
    task01 = models.IntegerField(choices=[(0, 'Lost'),(1, 'Won')])
    difficulty02 = models.IntegerField()
    task02 = models.IntegerField(choices=[(0, 'Lost'),(1, 'Won')])



    gamedone = models.IntegerField(choices=[(0, 'Lost'),(1, 'Won')])
    gamedone1 = models.IntegerField(choices=[(0, 'Lost'),(1, 'Won')])
    gamedone2 = models.IntegerField(choices=[(0, 'Lost'),(1, 'Won')])

    ans1=models.StringField(blank=True)
    ans2=models.StringField(blank=True)
    ans1r=models.StringField(blank=True)
    ans2r=models.StringField(blank=True)

    currentTime = models.FloatField()
    ans = models.BooleanField()
    b1=models.IntegerField()
    b2=models.IntegerField()
    q=models.IntegerField()
    currentTime2 = models.FloatField()
    timerest = models.IntegerField()                          
    timerest1 = models.IntegerField()
    timerest0 = models.IntegerField()                          
    timerest01 = models.IntegerField()



