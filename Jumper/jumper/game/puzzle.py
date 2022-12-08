import random

class Puzzle:
    # The word that needs to be guessed. 
    
    # The responsibility of Puzzle is to keep track of letters that have
    # been found. 
    
    # Attributes:
    #     _puzzles[]: List of 5 possible puzzles.
    #     _puzzle[]: List of letters in the puzzle
      

    def __init__(self):
        # Constructs a new Puzzle.

        # Args:
        #     self (Puzzle): An instance of Puzzle.
        
        self._puzzles = ["tomahawk", "sherman", "theory", "distance","string"]
        self._word = self._puzzles[random.randint(0, 4)]
        self._old_answers = [] 
        for i in list(self._word):
            self._old_answers.append("_")
        self._new_answers = []
        for i in list(self._word):
            self._new_answers.append("_") 
        self._letter = ""
        

    def pass_letter(self, letter):

        self._letter = letter
    
    def right_wrong(self):
        if self._word.find(self._letter) > -1:
            right = True
        elif self.word.find(self._letter) ==-1:
            right = False
        
        return right

    def track_answers(self):
    #     Whether or not the letter has been found in the puzzle.

    #     Args:
    #         self (Puzzle): An instance of Puzzle.
            
    #     Returns:
    #         boolean: True if the letter was found; false if otherwise.
        

        val = -1
        for i in self._old_answers:
            val += 1

            index = self._word.find(self._letter, val)
            
            if index > -1:
                self._new_answers[index] = self._letter

        print (self._old_answers)        
        return self._new_answers

        
    # def change_old_answers(self, new_answers):

    #     self._old_answers = new_answers

        