from BehaviourTree.Node import Node, State
from BehaviourTree.Selector import Selector


class EnnemyBehaviour():
    def __init__(self, gameObject, player):
        self.gameObject  = gameObject
        self.root = Selector()

        ra = RunAway()
        ra.blackboard["player"] = player
        ra.blackboard["ennemy"] = self.gameObject
        self.root.add_node(ra)



    def update(self):
        self.root.tick()




class RunAway(Node):
    def __init__(self):
        Node.__init__(self)
        self.ennemy = None


    def update(self):
        print("ok")
         # Ennemy Behaviour Fleee
        self.ennemy = self.blackboard["ennemy"]
        player = self.blackboard["player"]
        if self.ennemy.rect.x > player.rect.x:
            self.ennemy.move_right()

        if self.ennemy.rect.x < player.rect.x:
            self.ennemy.move_left()

        # Jump if ennemy on ground
        if self.ennemy.rect.y <= player.rect.y:
             self.ennemy.jump()


        return State.RUNNING



