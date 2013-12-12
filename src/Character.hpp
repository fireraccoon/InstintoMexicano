/////////////////////////////////////////////////////////////////////////////////
//
// Instinto Mexicano
// Copyright (C) 2013 Team G.O.A.T
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
//        as published by the Free Software Foundation; either version 2
//        of the License, or (at your option) any later version.
//
//        This program is distributed in the hope that it will be useful,
//        but WITHOUT ANY WARRANTY; without even the implied warranty of
//        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
//        GNU General Public License for more details.
//
//        You should have received a copy of the GNU General Public License
//        along with this program; if not, write to the Free Software
//        Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
//
// Nom:          Position
// Autheur: Cesare James
// Description: A class managing a character
// Nom:                  Character
// Auteur:                 Mixbo
// Description:         A class managing the character and its attributes
//	You should have received a copy of the GNU General Public License
//	along with this program; if not, write to the Free Software
//	Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
//  
//  Nom:    	 Position
//  Autheur:     Cesare James
//  Description: A class managing a character
//  Nom:    	 	Character
//  Auteur: 		Mixbo
//  Description: 	A class managing the character and its attributes
//
//
/////////////////////////////////////////////////////////////////////////////////

#ifndef CHARACTER_HPP
#define CHARACTER_HPP

#include <vector>


#include "GameObject.h"
#include "Weapons.h"

class Character : public GameObject
{
public:
        Character(std::string name);
        ~Character();
        
        /* METHODS */
        void shoot();
        Position move(char direction, int facteur);


private:
        std::string m_name;                //The caracter's name
        std::string m_teamName;            //The name of the character's team


        // Movement
        float m_weight; //trapu
        float m_speedX;
        float m_speedY;
        std::vector<Weapon> m_weapons;


};


#endif
=======
	Character(std::string name);
	~Character();
	
	/* METHODS */
	void shoot();
	Position move(char direction, int facteur);


private:
	std::string m_name;		//The caracter's name
	std::string m_teamName;		//The name of the character's team



	// Movement
	float m_weight; //trapu
	float m_speedX;
	float m_speedY;
	std::vector<Weapon> m_weapons;





};


#endif

