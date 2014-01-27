#ifndef ENGINE_ENGINE_HPP
#define ENGINE_ENGINE_HPP

/*- STL INCLUDES -*/
#include <iostream>
#include <vector>

/*- PROJECT INCLUDE -*/
#include <SFML\Graphics\RenderWindow.hpp>
#include "ResourceManager.hpp"



//forward declaration
class GameState;

class Engine
{
public:
	Engine();
	~Engine();

	void static exitWithError(const std::string &error) 
	{
		Log::error(error);
		std::cin.ignore();
		std::cin.get();

		exit(EXIT_FAILURE);
	}




	void init();
	void cleanUp();

	//Manage Games states
	void changeState(GameState* state);

	void addState(GameState* state);
	
	void handleEvents();
	void update();
	void draw();



	/*
	* Deletes the last GameState in the Stack
	*/
	void popState();

	
	bool isRunning() { return m_isRunning;}
	void quit();



	//The Render Window,and yeah, it is public...
	sf::RenderWindow screen; 


	ResourceManager* resourceManager(){ return &m_resMgr; }

private:

	std::vector<GameState*> m_states; // A Stack of GameStates 
	bool m_isRunning; //Specifies if the Engine (the Game) is running or not

	

	//Managers
	ResourceManager m_resMgr;

	






};

#endif