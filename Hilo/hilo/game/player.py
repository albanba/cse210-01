from game.card import Card;

class Player:

    """A person who directs the game. 
    
    Start the game. Decides to play and guesses if the next card
    will be higher or lower. Calculates the final score and determines 
    if lost the game or continues.

    Attributes:
        nextRound (boolean): Whether or not the game is being played. 
        cardGuess (input): the player guesses if next card will be higher or lower (h/l)
        totalScore (int): The score for the entire game.
        previousCard (int) A card to start the game
    """

    def __init__(self):

        """Constructs a new Player.
        
        Args:
            self (Player): an instance of Player.
        """
        
        self.nextRound = True
        self.totalScore = 300
        self.guessCard = ""
        self.card = Card()
        self.card.randomCard()
        self.card.oldCard()
        self.previousCard = self.card.previousCard   
        
    def startGame(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Player): an instance of Player.
        """
        
        while self.nextRound: 
            self.guess()
            self.compareCards()
            self.playAgain()
            

            

    def guess(self):

        """Provides a card and asks if the next one will be higher or lower.
        
        Args:
            self (Player): an instance of Player.
        """
        print (f"The card is: {self.previousCard}")
        self.guessCard = input("Next card higher or lower (h/l)? ")
        

    def compareCards(self):
        """Provides a new card and compares to the previous one to determine if guess was right. 
        updates the score accordingly and sets the new card as the previous one.
        
        Args:
            self (Player): an instance of Player.
        """
        self.card.randomCard()
        print (f"The next card was {self.card.newCard}")

        if self.previousCard > self.card.newCard and self.guessCard == "l":
            self.totalScore += 100
        elif self.previousCard < self.card.newCard and self.guessCard == "h":
            self.totalScore += 100
        
        elif self.previousCard < self.card.newCard and self.guessCard == "l":
            self.totalScore -= 75
        elif self.previousCard > self.card.newCard and self.guessCard == "h":
            self.totalScore -= 75
        
        self.card.oldCard()
        self.previousCard = self.card.previousCard 

    def playAgain(self):

        """Provides the score so far and determines if the game can continue.
        If the game is still on, the player can choose to quit.
        
        Args:
            self (Player): an instance of Player.
        """

        print (f"Your score is: {self.totalScore}")

        if self.totalScore <= 0:
            print("Game Over")
            self.nextRound = False


        elif self.totalScore > 0:
            self.nextRound = input("Play again? [y/n]")

            if self.nextRound == "n":
                self.nextRound = False
                print("Game Over")
            