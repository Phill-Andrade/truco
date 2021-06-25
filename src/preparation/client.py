import random

from src.utils.constants import SUIT, VALUE_CARD


def generate_deck():
    deck = list()
    for value in VALUE_CARD:
        for icon in SUIT:
            deck.append(value + icon)
    return deck


def generate_player(qty_players):
    players = dict()
    for num in range(qty_players):
        key = 'player_' + str(num + 1)
        players[key] = []
    return players


def generate_team(qty_teams=2):
    teams = dict()
    for num in range(qty_teams):
        key = 'team_' + str(num + 1)
        teams[key] = []
    return teams


def distribute_team(teams, players):
    for team in teams:
        for player in players:
            if int(team[-1]) % 2 == 1:
                if int(player[-1]) % 2 == 1:
                    teams[team].append(player)

            elif int(team[-1]) % 2 == 0:
                if int(player[-1]) % 2 == 0:
                    teams[team].append(player)
    return teams


def starter_player(players):
    player = list(players.keys())
    starter = random.choice(player)
    return starter


def order_player(starter, players):
    init_player = int(starter[-1])
    total = len(players)
    order = list()
    for player in range(total):
        if total >= init_player + player:
            starter = 'player_' + str(init_player + player)
            order.append(starter)
        else:
            starter = 'player_' + str(init_player + player - total)
            order.append(starter)
    return order


def turn_manilha(deck):
    choice_manilha = deck.index(random.choice(deck))
    manilha = deck.pop(choice_manilha)
    return manilha


def distribute_card(deck, players):
    for player in players:
        for draw in range(3):
            choice_card = deck.index(random.choice(deck))
            cards = deck.pop(choice_card)
            players[player].append(cards)
