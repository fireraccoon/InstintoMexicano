#include "Engine.hpp"
#include "GameState.hpp"

Engine::Engine()
{
}

Engine::~Engine()
{
}


void Engine::init(){


	//Load all the managers and user settings



	//Creation of the Render Window
	int width = 1024, height = width * 3/4; // Ratio 4:3
	screen.create(sf::VideoMode(width,height), "Instinto Mexicano v0.0");
	m_isRunning = true;
	//LOG
	std::cout << "GameEngine Init" << std::endl;
}

void Engine::cleanUp(){

	//Clean up all states and delete them
	while( !m_states.empty() ){
		m_states.back()->cleanUp();
		m_states.pop_back();
	}

	//Close the Window
	screen.close();
	std::cout << "GameEngine Shutting down" << std::endl;

}

//Manage Games states
void Engine::changeState(GameState* state){

	if( !m_states.empty() ){
		m_states.back()->cleanUp(); //clean up the last state
		m_states.pop_back(); //we delete it
	}

	//add the new state and start it
	m_states.push_back(state);
	m_states.back()->init(this);


}

void Engine::addState(GameState* state){

	if( !m_states.empty() ){
		m_states.back()->pause();
	}

	//add the new state and start it
	m_states.push_back(state);
	m_states.back()->init(this);

}
	
void Engine::popState(){

	if( !m_states.empty() ){
		m_states.back()->cleanUp();
		m_states.pop_back();
	}

	if( !m_states.empty() ){
		m_states.back()->resume();
	}

}


void Engine::handleEvents(){

	m_states.back()->handleEvents(this);
}

void Engine::update(){

	m_states.back()->update(this);
}

void Engine::draw(){
	m_states.back()->draw(this);
}


void Engine::quit(){
	m_isRunning = false;
}



