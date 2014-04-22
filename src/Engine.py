import pygame


class Engine():
    def __init__(self, title, verbose=False):
        self.verbose = verbose
        self.isRunning = False

        self.states = [] # A list of states
        self.clock = None

        self.screen = None
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 640
        self.title = title



    def log(self, message):
         if self.verbose:
            print("Game Engine " + message)

    def init(self):
        self.log("Init")
        pygame.init()
        self.isRunning = True
        self.clock = pygame.time.Clock()

        # Graphical Interface
        self.log("Init::GUI Initialisation")
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        pygame.display.set_caption(self.title)



    def cleanUp(self):
        self.log("Cleaning up...")

    def exit(self):
        self.log("Exiting...")
        self.isRunning = False

    def exitWithError(self, errorMessage):
        exit(errorMessage)



    def changeState(self, newState):
        """ Kills the current state if any and switch to the new one """
        if self.states:
            self.states[-1].cleanUp(self)
            self.states.pop() #delete the last state

        self.states.append(newState)
        self.states[-1].init(self)


    def addState(self, newState):
        """ Pauses the current state if any and switch to the new one """
        if self.states:
            self.states[-1].pause(self)

        self.states.append(newState)
        self.states[-1].init(self)


    def popState(self):
        """  Kills the current state and switch to the las one remaining if any """
        if self.states:
            self.states[-1].cleanUp(self)
            self.states.pop()

        if self.states:
            self.states[-1].resume(self)

    # ================================ LOOP ====================================================#
    def handleEvents(self):
        if self.states:
            self.states[-1].handleEvents(self, pygame.event.get())
        else:
            self.exitWithError("has no event in queue")

    def update(self):
        if self.states:
            self.states[-1].update(self)

        else:
            self.exitWithError("has no event in queue")

    def draw(self):
        if self.states:
            self.states[-1].draw(self)
        else:
            self.exitWithError("has no event in queue")



    def run(self):
        while self.isRunning:
            self.handleEvents()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
