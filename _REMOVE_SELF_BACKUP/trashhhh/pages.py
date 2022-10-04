from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Intro(Page):
  def is_displayed(self):
     return self.round_number==1

class DifficultyChoice(Page):
    form_model = 'player'
    form_fields = ['difficulty']
class DifficultyChoice1(Page):
    form_model = 'player'
    form_fields = ['difficulty1']
class DifficultyChoice2(Page):
    form_model = 'player'
    form_fields = ['difficulty2']



class Train(Page):
    form_model = 'player'
    form_fields = ['task','gamedone','timerest']
    def before_next_page(self):
          self.participant.vars['traindone']=self.player.gamedone+self.participant.vars['traindone']
          self.participant.vars['trainwin']=self.player.task*(self.player.difficulty+1)+self.participant.vars['trainwin']


class Train1(Page):
    form_model = 'player'
    form_fields = ['task1','gamedone1','timerest1']
    def vars_for_template(self):
          return dict(timerest=self.player.timerest)
    def before_next_page(self):
          self.participant.vars['traindone']=self.player.gamedone1+self.participant.vars['traindone']
          self.participant.vars['trainwin']=self.player.task1*(self.player.difficulty1+1)+self.participant.vars['trainwin']
    def is_displayed(self):
          return self.player.timerest>300


class Train2(Page):
    form_model = 'player'
    form_fields = ['gamedone2','task2']
    def vars_for_template(self):
          return dict(timerest=self.player.timerest1)
    def before_next_page(self):
          self.participant.vars['traindone']=self.player.gamedone2+self.participant.vars['traindone']
          self.participant.vars['trainwin']=self.player.task2*(self.player.difficulty2+1)+self.participant.vars['trainwin']

    def is_displayed(self):
          if self.player.timerest<301: 
           self.player.timerest1=0
          return self.player.timerest1>300


class Befor(Page):
    form_model = 'player'
    form_fields = ['currentTime','ans','q']
    timeout_seconds = 20
    def vars_for_template(self):
          qw=['комната - положение - река','голова - монарх - солнечный ','подсолнух - солнце - масло','садовая - мозг - пустая','друг - город - круг','дверь - доверие - быстро','долгая - вечер - друзья','болид - квалификация - вооружение','скакалка - пружина - мяч','детство - случай - хорошее']
          qw=['громкая - правда - медленно','холодная - зелень - мутная','толковый - книга - Даль','география - туз - масштаб','береста - плести - гриб','клетка - лист - обложка','зубной - тонкий - клубок','сочный - искушение - круглый','трудное - истекло - золото','школа - лямка - спина']
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

          qw1=['и','а','з','в','ж', 'т','с','г','и','в']
          qw2=['в','б','ж','г','б', 'у','з','к','п','ф']
          qw3=['к','к','и','с','з', 'ф','в','з','р','з']
          qw4=['с','д','к','т','н', 'в','г','с','с','с']
          qw1=['п','а','п','к','к', 'т','н','а','а','п']
          qw2=['р','б','р','л','л', 'г','о','с','б','р']
          qw3=['г','в','г','м','м', 'к','в','я','в','к']
          qw4=['к','г','к','н','н', 'п','т','г','г','к']


          return dict(a1=qw1[self.participant.vars['task_rounds'][self.round_number-1]-1],a2=qw2[self.participant.vars['task_rounds'][self.round_number-1]-1],a3=qw3[self.participant.vars['task_rounds'][self.round_number-1]-1],a4=qw4[self.participant.vars['task_rounds'][self.round_number-1]-1])
    def before_next_page(self):
          self.participant.vars['aans1'][self.round_number-1] = self.player.ans1 


class Afterans(Page):
    form_model = 'player'
    form_fields = ['ans2']
    timeout_seconds = 6
    def vars_for_template(self):
          qw=['комната - положение - река', 'голова - монарх - солнечный ',    'подсолнух - солнце - масло',  'садовая - мозг - пустая',    'друг - город - круг'    ,     'дверь - доверие - быстро',    'долгая - вечер - друзья',  'болид - квалификация - вооружение',  'скакалка - пружина - мяч',  'детство - случай - хорошее']
          qw=['громкая - правда - медленно','холодная - зелень - мутная','толковый - книга - Даль','география - туз - масштаб','береста - плести - гриб','клетка - лист - обложка','зубной - тонкий - клубок','сочный - искушение - круглый','трудное - истекло - золото','школа - лямка - спина']

          qw1=['и','а','з','в','ж', 'т','с','г','и','в']
          qw2=['в','б','ж','г','б', 'у','з','к','п','ф']
          qw3=['к','к','и','с','з', 'ф','в','з','р','з']
          qw4=['с','д','к','т','н', 'в','г','с','с','с']
          qw1=['п','а','п','к','к', 'т','н','а','а','п']
          qw2=['р','б','р','л','л', 'г','о','с','б','р']
          qw3=['г','в','г','м','м', 'к','в','я','в','к']
          qw4=['к','г','к','н','н', 'п','т','г','г','к']


          return dict(a=qw[self.participant.vars['task_rounds'][self.round_number-1]-1],a1=qw1[self.participant.vars['task_rounds'][self.round_number-1]-1],a2=qw2[self.participant.vars['task_rounds'][self.round_number-1]-1],a3=qw3[self.participant.vars['task_rounds'][self.round_number-1]-1],a4=qw4[self.participant.vars['task_rounds'][self.round_number-1]-1])
    def before_next_page(self):
          self.participant.vars['aans2'][self.round_number-1] = self.player.ans2 



class Res(Page):
    def is_displayed(self):
        return self.player.ans
    form_model = 'player'
    form_fields = ['b1']
    timeout_seconds = 6
    
    def vars_for_template(self):
          qa1=['йти',                        'корона',                        'елт',                          'голова',                      'близкий',                'войти',                      'встреча',                   'гонк',                                       'прыг','воспоминание']
          qa1=['в',                          'к',                             'ж',                            'г',                           'б',                      'в',                          'в',                         'г',                                       'п','в']
          qa2=['лев',                        'бабочка',                       'олот',                         'тыква',                       'знакомый',               'входить',                    'сиде',                      'щщщщ',                                       'щщщщ','щщщщ']
          qa2=['с',                          'б',                             'з',                            'т',                           'з',                      'в',                          'с',                         'щщщщ',                                       'щщщщ','щщщщ']
          qa1=['р','в','с','к','к', 'т','н','я','в','р']
          qa2=['г','б','э','к','л', 'п','н','я','в','р']

          a1=qa1[self.participant.vars['task_rounds'][self.round_number-1]-1]
          a2=qa2[self.participant.vars['task_rounds'][self.round_number-1]-1]
          c='Вашего ответа нет в числе известных нам. 0 баллов, попробуйте за вторую попытку дать более известный ответ.'
          b1=0
          if self.player.ans1:
           if a2 in self.player.ans1: 
            c='Вы дали правильный ответ и получаете 3 балла. Попробуйте за второую попытку дать еще один ответ' 
            b1=3
           if a1 in self.player.ans1: 
            c='Вы дали правильный ответ и получаете 3 балла. Попробуйте за второую попытку дать еще один ответ' 
            b1=3
          self.participant.vars['qwin']=b1+self.participant.vars['qwin']
          return dict(a=c,b=b1)

class Res2(Page):
    form_model = 'player'
    form_fields = ['b2']
    timeout_seconds = 12
    
    def vars_for_template(self):
          qa1=['йти',                        'корона',                        'елт',                          'голова',                      'близкий',                'войти',                      'встреча',                   'гонк',                                       'прыг','воспоминание']
          qa1=['в',                          'к',                             'ж',                            'г',                           'б',                      'в',                          'в',                         'г',                                       'п','в']
          qa2=['лев',                        'бабочка',                       'олот',                         'тыква',                       'знакомый',               'входить',                    'сиде',                      'щщщщ',                                       'щщщщ','щщщщ']
          qa2=['с',                          'б',                             'з',                            'т',                           'з',                      'в',                          'с',                         'щщщщ',                                       'щщщщ','щщщщ']
          qa1=['р','в','с','к','к', 'т','н','я','в','р']
          qa2=['г','б','э','к','л', 'п','н','я','в','р']


          a1=qa1[self.participant.vars['task_rounds'][self.round_number-1]-1]
          a2=qa2[self.participant.vars['task_rounds'][self.round_number-1]-1]
          c='Вашего ответа нет в числе известных намю 0 баллов.'
          b1=0
          if self.player.ans2:
           if a2 in self.player.ans2: 
            c='Вы дали правильный ответ и получаете 3 балла. ' 
            b1=3
           if a1 in self.player.ans2: 
            c='Вы дали правильнй ответ и получаете 3 балла. ' 
            b1=3
          self.participant.vars['qwin']=b1+self.participant.vars['qwin']
          return dict(a=c,b=b1,gr=self.participant.vars['traindone'],ballres=self.participant.vars['trainwin'],qres=self.participant.vars['qwin'])

class Q1(Page):

    form_model = 'player'
    form_fields = ['ans1r']
class Q2(Page):

    form_model = 'player'
    form_fields = ['ans2r']


    
class Results(Page):
    pass

page_sequence = [
    Cross,
    Befor,
    Beforans,
    Q1,
    Res,
    DifficultyChoice,
    Train,
    DifficultyChoice1,
    Train1,
    DifficultyChoice2,
    Train2,
    Afterans,
    Q2,
    Res2,

]
