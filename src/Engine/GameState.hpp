#ifndef ENGINE_GAMESTATE_HPP
#define ENGINE_GAMESTATE_HPP

/*- PROJECT INCLUDES -*/
#include "Engine.hpp"



class GameState
{
public:


	/*
	* Init the GameState
	*/
	virtual void init(Engine* engine=NULL)=0;

	/*
	* Unload the ressources
	*/
	virtual void cleanUp()=0;


	/*
	* Pause the GameState
	*/
	virtual void pause()=0;

	/*
	* Resume the GameState
	*/
	virtual void resume()=0;

	virtual void handleEvents(Engine* engine)=0;

	virtual void update(Engine* engine)=0;
	virtual void draw(Engine* engine)=0;

	void changeState(Engine* engine, GameState* state){ engine->changeState(state); }


protected:


};

#endif