import random


def drawn_player_table(players, order):
    table = dict()
    for player in order:
        value = players[player].index(random.choice(players[player]))
        hand = players[player].pop(value)
        table[player] = hand
    return table


def check_manilha(manilha, table):
    manilha_turn = dict()
    for player, card in table.items():
        if card[0] == manilha[0]:
            manilha_turn[player] = card
    return manilha_turn


def compare_values(table, value_card):
    power_turn_card = list()
    power = 0
    for player, card in table.items():
        if value_card.index(card[0]) >= power:
            power = value_card.index(card[0])
            power_turn_card.append([player, card])
    return power_turn_card


def compare_suit(check_manilha, suit):
    power_turn_card = list()
    power = 0
    for player, card in check_manilha.items():
        if suit.index(card[1]) >= power:
            power = suit.index(card[1])
            power_turn_card.append([player, card])
    return power_turn_card


def interation_card(players, order, manilha, value_card, suit):
    table = drawn_player_table(players, order)
    checkout_manilha = check_manilha(manilha, table)
    comparation_value_card = compare_values(table, value_card)
    comparation_suit_card = compare_suit(checkout_manilha, suit)
    return checkout_manilha, comparation_value_card, comparation_suit_card
