from game.terminal_service import TerminalService
from game.puzzle import Puzzle
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (Puzzle): The game's puzzle.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        self._answers = []
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._terminal_service.write_text(self._puzzle._old_answers)
        self._terminal_service.write_jumper(self._jumper._jumper_tracker)
        
      
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        # Ask for a letter.

        # Args:
        #     self (Director): An instance of Director.
        
        letter = self._terminal_service.read_text("\nEnter a letter: ")
        self._puzzle.pass_letter(letter)
        
    def _do_updates(self):
    #     """Keeps watch on where the seeker is moving.

    #     Args:
    #         self (Director): An instance of Director.
    #     """
        self._answers = self._puzzle.track_answers()
        
        self._jumper.update_jumper(self._puzzle, self._answers)
       
        
        
    def _do_outputs(self):
    #     """Provides a hint for the seeker to use.

    #     Args:
    #         self (Director): An instance of Director.
    #     """
        self._terminal_service.write_text(self._answers)
       
        self._terminal_service.write_jumper(self._jumper._jumper_tracker)

