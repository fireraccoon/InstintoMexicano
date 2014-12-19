from abc import ABCMeta
from abc import abstractmethod

import pygame

from GoatEngine import Config


class StateMachine():
    def __init__(self, title):
        self.isRunning = False  # Whether or not the engine is running
        self.states = []  # A list of states

        self.clock = None   # The FPS Clock
        self.screen = None  # The screen (Pygame Surface Object)
        self.title = title  # The title of the Window

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

        # Clocks
        self.clock = pygame.time.Clock()

        # Graphical Interface
        StateMachine.log("Init::GUI Initialisation")
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode([Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT])

        # DETECT VIDEO MODES
        #modes = pygame.display.list_modes(16)
        #if not modes:
        #    StateMachine.log('16bit not supported')
        #else:
        #    StateMachine.log('Found Resolution:')
        #    pygame.display.set_mode(modes[1], pygame.FULLSCREEN, 16)

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

        try:
            self.states[-1].handleEvents(self, pygame.event.get())
        except IndexError:
            raise EmptyMachineException("State Machine has no event in queue")

    def update(self, delta):
        """ Update logic for the current state
        :param delta: delta time
        """
        try:
            self.states[-1].update(self, delta)
        except IndexError:
            raise EmptyMachineException("State Machine has no event in queue")

    def draw(self):
        """ Renders graphics for the current state
        """

        self.screen.fill((0, 0, 0))
        try:
            self.states[-1].draw(self)
        except IndexError:
            raise EmptyMachineException("State Machine has no event in queue")

        if Config.DISPLAY_FRAME_RATE:
            self.drawText("FPS: {0:.2f}".format(self.clock.get_fps()))

        pygame.display.flip()  # Update Screen

    def drawText(self, text, x=20, y=20):
        """ Renders text on screen
        :param text: the text to display
        """
        font = pygame.font.SysFont('Arial', 18, bold=True)
        surface = font.render(text, True, (255, 255, 255))
        self.screen.blit(surface, (x, y))

    def run(self):
        """ Puts the engine in its mainloop
        """
        while self.isRunning:

            self.lastTick = pygame.time.get_ticks()

            self.handleEvents()

            self.update(self.lastTick)

            self.draw()
            self.clock.tick(Config.FRAMES_PER_SECONDS)

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
    def update(self, engine, delta):
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


################
# EXCEPTIONS
################

class EmptyMachineException(Exception):
    """ Raised when the StateMachine is Empty (having no state in its list)
    """
    def __init__(self, arg):
        self.msg = arg

    def __str__(self):
        return repr(self.msg)
