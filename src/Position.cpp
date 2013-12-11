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
//  Autheur:     Cesare James
//  Description: A class managing a position
//
//
/////////////////////////////////////////////////////////////////////////////////

##include "Position.h"


Position::Position(float x, float y)
{
	m_x = x;
	m_y = y;
}
Position::~Position(){};




	/* GETTERS & SETTERS */
float Position::getX(){ return m_x; }
float Position::getY(){ return m_y; }
void  Position::setX(float x){ m_x = x; }
void  Position::setY(float y){ m_y = y; }
void  Position::set(float x, float y){ m)x =x; m_y = y;}



/* OPERATOR OVERLOADING */
Position operator+ (const Position& a, const Position& b){
	Position result( a.getX()+b.getX(), a.getY()+b.getY() );
	return result;
}

Position operator- (const Position& a, const Position& b){
	Position result( a.getX()-b.getX(), a.getY()-b.getY() );
	return result;
}

Position operator== (const Position& a, const Position& b){
	if(a.getX() == b.getX() && a.getY() == b.getY())
		return true;

	return false;
}