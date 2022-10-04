from otree.api import Currency as cu, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Intro(Page):
  def is_displayed(self):
     return self.round_number==1


class Train(Page):
    form_model = 'player'
    form_fields = ['difficulty', 'task']
    def vars_for_template(self):
          return dict(timerest=30000)

class Train1(Page):
    form_model = 'player'
    form_fields = ['difficulty1', 'task1']
class Train2(Page):
    form_model = 'player'
    form_fields = ['difficulty2', 'task2']

class Befor(Page):
    form_model = 'player'
    form_fields = ['currentTime','ans','q']
    timeout_seconds = 20
    def vars_for_template(self):
          qw=['комната - положение - река','голова - монарх - солнечный ','подсолнух - солнце - масло','садовая - мозг - пустая','друг - город - круг','дверь - доверие - быстро','долгая - вечер - друзья','болид - квалификация - вооружение','скакалка - пружина - мяч','детство - случай - хорошее']
          return dict(a=qw[self.participant.vars['task_rounds'][self.round_number-1]-1],qa=self.round_number,qb=self.participant.vars['task_rounds'][self.round_number-1])
    def before_next_page(self):
          self.participant.vars['rnd2'][self.round_number-1] = 1*self.player.ans 

class Cross(Page):
    form_model = 'player'
    form_fields = ['randomTime']


class Beforans(Page):
    def is_displayed(self):
        return self.player.ans
    form_model = 'player'
    form_fields = ['ans1']
    timeout_seconds = 6
    def vars_for_template(self):
          qw1=['и','а','з','в','ж','т','д','г','и','в']
          qw2=['й','б','ж','г','и','у','т','к','ы','ф']
          qw3=['к','ц','и','с','к','ф','ж','з','ь','з']
          qw4=['л','д','к','т','н','х','ш','с','ъ','с']
          return dict(a1=qw1[self.participant.vars['task_rounds'][self.round_number-1]-1],a2=qw2[self.participant.vars['task_rounds'][self.round_number-1]-1],a3=qw3[self.participant.vars['task_rounds'][self.round_number-1]-1],a4=qw4[self.participant.vars['task_rounds'][self.round_number-1]-1])

class Afterans(Page):
    form_model = 'player'
    form_fields = ['ans2']
    timeout_seconds = 6
    def vars_for_template(self):
          qw=['комната - положение - река', 'голова - монарх - солнечный ',    'подсолнух - солнце - масло',  'садовая - мозг - пустая',    'друг - город - круг',     'дверь - доверие - быстро',    'долгая - вечер - друзья',  'болид - квалификация - вооружение',  'скакалка - пружина - мяч',  'детство - случай - хорошее']
          qw1=['и','а','з','в','ж','т','д','г','и','в']
          qw2=['й','б','ж','г','и','у','т','к','ы','ф']
          qw3=['к','ц','и','с','к','ф','ж','з','ь','з']
          qw4=['л','д','к','т','н','х','ш','с','ъ','с']
          return dict(a=qw[self.participant.vars['task_rounds'][self.round_number-1]-1],a1=qw1[self.participant.vars['task_rounds'][self.round_number-1]-1],a2=qw2[self.participant.vars['task_rounds'][self.round_number-1]-1],a3=qw3[self.participant.vars['task_rounds'][self.round_number-1]-1],a4=qw4[self.participant.vars['task_rounds'][self.round_number-1]-1])
    def before_next_page(self):
          self.participant.vars['aans2'][self.round_number-1] = self.player.ans2 


class After(Page):
    form_model = 'player'
    form_fields = ['ans2','currentTime2']
    timeout_seconds = 6
    def vars_for_template(self):
          qw=['комната - положение - река', 'голова - монарх - солнечный ',    'подсолнух - солнце - масло',  'садовая - мозг - пустая',    'друг - город - круг',     'дверь - доверие - быстро',    'долгая - вечер - друзья',  'болид - квалификация - вооружение',  'скакалка - пружина - мяч',  'детство - случай - хорошее']
          qw=['a) и,  b) й,  c) к, d) л. ', 'a) а, b) б, c) ц, d) д.',         'a) з, b) ж, c) и, d) к.',     'a) в, b) г, c) с, d) т.',    'a) ж, b) и, c) к, d) н.', 'a) т, b) у, c) ф, d) х.',     'a) д, b) т, c) ж, d) ш.',  'a) г, b) к, c) з, d) с.',            'a) и, b) ы, c) ь, d) ъ.',   'a) в, b) ф, c) з, d) с.']
          return dict(a=qw[self.participant.vars['task_rounds'][self.round_number-1]-1],qa=self.round_number,qb=self.participant.vars['task_rounds'][self.round_number-1])
    def before_next_page(self):
          self.participant.vars['aans2'][self.round_number-1] = self.player.ans2 


class Res(Page):
    def is_displayed(self):
        return self.player.ans
    form_model = 'player'
    form_fields = ['b']
    timeout_seconds = 6
    
    def vars_for_template(self):
          qa1=['йти',                        'корона',                        'елт',                          'голова',                      'близкий',                'войти',                      'встреча',                   'гонк',                                       'прыг','воспоминание']
          qa1=['й',                          'а',                             'ж',                            'г',                           'к',                     'т',                          'т',                         'г',                                       'ы','в']
          qa2=['лев',                        'бабочка',                       'олот',                         'тыква',                       'знакомый',               'входить',                    'сиде',                      'щщщщ',                                       'щщщщ','щщщщ']
          qa2=['л',                          'б',                             'з',                            'т',                           'н',                      'х',                          'д',                         'щщщщ',                                       'щщщщ','щщщщ']
          a1=qa1[self.participant.vars['task_rounds'][self.round_number-1]-1]
          a2=qa2[self.participant.vars['task_rounds'][self.round_number-1]-1]
          c='Вашего ответа нет в числе встречаемых - 0 баллов, попробуйте за вторую попытку дать более встречающийся ответ.'
          b1=0
          if self.player.ans1:
           if a2 in self.player.ans1: 
            c='Вы выбрали второй по встречаемости ответ и получаете половину баллов -1 балл. Попробуйте за второую попытку угадать самый встречающийся ответ' 
            b1=1
           if a1 in self.player.ans1: 
            c='Вы выбрали самый встречаемый ответ и получаете полный балл - 2 балла. Попробуйте за вторую попытку угадать второй по встречаемости ответ' 
            b1=2
          return dict(a=c,b=b1)
class Res2(Page):
    form_model = 'player'
    form_fields = ['b']
    timeout_seconds = 6
    
    def vars_for_template(self):
          qa1=['йти',                        'корона',                        'елт',                          'голова',                      'близкий',                'войти',                      'встреча',                   'гонк',                                       'прыг','воспоминание']
          qa1=['й',                          'а',                             'ж',                            'г',                           'к',                     'т',                          'т',                         'г',                                       'ы','в']
          qa2=['лев',                        'бабочка',                       'олот',                         'тыква',                       'знакомый',               'входить',                    'сиде',                      'щщщщ',                                       'щщщщ','щщщщ']
          qa2=['л',                          'б',                             'з',                            'т',                           'н',                      'х',                          'д',                         'щщщщ',                                       'щщщщ','щщщщ']
          a1=qa1[self.participant.vars['task_rounds'][self.round_number-1]-1]
          a2=qa2[self.participant.vars['task_rounds'][self.round_number-1]-1]
          c='Вашего ответа нет в числе встречаемых - 0 баллов, попробуйте за вторую попытку дать более встречающийся ответ.'
          b1=0
          if self.player.ans2:
           if a2 in self.player.ans2: 
            c='Вы выбрали второй по встречаемости ответ и получаете половину баллов -1 балл. Попробуйте за второую попытку угадать самый встречающийся ответ' 
            b1=1
           if a1 in self.player.ans2: 
            c='Вы выбрали самый встречаемый ответ и получаете полный балл - 2 балла. Попробуйте за вторую попытку угадать второй по встречаемости ответ' 
            b1=2
          return dict(a=c,b=b1)


class Insa(Page):
    def is_displayed(self):
     	return self.round_number==10

    form_model = 'player'
    form_fields = ['ins1','ins2','ins3','ins4','ins5','ins6','ins7','ins8','ins9','ins10']

    def vars_for_template(self):
          qw=['комната - положение - река','голова - монарх - солнечный ','подсолнух - солнце - масло','садовая - мозг - пустая','друг - город - круг','дверь - доверие - быстро','долгая - вечер - друзья','болид - квалификация - вооружение','скакалка - пружина - мяч','детство - случай - хорошее']
          qww=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
          n=0
          for x in range(10):
             n=  self.participant.vars['task_rounds'][x]
             qww[x]=qw[n-1]
          
          return dict(a=qww, cu=self.participant.vars['rnd2'],e=[1,2,3,4,5,6,7,8,9,10], f=self.participant.vars['aans2'])
  

    
class Results(Page):
    pass

page_sequence = [
    Intro,
    Cross,
    Befor,
    Beforans,
    Res,
    Train,
    Train1,
    Train2,
    Afterans,
    Res2,
    Insa,

]
