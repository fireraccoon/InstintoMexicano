"""
*  check which child to run in priority order until the
*  first one succeeds or returns that it is running.
*  Order of child counts
*
*  SUCCESS : as soon as any of the children returns SUCCESS
*  FAILED  : if all children return FAILED
*  RUNNING : as soon as any of the children returns RUNNING
"""

from BehaviourTree.Composite import Composite
from BehaviourTree.Node import State


class Selector(Composite):
    def __init__(self):
        Composite.__init__(self)

        self.current_node = 0

    def update(self):
        state = State.RUNNING

        while state == State.RUNNING:
            state = self.children[self.current_node].tick()

            if state == State.SUCCESS or state == State.RUNNING:
                self.current_node = 0 #reset
                return state

            if (self.current_node+1) is not len(self.children):
                self.current_node += 1
            else:
                break

        return State.FAILED
