from gameSetup import Deck, Card

# Calculating the current value on a given array of Card objects
def getHandValue(hand):

    handValue = 0
    aceCounter = 0

    for card in hand:
        if card.value in ["J", "Q", "K"]:
            handValue += 10
        elif card.value == "A":
            aceCounter += 1
        else:
            handValue += int(card.value)
    
    while aceCounter > 0:
        if handValue > 11:
            handValue += 1
        else:
            handValue += 11
        aceCounter -= 1

    
    return handValue

def playAgain(bal):
    choice = input("Do you want to play another hand?\n")

    if bal <= 0:
        print("Your balance is 0. You cannot play another game.")
        return False

    if choice not in ["y", "n"]:
        print("Please select \"y\" or \"n\".")
        playAgain()
    elif choice == "y":
        return True
    else:
        return False
    
# Game

playing = True
balance = 200

while playing:

    #Placing wager
    bet = -1
    while bet <= 0 or bet > balance:
        bet = int(input(f"Please place your bet. You current balance is: {balance}.\n"))

    # Game setup
    deck = Deck()
    deck.shuffleDeck()
    dealerCards = []
    playerCards = []
    dealerHandValue = 0
    playerHandValue = 0

    # Dealing first cards, calculating their value and showing them to the player
    playerCards.append(deck.dealCard())
    dealerCards.append(deck.dealCard())
    playerCards.append(deck.dealCard())
    dealerCards.append(deck.dealCard())
    playerHandValue = getHandValue(playerCards)
    dealerHandValue = getHandValue(dealerCards)

    if playerHandValue == 21 and dealerHandValue != 21:
        print("Blackjack!")
        print("Your hand:", [f"{card.value}{card.house}" for card in playerCards], f"\nValue: {playerHandValue}")
        print("Dealer's hand:", [f"{card.value}{card.house}" for card in dealerCards], f"\nValue: {dealerHandValue}")
        balance += 2.5 * bet
        playing = playAgain(balance)
        continue

    if playerHandValue != 21 and dealerHandValue == 21:
        print("Dealer has a Blackjack! You lost.")
        print("Your hand:", [f"{card.value}{card.house}" for card in playerCards], f"\nValue: {playerHandValue}")
        print("Dealer's hand:", [f"{card.value}{card.house}" for card in dealerCards], f"\nValue: {dealerHandValue}")
        balance -= bet
        playing = playAgain(balance)
        continue
   
    print("Your hand:", [f"{card.value}{card.house}" for card in playerCards], f"\nValue: {playerHandValue}")
    print("Dealer's hand:", [f"{dealerCards[0].value}{dealerCards[0].house}, XX"])
    while playerHandValue < 21:
        choice = input("You may hit \"h\", stand \"s\", split \"x\", or play double \"d\".\n").lower()
        if choice not in ["s", "h", "d", "x"]:
            print("Please select one of the following options.")
            continue
        else:
            match choice:
                case "s":
                    print(f"You stand. Your hand value is {playerHandValue}")
                    break
                case "d":
                    if balance < 2 * bet:
                        print(f"You cannot afford to play double. You balance is {balance} and you need {2*bet}")
                        continue
                    print("Playing double!")
                    bet += bet
                    playerCards.append(deck.dealCard())
                    playerHandValue = getHandValue(playerCards)
                    print("Your hand:", [f"{card.value}{card.house}" for card in playerCards], f"\nValue: {playerHandValue}")
                    break
                case "x":
                    print("To be implemented")
                case "h":
                    playerCards.append(deck.dealCard())
                    playerHandValue = getHandValue(playerCards)
                    print("Your hand:", [f"{card.value}{card.house}" for card in playerCards], f"\nValue: {playerHandValue}")
    
    if playerHandValue > 21:
        print("You busted!")
        balance -= bet
        print(f"Your current balance is {balance}.")
        playing = playAgain(balance)
        continue

    print("Dealer's hand:", [f"{card.value}{card.house}" for card in dealerCards], f"\nValue: {dealerHandValue}")
    while dealerHandValue < 17:
        dealerCards.append(deck.dealCard())
        dealerHandValue = getHandValue(dealerCards)
        print("Dealer's hand:", [f"{card.value}{card.house}" for card in dealerCards], f"\nValue: {dealerHandValue}")

    if dealerHandValue > 21:
        print("Dealer busted! You won.")
        balance += bet
        print(f"Your current balance is {balance}.")
        playing = playAgain(balance)
        continue
    elif dealerHandValue == playerHandValue:
        print("It is a tie! Your bet has been returned.")
        playing = playAgain(balance)
        continue
    elif dealerHandValue > playerHandValue:
        print(f"Dealer won! {dealerHandValue} > {playerHandValue}")
        balance -= bet
        playing = playAgain(balance)
        continue
    else:
        print(f"You won! {dealerHandValue} < {playerHandValue}")
        balance += bet
        playing = playAgain(balance)
        continue


print(f"Thank you for the game. You ended with a balance of {balance}. The program ends now.")