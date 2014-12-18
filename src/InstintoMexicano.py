#!usr/bin/python
#This file is the main entry point


from GoatEngine.Engine import StateMachine, GameState


def main():
    game = StateMachine("Instinto Mexicano")
    game.init()
    game.addState(GameState())
    game.run()




if __name__ == "__main__":
    main()