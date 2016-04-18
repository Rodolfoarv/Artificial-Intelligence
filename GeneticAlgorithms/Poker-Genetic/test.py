from deuces import Card, Evaluator, Deck
# create a card
evaluator = Evaluator()
deck = Deck()
board = deck.draw(5)
player1_hand = deck.draw(5)
player2_hand = deck.draw(5)

print "The board:"
Card.print_pretty_cards(board)

print "Player 1's cards:"
Card.print_pretty_cards(player1_hand)

print "Player 2's cards:"
Card.print_pretty_cards(player2_hand)

p1_score = evaluator.evaluate(board, player1_hand)
p2_score = evaluator.evaluate(board, player2_hand)

print (p1_score)
