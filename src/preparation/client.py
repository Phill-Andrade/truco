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


def distribute_team(players):
    teams = dict()
    for team in teams:
        for player in players:
            if int(team[-1]) % 2 == 1:
                if int(player[-1]) % 2 == 1:
                    teams['team_1'].append(player)

            elif int(team[-1]) % 2 == 0:
                if int(player[-1]) % 2 == 0:
                    teams['team_2'].append(player)
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


def turn_manilha(deck, value_card):
    choice_manilha = deck.index(random.choice(deck))
    upset = deck.pop(choice_manilha)
    index_suit = upset[1]
    index_value = value_card.index(upset[0])
    if int(index_value) < 9:
        index_value = index_value + 1
    elif int(index_value) == 9:
        index_value = 0
    manilha = str(value_card[index_value]) + index_suit
    return manilha, upset


def distribute_card(deck, players):
    for player in players:
        for draw in range(3):
            choice_card = deck.index(random.choice(deck))
            cards = deck.pop(choice_card)
            players[player].append(cards)


def game_preparation():
    deck = generate_deck()
    players = generate_player(4)
    distribute_team(players)
    starter = starter_player(players)
    order = order_player(starter, players)
    manilha, upset = turn_manilha(deck, VALUE_CARD)
    distribute_card(deck, players)
    return players, order, manilha, upset
