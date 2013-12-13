/////////////////////////////////////////////////////////////////////////////////
//  
//  Instinto Mexicano
//  Copyright (C) 2013 Team G.O.A.T
//  This program is free software; you can redistribute it and/or
//  modify it under the terms of the GNU General Public License
//        as published by the Free Software Foundation; either version 2
//        of the License, or (at your option) any later version.
//
//        This program is distributed in the hope that it will be useful,
//        but WITHOUT ANY WARRANTY; without even the implied warranty of
//        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//        GNU General Public License for more details.
//
//        You should have received a copy of the GNU General Public License
//        along with this program; if not, write to the Free Software
//        Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
//  
//  Nom:             Position
//  Auteur:     Cesare James
//  Description: A class managing a position
//
//
/////////////////////////////////////////////////////////////////////////////////

#include "Position.hpp"


Position::Position(float x, float y)
{
        m_x = x;
        m_y = y;
}
Position::~Position(){};

/* METHODS */

bool Position::equals(Position b)
{
	return  (m_x == b.getX() && m_y == b.getY() );
}


void Position::add(float amount){

	m_x += amount;
	m_y += amount;
}

void Position::addX(float amount)
{
	m_x += amount;
}

void Position::addY(float amount)
{
	m_y += amount;
}



void Position::substract(float amount)
{
	m_x -= amount;
	m_y -= amount;
}

void Position::substractX(float amount)
{
	m_x -= amount;
}

void Position::substractY(float amount)
{
	m_y -= amount;
}









        /* GETTERS & SETTERS */
float Position::getX(){ return m_x; }
float Position::getY(){ return m_y; }
void  Position::setX(float x){ m_x = x; }
void  Position::setY(float y){ m_y = y; }
void  Position::set(float x, float y){ m_x =x; m_y = y;}


