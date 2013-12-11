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
//  Nom:    	 Position
//  Auteur:     Cesare James
//  Description: A class managing a position
//
//
/////////////////////////////////////////////////////////////////////////////////

class Position
{
public:

	Position(float x, float y);
	~Position();





	/* GETTERS & SETTERS */
	float getX();
	float getY();
	void  setX();
	void  setY();
	void  set(float x, float y);


private:
	float m_x;
	float m_y;

};

/* OPERATOR OVERLOADING */
Position operator+ (const Position& a, const Position& b);
Position operator- (const Position& a, const Position& b);
Position operator== (const Position& a, const Position& b);