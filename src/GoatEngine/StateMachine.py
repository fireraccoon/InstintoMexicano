from abc import ABCMeta
from abc import abstractmethod
import pygame
from GoatEngine import Config


class StateMachine():
    def __init__(self, title):
        self.isRunning = False  # Whether or not the engine is running
        self.states = []  # A list of states

        self.clock = None
        self.screen = None

        self.title = title

    @staticmethod
    def log(message):
        """ Displays in the console the engine's messages
        :param message: the message to display
        """
        if Config.ENGINE_VERBOSE:
            print("Game Engine " + message)

    def init(self):
        """ Initialises the Engine
        """
        StateMachine.log("Init")
        pygame.init()
        self.isRunning = True
        self.clock = pygame.time.Clock()

        # Graphical Interface
        StateMachine.log("Init::GUI Initialisation")
        self.screen = pygame.display.set_mode([Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT])
        pygame.display.set_caption(self.title)


    def cleanUp(self):
        """ Does necessary clean ups of the engine
        """
        StateMachine.log("Cleaning up...")

    def exit(self):
        """ Exits the engine in a clean way
        """
        StateMachine.log("Exiting...")
        self.isRunning = False

    def exitWithError(self, errorMessage):
        """ Exists the engine and the program because of an error
        :param errorMessage: The error message to display
        """
        exit(errorMessage)

    # ================================ STATE MANAGEMENT ==================================================== #
    def changeState(self, newState):
        """  KILLS [clean up] the current state if any and switch to the new one
        :param newState: The new state to put in the engine
        """
        if self.states:
            self.states[-1].cleanUp(self)
            self.states.pop()  # delete the last state

        self.states.append(newState)
        self.states[-1].init(self)


    def addState(self, newState):
        """ PAUSES the current state if any and switch to the new one
        :param newState: the new state
        """

        if self.states:
            self.states[-1].pause(self)

        self.states.append(newState)
        self.states[-1].init(self)


    def popState(self):
        """  KILLS the current state and switch to the last one remaining if any """
        if self.states:
            self.states[-1].cleanUp(self)
            self.states.pop()

        if self.states:
            self.states[-1].resume(self)

    # ================================ LOOP ==================================================== #
    def handleEvents(self):
        """ Handle user inputs for the current state
        """
        if self.states:
            self.states[-1].handleEvents(self, pygame.event.get())
        else:
            self.exitWithError("has no event in queue")

    def update(self):
        """ Update logic for the current state
        """
        if self.states:
            self.states[-1].update(self)

        else:
            self.exitWithError("has no event in queue")

    def draw(self):
        """ Renders graphics for the current state
        """
        if self.states:
            self.states[-1].draw(self)
        else:
            self.exitWithError("has no event in queue")

    def run(self):
        """ Puts the engine in its mainloop
        """
        while self.isRunning:
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()


class GameState():
    """ Represents a Game State
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def init(self, engine):
        """ Initialises the game state
        :param engine: a reference to the game Engine
        """
        pass

    @abstractmethod
    def handleEvents(self, engine, events):
        """ Handle user inputs for the current state
        :param engine: a reference to the game engine
        :param events: the capted events
        """
        pass

    @abstractmethod
    def update(self, engine):
        """ Update logic for the current state
        :param engine: a reference to the game Engine
        """
        pass

    @abstractmethod
    def draw(self, engine):
        """ Renders graphic
        :param engine: a reference to the game Engine
        """
        pass

    # These are default behaviors, so no need to make them abstract
    def cleanUp(self, engine):
        """ Cleans up the state
        :param engine: a reference to the game Engine
        """
        pass

    def resume(self, engine):
        """ Resume the engine after it was paused
        :param engine: a reference to the game Engine
        """
        pass

    def pause(self, engine):
        """ Pauses the state (called right before it is paused)
        :param engine: a reference to the game Engine
        :return:
        """
        pass

















