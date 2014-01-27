#ifndef ENGINE_STATES_IN_GAMES_TATE_HPP
#define ENGINE_STATES_IN_GAME_STATE_HPP


/*- STL -INCLUDES */
#include <iostream>


/*- SFML INCLUDES -*/
#include "SFML\Graphics.hpp"


/*- PROJECT INCLUDES -*/
#include "../GameState.hpp"
#include "../../Maps/TileMap.hpp"
#include "../../Player.hpp"



class InGameState : public GameState
{
public:
	InGameState();
	~InGameState();


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

private:
	TileMap m_map;
	sf::View m_view;



	Player m_player;

	sf::Clock m_frameTime;



};

#endif //ENGINE_STATES_INGAMESTATE_HPP