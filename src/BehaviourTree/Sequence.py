"""
* Child are evaluated one by one (from left to right)
* When it is finished, the next one is validated and executed
* If one fails, the Sequence fails
*
* SUCCESS : all children return SUCCESS
* FAILED  : as soon as any of the children returns FAILURE
* RUNNING : as soon as any of the children returns RUNNING
"""
from BehaviourTree.Composite import Composite
from BehaviourTree.Node import State


class Sequence(Composite):
    def __init__(self):
        Composite.__init__(self)
        self.current_node = 0

    def update(self):
        state = State.RUNNING
        while state == State.RUNNING:
            state = self.children[self.current_node].tick()
            if state is not State.SUCCESS:
                self.current_node = 0
                return state

            if (self.current_node+1) is not len(self.children):
                self.current_node += 1
            else:
                break

        return State.SUCCESS
