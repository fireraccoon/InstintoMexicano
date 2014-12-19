#!usr/bin/python
#This file is the main entry point


from GoatEngine.Engine import StateMachine
from Scenes.PlayGroundScene import PlayGroundScene


def main():
    game = StateMachine("Instinto Mexicano")
    game.init()
    game.addState(PlayGroundScene())
    game.run()




if __name__ == "__main__":
    main()