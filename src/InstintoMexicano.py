#!usr/bin/python



from GoatEngine import Engine
from Levels.Level_02 import Level




def main():
    game = Engine("Plateform Jumper", True)

    game.init()
    game.addState(Level())
    game.run()




if __name__ == "__main__":
    main()