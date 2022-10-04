import random

from otree.api import *

from . import models


author = 'Your name here'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 't'
    players_per_group = None
    speed = 0.01
    num_rounds = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    randomTime = models.FloatField()
    difficulty = models.IntegerField()
    task = models.IntegerField(choices=[(0, 'Lost'), (1, 'Won')])
    difficulty1 = models.IntegerField()
    task1 = models.IntegerField(choices=[(0, 'Lost'), (1, 'Won')])
    difficulty2 = models.IntegerField()
    task2 = models.IntegerField(choices=[(0, 'Lost'), (1, 'Won')])
    gamedone = models.IntegerField(choices=[(0, 'Lost'), (1, 'Won')])
    gamedone1 = models.IntegerField(choices=[(0, 'Lost'), (1, 'Won')])
    gamedone2 = models.IntegerField(choices=[(0, 'Lost'), (1, 'Won')])
    ans1 = models.StringField(blank=True)
    ans2 = models.StringField(blank=True)
    ans1r = models.StringField(blank=True)
    ans2r = models.StringField(blank=True)
    currentTime = models.FloatField()
    ans = models.BooleanField()
    b1 = models.IntegerField()
    b2 = models.IntegerField()
    q = models.IntegerField()
    currentTime2 = models.FloatField()
    timerest = models.IntegerField()
    timerest1 = models.IntegerField()


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_rounds + 1))
            random.shuffle(round_numbers)
            p.participant.vars['task_rounds'] = round_numbers
            p.participant.vars['rnd2'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            p.participant.vars['aans1'] = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
            p.participant.vars['aans2'] = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
            p.participant.vars['traindone'] = 0
            p.participant.vars['trainwin'] = 0
            p.participant.vars['qwin'] = 0


# PAGES
class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


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
    form_fields = ['task', 'gamedone', 'timerest']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['traindone'] = (
            player.gamedone + player.participant.vars['traindone']
        )
        player.participant.vars['trainwin'] = (
            player.task * (player.difficulty + 1) + player.participant.vars['trainwin']
        )


class Train1(Page):
    form_model = 'player'
    form_fields = ['task1', 'gamedone1', 'timerest1']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(timerest=player.timerest)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['traindone'] = (
            player.gamedone1 + player.participant.vars['traindone']
        )
        player.participant.vars['trainwin'] = (
            player.task1 * (player.difficulty1 + 1) + player.participant.vars['trainwin']
        )

    @staticmethod
    def is_displayed(player: Player):
        return player.timerest > 300


class Train2(Page):
    form_model = 'player'
    form_fields = ['gamedone2', 'task2']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(timerest=player.timerest1)

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['traindone'] = (
            player.gamedone2 + player.participant.vars['traindone']
        )
        player.participant.vars['trainwin'] = (
            player.task2 * (player.difficulty2 + 1) + player.participant.vars['trainwin']
        )

    @staticmethod
    def is_displayed(player: Player):
        if player.timerest < 301:
            player.timerest1 = 0
        return player.timerest1 > 300


class Befor(Page):
    form_model = 'player'
    form_fields = ['currentTime', 'ans', 'q']
    timeout_seconds = 20

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
            'громкая - правда - медленно',
            'холодная - зелень - мутная',
            'толковый - книга - Даль',
            'география - туз - масштаб',
            'береста - плести - гриб',
            'клетка - лист - обложка',
            'зубной - тонкий - клубок',
            'сочный - искушение - круглый',
            'трудное - истекло - золото',
            'школа - лямка - спина',
        ]
        return dict(
            a=qw[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            qa=player.round_number,
            qb=player.participant.vars['task_rounds'][player.round_number - 1],
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['rnd2'][player.round_number - 1] = 1 * player.ans


class Cross(Page):
    form_model = 'player'
    form_fields = ['randomTime']


class Beforans(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.ans

    form_model = 'player'
    form_fields = ['ans1']
    timeout_seconds = 6

    @staticmethod
    def vars_for_template(player: Player):
        qw1 = ['и', 'а', 'з', 'в', 'ж', 'т', 'с', 'г', 'и', 'в']
        qw2 = ['в', 'б', 'ж', 'г', 'б', 'у', 'з', 'к', 'п', 'ф']
        qw3 = ['к', 'к', 'и', 'с', 'з', 'ф', 'в', 'з', 'р', 'з']
        qw4 = ['с', 'д', 'к', 'т', 'н', 'в', 'г', 'с', 'с', 'с']
        qw1 = ['п', 'а', 'п', 'к', 'к', 'т', 'н', 'а', 'а', 'п']
        qw2 = ['р', 'б', 'р', 'л', 'л', 'г', 'о', 'с', 'б', 'р']
        qw3 = ['г', 'в', 'г', 'м', 'м', 'к', 'в', 'я', 'в', 'к']
        qw4 = ['к', 'г', 'к', 'н', 'н', 'п', 'т', 'г', 'г', 'к']
        return dict(
            a1=qw1[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a2=qw2[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a3=qw3[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a4=qw4[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['aans1'][player.round_number - 1] = player.ans1


class Afterans(Page):
    form_model = 'player'
    form_fields = ['ans2']
    timeout_seconds = 6

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
            'громкая - правда - медленно',
            'холодная - зелень - мутная',
            'толковый - книга - Даль',
            'география - туз - масштаб',
            'береста - плести - гриб',
            'клетка - лист - обложка',
            'зубной - тонкий - клубок',
            'сочный - искушение - круглый',
            'трудное - истекло - золото',
            'школа - лямка - спина',
        ]
        qw1 = ['и', 'а', 'з', 'в', 'ж', 'т', 'с', 'г', 'и', 'в']
        qw2 = ['в', 'б', 'ж', 'г', 'б', 'у', 'з', 'к', 'п', 'ф']
        qw3 = ['к', 'к', 'и', 'с', 'з', 'ф', 'в', 'з', 'р', 'з']
        qw4 = ['с', 'д', 'к', 'т', 'н', 'в', 'г', 'с', 'с', 'с']
        qw1 = ['п', 'а', 'п', 'к', 'к', 'т', 'н', 'а', 'а', 'п']
        qw2 = ['р', 'б', 'р', 'л', 'л', 'г', 'о', 'с', 'б', 'р']
        qw3 = ['г', 'в', 'г', 'м', 'м', 'к', 'в', 'я', 'в', 'к']
        qw4 = ['к', 'г', 'к', 'н', 'н', 'п', 'т', 'г', 'г', 'к']
        return dict(
            a=qw[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a1=qw1[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a2=qw2[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a3=qw3[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a4=qw4[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['aans2'][player.round_number - 1] = player.ans2


class Res(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.ans

    form_model = 'player'
    form_fields = ['b1']
    timeout_seconds = 6

    @staticmethod
    def vars_for_template(player: Player):
        qa1 = [
            'йти',
            'корона',
            'елт',
            'голова',
            'близкий',
            'войти',
            'встреча',
            'гонк',
            'прыг',
            'воспоминание',
        ]
        qa1 = ['в', 'к', 'ж', 'г', 'б', 'в', 'в', 'г', 'п', 'в']
        qa2 = [
            'лев',
            'бабочка',
            'олот',
            'тыква',
            'знакомый',
            'входить',
            'сиде',
            'щщщщ',
            'щщщщ',
            'щщщщ',
        ]
        qa2 = ['с', 'б', 'з', 'т', 'з', 'в', 'с', 'щщщщ', 'щщщщ', 'щщщщ']
        qa1 = ['р', 'в', 'с', 'к', 'к', 'т', 'н', 'я', 'в', 'р']
        qa2 = ['г', 'б', 'э', 'к', 'л', 'п', 'н', 'я', 'в', 'р']
        a1 = qa1[player.participant.vars['task_rounds'][player.round_number - 1] - 1]
        a2 = qa2[player.participant.vars['task_rounds'][player.round_number - 1] - 1]
        c = 'Вашего ответа нет в числе известных нам. 0 баллов, попробуйте за вторую попытку дать более известный ответ.'
        b1 = 0
        if player.ans1:
            if a2 in player.ans1:
                c = 'Вы дали правильный ответ и получаете 3 балла. Попробуйте за второую попытку дать еще один ответ'
                b1 = 3
            if a1 in player.ans1:
                c = 'Вы дали правильный ответ и получаете 3 балла. Попробуйте за второую попытку дать еще один ответ'
                b1 = 3
        player.participant.vars['qwin'] = b1 + player.participant.vars['qwin']
        return dict(a=c, b=b1)


class Res2(Page):
    form_model = 'player'
    form_fields = ['b2']
    timeout_seconds = 12

    @staticmethod
    def vars_for_template(player: Player):
        qa1 = [
            'йти',
            'корона',
            'елт',
            'голова',
            'близкий',
            'войти',
            'встреча',
            'гонк',
            'прыг',
            'воспоминание',
        ]
        qa1 = ['в', 'к', 'ж', 'г', 'б', 'в', 'в', 'г', 'п', 'в']
        qa2 = [
            'лев',
            'бабочка',
            'олот',
            'тыква',
            'знакомый',
            'входить',
            'сиде',
            'щщщщ',
            'щщщщ',
            'щщщщ',
        ]
        qa2 = ['с', 'б', 'з', 'т', 'з', 'в', 'с', 'щщщщ', 'щщщщ', 'щщщщ']
        qa1 = ['р', 'в', 'с', 'к', 'к', 'т', 'н', 'я', 'в', 'р']
        qa2 = ['г', 'б', 'э', 'к', 'л', 'п', 'н', 'я', 'в', 'р']
        a1 = qa1[player.participant.vars['task_rounds'][player.round_number - 1] - 1]
        a2 = qa2[player.participant.vars['task_rounds'][player.round_number - 1] - 1]
        c = 'Вашего ответа нет в числе известных намю 0 баллов.'
        b1 = 0
        if player.ans2:
            if a2 in player.ans2:
                c = 'Вы дали правильный ответ и получаете 3 балла. '
                b1 = 3
            if a1 in player.ans2:
                c = 'Вы дали правильнй ответ и получаете 3 балла. '
                b1 = 3
        player.participant.vars['qwin'] = b1 + player.participant.vars['qwin']
        return dict(
            a=c,
            b=b1,
            gr=player.participant.vars['traindone'],
            ballres=player.participant.vars['trainwin'],
            qres=player.participant.vars['qwin'],
        )


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
