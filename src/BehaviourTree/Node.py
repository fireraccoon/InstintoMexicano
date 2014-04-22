

class State:
    INVALID = 0  # Needs a precondition
    SUCCESS = 1  # Success at executing
    FAILED = 2   # Failed at executing
    RUNNING = 3  # Has not finished yet


class Node:
    def __init__(self):
        self.state = None
        self.blackboard = {} #Dictionnary

    def update(self):
        return 0

    def precondition(self):
        return True

    def on_initialize(self):
        pass

    def on_terminate(self, state):
        pass

    def tick(self):
        if not self.precondition():
            return State.FAILED

        if self.state == State.INVALID:
            self.on_initialize()

        state = self.update()

        if state != State.RUNNING:
            self.on_terminate(state)
        return state

