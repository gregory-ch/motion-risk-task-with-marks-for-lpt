import random

from otree.api import *

from . import models


author = 'Your name here'
doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'tfmri'
    players_per_group = None
    speed = 0.01
    num_rounds = 16


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
    difficulty0 = models.IntegerField()
    task0 = models.IntegerField(choices=[(0, 'Lost'), (1, 'Won')])
    difficulty01 = models.IntegerField()
    task01 = models.IntegerField(choices=[(0, 'Lost'), (1, 'Won')])
    difficulty02 = models.IntegerField()
    task02 = models.IntegerField(choices=[(0, 'Lost'), (1, 'Won')])
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
    timerest0 = models.IntegerField()
    timerest01 = models.IntegerField()


# FUNCTIONS
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_rounds + 1))
            random.shuffle(round_numbers)
            round_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
            p.participant.vars['task_rounds'] = round_numbers
            p.participant.vars['rnd2'] = [
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ]
            p.participant.vars['aans1'] = [
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
            ]
            p.participant.vars['aans2'] = [
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
            ]
            p.participant.vars['traindone'] = 0
            p.participant.vars['trainwin'] = 0
            p.participant.vars['qwin'] = 0


# PAGES
class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class DifficultyChoice0(Page):
    form_model = 'player'
    form_fields = ['difficulty0']


class DifficultyChoice01(Page):
    form_model = 'player'
    form_fields = ['difficulty01']


class DifficultyChoice02(Page):
    form_model = 'player'
    form_fields = ['difficulty02']


class Train0(Page):
    form_model = 'player'
    form_fields = ['task0', 'gamedone', 'timerest0']


class Train01(Page):
    form_model = 'player'
    form_fields = ['task01', 'gamedone1', 'timerest01']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(timerest0=30000)

    @staticmethod
    def is_displayed(player: Player):
        return player.timerest0 > 300


class Train02(Page):
    form_model = 'player'
    form_fields = ['gamedone2', 'task02']

    @staticmethod
    def vars_for_template(player: Player):
        return dict(timerest0=30000)

    @staticmethod
    def is_displayed(player: Player):
        if player.timerest0 < 301:
            player.timerest01 = 0
        return player.timerest01 > 300


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
        return dict(timerest=30000)

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
        return dict(timerest=30000)

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
    timeout_seconds = 12

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
            'клетка - лист - обложка',
            'трудное - истекло - золото',
            'день - заяц - цвет',
            'календарь - светит - ночь',
            'вечерняя - бумага - стенная',
            'горький - молочный - крем',
        ]
        tmpp = ['полет шасси военный - самолет', 'ножка вино хрусталь - бокал']
        qw = [
            'кофе - петух - гимнастика',
            'школа - лямка - спина',
            'тяжелый - урожай - рождение',
            'дождь - календарь - растущий',
            'певец - Америка - тонкий',
            'воздух - быстрый - свежий',
            'дуга - дождь - спектр',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
        ]
        qw = [
            'комната - положение - река',
            'голова - монарх - солнечный ',
            'кофе - петух - гимнастика',
            'садовая - мозг - пустая',
            'друг - город - круг',
            'дверь - доверие - быстро',
            'дуга - дождь - спектр',
            'школа - лямка - спина',
            'скакалка - пружина - мяч',
            'тяжелый - урожай - рождение',
            'клетка - лист - обложка',
            'дождь - календарь - растущий',
            'певец - Америка - тонкий',
            'воздух - быстрый - свежий',
            'вечерняя - бумага - стенная',
            'горький - молочный - крем',
        ]
        qw = [
            'комната - положение - река',
            'голова - монарх - солнечный ',
            'кофе - петух - гимнастика',
            'садовая - мозг - пустая',
            'друг - город - круг',
            'дверь - доверие - быстро',
            'дуга - дождь - спектр',
            'школа - лямка - спина',
            'скакалка - пружина - мяч',
            'тяжелый - урожай - рождение',
            'клетка - лист - обложка',
            'дождь - календарь - растущий',
            'певец - Америка - тонкий',
            'воздух - быстрый - свежий',
            'вечерняя - бумага - стенная',
            'горький - молочный - крем',
            'неожиданно - человек - улица',
            'география - игра - пластик',
            'народная - мода - тройка',
            'овал - глаз - потерять',
        ]
        qw1 = [
            'и',
            'а',
            'у',
            'в',
            'ж',
            'т',
            'р',
            'р',
            'и',
            'г',
            'ч',
            'г',
            'г',
            'с',
            'г',
            'ч',
            'в',
            'к',
            'к',
            'л',
        ]
        qw2 = [
            'в',
            'б',
            'з',
            'г',
            'б',
            'у',
            'л',
            'п',
            'п',
            'п',
            'т',
            'п',
            'в',
            'п',
            'к',
            'ш',
            'у',
            'ф',
            'п',
            'о',
        ]
        qw3 = [
            'к',
            'к',
            'к',
            'с',
            'з',
            'ф',
            'к',
            'к',
            'р',
            'м',
            'ф',
            'м',
            'н',
            'р',
            'з',
            'ф',
            'г',
            'л',
            'м',
            'з',
        ]
        qw4 = [
            'с',
            'д',
            'с',
            'т',
            'н',
            'в',
            'с',
            'д',
            'с',
            'д',
            'в',
            'д',
            'ю',
            'в',
            'с',
            'х',
            'п',
            'м',
            'г',
            'с',
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
        qw1 = [
            'и',
            'а',
            'з',
            'в',
            'ж',
            'т',
            'с',
            'г',
            'и',
            'в',
            'ф',
            'ч',
            'и',
            'и',
            'б',
            'л',
            'и',
            'г',
            'ч',
            'к',
        ]
        qw2 = [
            'в',
            'б',
            'ж',
            'г',
            'б',
            'у',
            'з',
            'к',
            'п',
            'ф',
            'в',
            'т',
            'п',
            'в',
            'с',
            'м',
            'п',
            'к',
            'ш',
            'л',
        ]
        qw3 = [
            'к',
            'к',
            'и',
            'с',
            'з',
            'ф',
            'в',
            'з',
            'р',
            'з',
            'ч',
            'ф',
            'р',
            'к',
            'з',
            'н',
            'с',
            'з',
            'ф',
            'м',
        ]
        qw4 = [
            'с',
            'д',
            'к',
            'т',
            'н',
            'в',
            'г',
            'с',
            'с',
            'с',
            'т',
            'в',
            'с',
            'с',
            'н',
            'о',
            'р',
            'с',
            'х',
            'н',
        ]
        qw1 = ['и', 'а', 'з', 'в', 'ж', 'т', 'с', 'г', 'и', 'в', 'ч', 'и', 'б', 'л', 'г', 'ч']
        qw2 = ['в', 'б', 'ж', 'г', 'б', 'у', 'з', 'к', 'п', 'ф', 'т', 'в', 'с', 'м', 'к', 'ш']
        qw3 = ['к', 'к', 'и', 'с', 'з', 'ф', 'в', 'з', 'р', 'з', 'ф', 'к', 'з', 'н', 'з', 'ф']
        qw4 = ['с', 'д', 'к', 'т', 'н', 'в', 'г', 'с', 'с', 'с', 'в', 'с', 'н', 'о', 'с', 'х']
        qw = [
            'кофе - петух - гимнастика',
            'школа - лямка - спина',
            'тяжелый - урожай - рождение',
            'дождь - календарь - растущий',
            'певец - Америка - тонкий',
            'воздух - быстрый - свежый',
            'дуга - дождь - спектр',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
        ]
        qw = [
            'комната - положение - река',
            'голова - монарх - солнечный ',
            'кофе - петух - гимнастика',
            'садовая - мозг - пустая',
            'друг - город - круг',
            'дверь - доверие - быстро',
            'дуга - дождь - спектр',
            'школа - лямка - спина',
            'скакалка - пружина - мяч',
            'тяжелый - урожай - рождение',
            'клетка - лист - обложка',
            'дождь - календарь - растущий',
            'певец - Америка - тонкий',
            'воздух - быстрый - свежий',
            'вечерняя - бумага - стенная',
            'горький - молочный - крем',
            'неожиданно - человек - улица',
            'география - игра - пластик',
            'народная - мода - тройка',
            'овал - глаз - потерять',
        ]
        qw1 = ['у', 'р', 'г', 'г', 'г', 'с', 'р', 'г', 'и', 'в', 'ч', 'и', 'б', 'л', 'г', 'ч']
        qw2 = ['з', 'п', 'п', 'п', 'в', 'п', 'л', 'к', 'п', 'ф', 'т', 'в', 'с', 'м', 'к', 'ш']
        qw3 = ['к', 'к', 'м', 'м', 'н', 'р', 'к', 'з', 'р', 'з', 'ф', 'к', 'з', 'н', 'з', 'ф']
        qw4 = ['с', 'д', 'д', 'д', 'ю', 'в', 'с', 'с', 'с', 'с', 'в', 'с', 'н', 'о', 'с', 'х']
        qw = [
            'комната - положение - река',
            'голова - монарх - солнечный ',
            'кофе - петух - гимнастика',
            'садовая - мозг - пустая',
            'друг - город - круг',
            'дверь - доверие - быстро',
            'дуга - дождь - спектр',
            'школа - лямка - спина',
            'скакалка - пружина - мяч',
            'тяжелый - урожай - рождение',
            'клетка - лист - обложка',
            'дождь - календарь - растущий',
            'певец - Америка - тонкий',
            'воздух - быстрый - свежий',
            'вечерняя - бумага - стенная',
            'горький - молочный - крем',
            'неожиданно - человек - улица',
            'география - игра - пластик',
            'народная - мода - тройка',
            'овал - глаз - потерять',
        ]
        qw1 = [
            'и',
            'а',
            'у',
            'в',
            'ж',
            'т',
            'р',
            'р',
            'и',
            'г',
            'ч',
            'г',
            'г',
            'с',
            'г',
            'ч',
            'в',
            'к',
            'к',
            'л',
        ]
        qw2 = [
            'в',
            'б',
            'з',
            'г',
            'б',
            'у',
            'л',
            'п',
            'п',
            'п',
            'т',
            'п',
            'в',
            'п',
            'к',
            'ш',
            'у',
            'ф',
            'п',
            'о',
        ]
        qw3 = [
            'к',
            'к',
            'к',
            'с',
            'з',
            'ф',
            'к',
            'к',
            'р',
            'м',
            'ф',
            'м',
            'н',
            'р',
            'з',
            'ф',
            'г',
            'л',
            'м',
            'з',
        ]
        qw4 = [
            'с',
            'д',
            'с',
            'т',
            'н',
            'в',
            'с',
            'д',
            'с',
            'д',
            'в',
            'д',
            'ю',
            'в',
            'с',
            'х',
            'п',
            'м',
            'г',
            'с',
        ]
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
            'каракатица - фиолетовый - писать',
            'клетка - лист - обложка',
            'кисть - безымянный - кольцо',
            'трудное - истекло - золото',
            'день - заяц - цвет',
            'календарь - светит - ночь',
            'олень - ветвистый - изобилие',
            'вечерняя - бумага - стенная',
            'горький - молочный - крем',
            'бледная - спутник -круглая',
        ]
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
            'клетка - лист - обложка',
            'трудное - истекло - золото',
            'день - заяц - цвет',
            'календарь - светит - ночь',
            'вечерняя - бумага - стенная',
            'горький - молочный - крем',
        ]
        qw1 = [
            'и',
            'а',
            'з',
            'в',
            'ж',
            'т',
            'с',
            'г',
            'и',
            'в',
            'ф',
            'ч',
            'и',
            'и',
            'б',
            'л',
            'и',
            'г',
            'ч',
            'к',
        ]
        qw2 = [
            'в',
            'б',
            'ж',
            'г',
            'б',
            'у',
            'з',
            'к',
            'п',
            'ф',
            'в',
            'т',
            'п',
            'в',
            'с',
            'м',
            'п',
            'к',
            'ш',
            'л',
        ]
        qw3 = [
            'к',
            'к',
            'и',
            'с',
            'з',
            'ф',
            'в',
            'з',
            'р',
            'з',
            'ч',
            'ф',
            'р',
            'к',
            'з',
            'н',
            'с',
            'з',
            'ф',
            'м',
        ]
        qw4 = [
            'с',
            'д',
            'к',
            'т',
            'н',
            'в',
            'г',
            'с',
            'с',
            'с',
            'т',
            'в',
            'с',
            'с',
            'н',
            'о',
            'р',
            'с',
            'х',
            'н',
        ]
        qw1 = ['и', 'а', 'з', 'в', 'ж', 'т', 'с', 'г', 'и', 'в', 'ч', 'и', 'б', 'л', 'г', 'ч']
        qw2 = ['в', 'б', 'ж', 'г', 'б', 'у', 'з', 'к', 'п', 'ф', 'т', 'в', 'с', 'м', 'к', 'ш']
        qw3 = ['к', 'к', 'и', 'с', 'з', 'ф', 'в', 'з', 'р', 'з', 'ф', 'к', 'з', 'н', 'з', 'ф']
        qw4 = ['с', 'д', 'к', 'т', 'н', 'в', 'г', 'с', 'с', 'с', 'в', 'с', 'н', 'о', 'с', 'х']
        qw = [
            'кофе - петух - гимнастика',
            'школа - лямка - спина',
            'тяжелый - урожай - рождение',
            'дождь - календарь - растущий',
            'певец - Америка - тонкий',
            'воздух - быстрый - свежий',
            'дуга - дождь - спектр',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
            '19',
            '20',
        ]
        qw1 = ['у', 'р', 'г', 'г', 'г', 'с', 'р', 'г', 'и', 'в', 'ч', 'и', 'б', 'л', 'г', 'ч']
        qw2 = ['з', 'п', 'п', 'п', 'в', 'п', 'л', 'к', 'п', 'ф', 'т', 'в', 'с', 'м', 'к', 'ш']
        qw3 = ['к', 'к', 'м', 'м', 'н', 'р', 'к', 'з', 'р', 'з', 'ф', 'к', 'з', 'н', 'з', 'ф']
        qw4 = ['с', 'д', 'д', 'д', 'ю', 'в', 'с', 'с', 'с', 'с', 'в', 'с', 'н', 'о', 'с', 'х']
        qw = [
            'комната - положение - река',
            'голова - монарх - солнечный ',
            'кофе - петух - гимнастика',
            'садовая - мозг - пустая',
            'друг - город - круг',
            'дверь - доверие - быстро',
            'дуга - дождь - спектр',
            'школа - лямка - спина',
            'скакалка - пружина - мяч',
            'тяжелый - урожай - рождение',
            'клетка - лист - обложка',
            'дождь - календарь - растущий',
            'певец - Америка - тонкий',
            'воздух - быстрый - свежий',
            'вечерняя - бумага - стенная',
            'горький - молочный - крем',
            'неожиданно - человек - улица',
            'география - игра - пластик',
            'народная - мода - тройка',
            'овал - глаз - потерять',
        ]
        qw1 = [
            'и',
            'а',
            'у',
            'в',
            'ж',
            'т',
            'р',
            'р',
            'и',
            'г',
            'ч',
            'г',
            'г',
            'с',
            'г',
            'ч',
            'в',
            'к',
            'к',
            'л',
        ]
        qw2 = [
            'в',
            'б',
            'з',
            'г',
            'б',
            'у',
            'л',
            'п',
            'п',
            'п',
            'т',
            'п',
            'в',
            'п',
            'к',
            'ш',
            'у',
            'ф',
            'п',
            'о',
        ]
        qw3 = [
            'к',
            'к',
            'к',
            'с',
            'з',
            'ф',
            'к',
            'к',
            'р',
            'м',
            'ф',
            'м',
            'н',
            'р',
            'з',
            'ф',
            'г',
            'л',
            'м',
            'з',
        ]
        qw4 = [
            'с',
            'д',
            'с',
            'т',
            'н',
            'в',
            'с',
            'д',
            'с',
            'д',
            'в',
            'д',
            'ю',
            'в',
            'с',
            'х',
            'п',
            'м',
            'г',
            'с',
        ]
        return dict(
            a=qw[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a1=qw1[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a2=qw2[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a3=qw3[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
            a4=qw4[player.participant.vars['task_rounds'][player.round_number - 1] - 1],
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.participant.vars['aans2'][
            player.participant.vars['task_rounds'][player.round_number - 1] - 1
        ] = player.ans2


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
        qa1 = [
            'в',
            'к',
            'ж',
            'г',
            'б',
            'в',
            'в',
            'г',
            'п',
            'в',
            'ч',
            'т',
            'п',
            'в',
            'б',
            'л',
            'р',
            'г',
            'ш',
            'л',
        ]
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
        qa2 = [
            'с',
            'б',
            'з',
            'т',
            'з',
            'в',
            'с',
            'щщщщ',
            'щщщщ',
            'щщщщ',
            'ч',
            'т',
            'п',
            'в',
            'с',
            'м',
            'р',
            'г',
            'ш',
            'л',
        ]
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
        qa1 = [
            'в',
            'к',
            'ж',
            'г',
            'б',
            'в',
            'в',
            'г',
            'п',
            'в',
            'ч',
            'т',
            'п',
            'в',
            'б',
            'л',
            'р',
            'г',
            'ш',
            'л',
        ]
        qa2 = [
            'с',
            'б',
            'з',
            'т',
            'з',
            'в',
            'с',
            'щщщщ',
            'щщщщ',
            'щщщщ',
            'ч',
            'т',
            'п',
            'в',
            'с',
            'м',
            'р',
            'г',
            'ш',
            'л',
        ]
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
    @staticmethod
    def is_displayed(player: Player):
        return player.ans

    form_model = 'player'
    form_fields = ['ans1r']


class Q2(Page):
    form_model = 'player'
    form_fields = ['ans2r']


class start(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Results(Page):
    pass


page_sequence = [
    start,
    DifficultyChoice0,
    Train0,
    DifficultyChoice01,
    Train01,
    DifficultyChoice,
    Train,
    DifficultyChoice1,
    Train1,
    DifficultyChoice2,
    Train2,
]
