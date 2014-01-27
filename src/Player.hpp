#pragma once

#include <SFML\Graphics.hpp>


#include <alg.h>


class Player
{
public:
	enum Direction{ LEFT, RIGHT, DOWN, UP, NONE};

	Direction direction;

	sf::RectangleShape rect;
	float bottom, left, right, top; //AABB bonding box
	std::vector<sf::Vector2i> tiles; //the tiles the player is touching

	void init(sf::Vector2f position, sf::Vector2f size, sf::Color color){
		rect.setPosition(position);
		rect.setSize(size);
		rect.setFillColor(color);
	}

	void update(){

		//the sides
		bottom = rect.getPosition().y + rect.getSize().y;
		left = rect.getPosition().x;
		right = rect.getPosition().x+rect.getSize().x;
		top = rect.getPosition().y;

		//get the corners (this implies the rect is 32 pixels)
		sf::Vector2i topLeft(sf::Vector2i((int)left/32, (int)top /32));
		sf::Vector2i topRight(sf::Vector2i((int)right/32, (int)top /32));
		sf::Vector2i bottomLeft(sf::Vector2i((int)left/32, (int)bottom /32));
		sf::Vector2i bottomRight(sf::Vector2i((int)right/32, (int)bottom /32));


		tiles.clear();

		tiles.push_back(topLeft);
		if(std::find(tiles.begin(), tiles.end(), topRight) == tiles.end()) tiles.push_back(topRight);
		if(std::find(tiles.begin(), tiles.end(), bottomLeft) == tiles.end()) tiles.push_back(bottomLeft);
		if(std::find(tiles.begin(), tiles.end(), topRight) == tiles.end()) tiles.push_back(topRight);


	}

	Player();
	~Player();
};

