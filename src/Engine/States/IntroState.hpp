#ifndef ENGINE_STATES_INTROSTATE_HPP
#define ENGINE_STATES_INTROSTATE_HPP

/*- STL -INCLUDES */
#include <iostream>



/*- SFML INCLUDES -*/
#include "SFML\Graphics.hpp"



/*- PROJECT INCLUDES -*/
#include "..\GameState.hpp"
#include "InGameState.hpp"



class IntroState : public GameState
{
public:
	/* ctor & dtor */
	 IntroState();
	~IntroState();

	
	/*
	* Init the GameState
	*/
	void init(Engine* engine);

	/*
	* Unload the ressources
	*/
	void cleanUp();


	/*
	* Pause the GameState
	*/
	void pause();

	/*
	* Resume the GameState
	*/
	 void resume();


	 void handleEvents(Engine* engine);
	 void update(Engine* engine);
	 void draw(Engine* engine);

	 void changeState(Engine* engine, GameState* state);




protected:



private:
	

	sf::Texture m_splash;
	sf::Texture m_title;
	sf::Sprite  m_background;

	sf::RectangleShape m_fader;
	sf::Color m_alpha;


};

#endif //ENGINE_STATES_INTROSTATE_HPP