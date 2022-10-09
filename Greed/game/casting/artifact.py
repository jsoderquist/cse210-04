from game.casting.actor import Actor

class Artifact(Actor):
    """A visible, unmovable object with a message 
    
    The responsibility of Artifact is keep track of its message. It is also 
    a child of the Actor class and tracks its location.

    Attributes:
        All attributes of the class Actor
        message (string): a message to be displayed when the robot moves to Artifact's position
    """

    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._message = ""

    def set_message(self, message):
        """Sets Artifact's message"""
        self._message = message
    
    def get_message(self):
        """gets Artifact's message"""
        return self._message
