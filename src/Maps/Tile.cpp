#include "Tile.hpp"


Tile::Tile()
{

	m_isBreakable = false;
	m_isSolid = false;
	m_corners.setPrimitiveType(sf::Quads);//Square
	m_corners.resize(4);

}


Tile::~Tile()
{

}

