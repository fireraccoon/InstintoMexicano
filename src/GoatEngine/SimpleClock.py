import time


class Clock:
    """ Classe permettant d'être utilisée pour délayer une tâche
    """

    def __init__(self, delayInMs):
        self.delay = delayInMs  # in milliseconds
        self.startTime = None
        self.lastCheck = None

    def start(self):
        self.startTime = time.time()
        self.lastCheck = time.time()

    def isDone(self):
        """ Retourne si oui ou non le délais requis à été complété
        :return: True si le délais est terminé sinon False
        """
        try:
            return time.time() - self.lastCheck >= self.delay / 1000
        except TypeError:  # Le timer n'a pas été explicitement démarré
            raise ClockException("Le timer n'a pas été lancé, appeler la fonction start() explicitement")

    def getRunningTime(self):
        """ Retourne le temps en seconde depuis le début que le timer fonctionne
        :return: int temps en secondes
        """
        return int(time.time() - self.startTime)

    def reset(self):
        self.lastCheck = time.time()

    def getNow(self):
        return time.time()


class FrameClock:
    def __init__(self, delayInFrame):
        self.delay = delayInFrame
        self.startFrame = -1
        self.lastCheck = -1


    def start(self):
        self.startFrame = 0
        self.lastCheck = 0


    def isDone(self):
        """ Retourne si oui ou non le délais requis à été complété, doit etre appelé à chaque frame
        :return: True si le délais est terminé sinon False
        """
        if not (self.startFrame >= 0 and self.lastCheck >= 0):
            raise ClockException("Le timer n'a pas été lancé, appeler la fonction start() explicitement")
        self.lastCheck += 1
        return self.lastCheck - self.startFrame >= self.delay

    def reset(self):
        self.lastCheck = 0
        self.startFrame = 0





class ClockException(Exception):
    def __init__(self, msg):
        self.message = msg
        Exception.__init__(self, self.message)


# EXEMPLE UTILISATION
def exemple():
    t = Clock(1000)
    t.start()
    while 1:
        if t.isDone():
            print("Running time: %ssec" % t.getRunningTime())
            t.reset()
