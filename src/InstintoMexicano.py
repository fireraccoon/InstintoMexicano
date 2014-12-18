#!usr/bin/python
#This file is the main entry point


from GoatEngine.StateMachine import StateMachine


def main():
    game = StateMachine("Plateform Jumper")
    game.init()
    #game.addState(None)
    game.run()




if __name__ == "__main__":
    main()