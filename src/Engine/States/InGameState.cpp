#include "InGameState.hpp"


InGameState::InGameState()
{
}


InGameState::~InGameState()
{
}




/*
* Init the GameState
*/
void InGameState::init(Engine* engine){


	int height = 6;
	int width = 26;
	m_map.load("Map1.Gmap_config", *engine->resourceManager());

	//sf::FloatRect visibleArea(0,0, engine->screen.getSize().x, engine->screen.getSize().y);
	//m_view.reset(visibleArea);


	//m_view.setViewport(sf::FloatRect(0.0f,0.0f,1.0f,1.5f));


	m_view.reset(sf::FloatRect(0,0, engine->screen.getSize().x, engine->screen.getSize().y));

	m_player.init(sf::Vector2f(10,10),sf::Vector2f(20,20),sf::Color::Blue);

	engine->screen.setView(m_view);


	Log::debug("In Game State: Init");


}

/*
* Unload the ressources
*/
void InGameState::cleanUp(){

}


/*
* Pause the GameState
*/
void InGameState::pause(){

	

}

/*
* Resume the GameState
*/
void InGameState::resume(){


}


void InGameState::handleEvents(Engine* engine){
	sf::Event event;
	while(engine->screen.pollEvent(event))
	{
		
		switch(event.type)
		{

			case sf::Event::Closed :
				engine->quit();
				break;

			case sf::Event::KeyPressed:
			{
				if(event.key.code == sf::Keyboard::Escape)
					engine->quit();


				if(event.key.code == sf::Keyboard::Down)
					int i = 0;
				if(event.key.code == sf::Keyboard::Up)
					int i = 0;

				if(event.key.code == sf::Keyboard::Right)
					int i = 0;
				if(event.key.code == sf::Keyboard::Left)
					int i = 0;



				break;
			}



			default:
				break;

		}
	}

}

void InGameState::update(Engine* engine){

	m_player.rect.setFillColor(sf::Color::Blue);

	sf::Vector2f InitialPos = m_player.rect.getPosition();


	//MOVE CHARACTER
	m_player.direction = Player::NONE;

    if(sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
    {
		m_player.rect.move(1.0f,0);
		m_player.direction = Player::RIGHT;
    }
	else if(sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
    {
		m_player.rect.move(-1.0f,0);
		m_player.direction = Player::LEFT;
    }
	else if(sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
    {
		m_player.rect.move(0,-1.0f);
		m_player.direction = Player::UP;
    }
	else if(sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
    {
		m_player.rect.move(0,1.0f);
		m_player.direction = Player::DOWN;
    }
	else
	{
		
	}

	m_player.update();
	
	
	m_player.rect.move(0,1.0f); //Gravity

	//Out of bounds
	
	int x = m_player.rect.getPosition().x/64; //tile sizes are 64*64
	int y = m_player.rect.getPosition().y/64;

	if(x < 0)
		m_player.rect.setPosition(0,y*64);
	if(y < 0)
		m_player.rect.setPosition(x*64,0);



	//Collision
	//get forward facing edge of AABB




	std::cout << "(" << x << "," << y << ")";
	std::cout << " ====> " << (m_map.m_tiles[ x + y * m_map.m_width ].getSymbol()) << std::endl;

	if(m_map.getTileID(m_player.rect.getPosition()).isSolid()){
		if(m_map.getTileID(m_player.rect.getPosition()).isCollision(m_player.rect.getPosition()))
			m_player.rect.setPosition(InitialPos);
	}



	m_frameTime.restart();


	//Keep the view centered on the player
	m_view.setCenter(m_player.rect.getPosition());
	engine->screen.setView(m_view); //reatribute the view


	
}

void InGameState::draw(Engine* engine){
	engine->screen.clear();
	//TODO draw background
	engine->screen.draw(m_map);
	engine->screen.draw(m_player.rect);
	engine->screen.display();
}
	 
void InGameState::changeState(Engine* engine, GameState* state){

}