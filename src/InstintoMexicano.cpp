#include <iostream>
#include <string>

/* SFML INCLUDES */
#include <SFML\Graphics.hpp>


/* PROJECT INCLUDES */
#include "Application.hpp"
#include "Engine\Engine.hpp"
#include "Engine\States\IntroState.hpp"

#include "Engine\SettingParser.hpp"



int main(int argc, char* argv[])
{
  //Disable SFML output
  sf::err().rdbuf(NULL);

	/// START ///

  Engine game;
  game.init();

  game.changeState( new IntroState() );

  while(game.isRunning()){

	  game.handleEvents();
	  game.update();
	  game.draw();
  }

  game.cleanUp();


    return 0;
}