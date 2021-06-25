from src import preparation

deck = preparation.generate_deck()
player = preparation.generate_player(4)
teams = preparation.generate_team(2)
preparation.distribute_team(teams, player)
starter = preparation.starter_player(player)
preparation.order_player(starter, player)
preparation.turn_manilha(deck)
