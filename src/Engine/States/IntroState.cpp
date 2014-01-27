#include "IntroState.hpp"

//Instanciation
/*IntroState IntroState::m_instance; //Singleton pattern*/


IntroState::IntroState()
{

}


IntroState::~IntroState()
{
	
}


void IntroState::init(Engine* engine){

	//Load Splash Screen
	engine->resourceManager()->textures()->addDirectory("data/");
	m_splash = engine->resourceManager()->textures()->get("dude.png");
	
	m_background.setTexture(m_splash,true);

	m_alpha = sf::Color( 0, 0, 0, 255 );

	m_fader.setFillColor(m_alpha);
	m_fader.setSize( static_cast<sf::Vector2f>( m_splash.getSize() ) );


	std::cout << "IntroState Init" << std::endl;
}

void IntroState::cleanUp(){

}

void IntroState::pause(){

}

void IntroState::resume(){

}

void IntroState::handleEvents(Engine* engine){

	sf::Event event;
	while(engine->screen.pollEvent(event))
	{
		
		switch(event.type)
		{

			case sf::Event::Closed :
				engine->quit();

			case sf::Event::KeyPressed:

				if(event.key.code == sf::Keyboard::Return)
					engine->changeState(new InGameState());
				break;

			default:
				break;

		}
	}


}

void IntroState::update(Engine* engine){

	

	
	if(m_alpha.a != 0)
		m_alpha.a--;

	m_fader.setFillColor(m_alpha);

	/*sf::Sprite sprite;
	sprite.setTexture(m_splash);
	engine->screen.draw(sprite);*/

}

void IntroState::draw(Engine* engine){

	engine->screen.clear();

	engine->screen.draw(m_background);
	if(m_alpha.a != 0)
		engine->screen.draw(m_fader);

	engine->screen.display();


}

void IntroState::changeState(Engine* engine, GameState* state){


}