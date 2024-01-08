import random

# Function to calculate the total score of a hand
def calculate_score(hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        score -= 10
    return score

# Function to play the game
def play_game():
    # Create a deck of cards
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # 11 represents Ace

    # Shuffle the deck
    random.shuffle(deck)

    # Deal initial cards to Sam and the Dealer
    sam_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Check for blackjack in initial hands
    if calculate_score(sam_hand) == 21:
        return "Sam wins with Blackjack!"
    elif calculate_score(dealer_hand) == 21:
        return "Dealer wins with Blackjack!"

    # Sam draws cards until the total reaches 17 or higher
    while calculate_score(sam_hand) < 17:
        sam_hand.append(deck.pop())

    # Check if Sam busts (total > 21)
    sam_score = calculate_score(sam_hand)
    if sam_score > 21:
        return "Dealer wins, Sam busted!"

    # Dealer draws cards until their total is higher than Sam's
    while calculate_score(dealer_hand) <= sam_score:
        dealer_hand.append(deck.pop())

    # Check if Dealer busts (total > 21)
    dealer_score = calculate_score(dealer_hand)
    if dealer_score > 21:
        return "Sam wins, Dealer busted!"

    # Determine the winner based on the higher score
    if sam_score > dealer_score:
        return "Sam wins with a score of {}!".format(sam_score)
    elif dealer_score > sam_score:
        return "Dealer wins with a score of {}!".format(dealer_score)
    else:
        return "It's a tie!"

# Play the game
result = play_game()
print(result)
