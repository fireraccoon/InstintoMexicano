/////////////////////////////////////////////////////////////////////////////////
//  
//  Instinto Mexicano
//  Copyright (C) 2013 Team G.O.A.T
//  This program is free software; you can redistribute it and/or
//  modify it under the terms of the GNU General Public License
//	as published by the Free Software Foundation; either version 2
//	of the License, or (at your option) any later version.
//
//	This program is distributed in the hope that it will be useful,
//	but WITHOUT ANY WARRANTY; without even the implied warranty of
//	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//	GNU General Public License for more details.
//
//	You should have received a copy of the GNU General Public License
//	along with this program; if not, write to the Free Software
//	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
//  
//  Nom:    	 GameObject
//  Auteur:      Cesare James
//  Description: Contains a base class for all game objects.
//
//
/////////////////////////////////////////////////////////////////////////////////

#ifndef GAME_OBJECT_HPP
#define GAME_OBJECT_HPP

/*SFML INCLUDE */
#include <SFML\Graphics.hpp>

/* PROJECT INCLUDE */


class GameObject : public sf::Drawable, sf::Transformable
{
public:
	//Mvnt Direction
	enum Direction {UP,DOWN,LEFT,RIGHT};
	
	/* ctor & dtor */

	GameObject(arguments);
	~GameObject();

   	/*
   	* Draws the gameobject on screen
   	*/
	virtual void draw() =0;
	virtual Position move() =0;
	/*
	* Handles the collisions with the other GameObjects
	*/
	virtual void collision() =0;



protected:
	float m_height;		 //It's height
	float m_width;		 //It's width
	
	sf::Vector2f m_position; //The GameObject position
	
	sf::FloatRect m_boundingBox; //The GameObject boundingBox
	
	
	sf::Sprite m_sprite*;	//We use a pointer since all the sprites are contained by SpriteManager
	float m_currentFrame;	//The current Frame
	
	


};
#endif
