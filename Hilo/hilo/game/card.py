import random

class Card:
    """Responsibility: hold cards previous and next.  

    Attributes:
        newCard (int): a random number between 1 and 13
        previousCard (int): the new card turned old for a new turn.
        
    """

    def __init__(self):
        
        """Constructs a new Card.
        
        Args:
            self (card): an instance of Card.
        """
        self.previousCard = 0
        self.newCard = 0

    def randomCard(self):
        """randomly picks a number from 1 to 13
        
        Args:
            self (Card): an instance of Card.
        """
        self.newCard = random.randrange(1,14)

    def oldCard(self):
        """turns the new card into the previous card for the next turn.
        
        Args:
            self (Card): an instance of Card.
        """
        self.previousCard = self.newCard
