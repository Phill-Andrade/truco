from src.utils.constants import VALUE_CARD, SUIT


def generate_deck():
    deck = list()
    for value in VALUE_CARD:
        for icon in SUIT:
            deck.append(value + icon)
    return deck
