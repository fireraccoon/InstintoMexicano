#ifndef ENGINE_TILE_HPP
#define ENGINE_TILE_HPP


#include "../Engine/GameObject.hpp"
class Tile 
{
public:
	Tile();
	~Tile();


	/* GETTERS & SETTERS */
	bool isSolid(){ return m_isSolid;}
	bool isBreakable(){ return m_isBreakable;}

	void setSolid(bool value){ m_isSolid = value;}
	void setBreakable(bool value){m_isBreakable = value;}

	sf::Vertex getTopLeftVertex(){ return m_corners[0];}
	sf::Vertex getTopRightVertex(){ return m_corners[1]; }
	sf::Vertex getBottomLeftVertex(){ return m_corners[2];}
	sf::Vertex getBottomRightVertex(){ return m_corners[3];}

	void setTopLeftVertex(sf::Vertex value){  m_corners[0] = value;}
	void setTopRightVertex(sf::Vertex value){  m_corners[1] = value; }
	void setBottomLeftVertex(sf::Vertex value){  m_corners[2] = value;}
	void setBottomRightVertex(sf::Vertex value){  m_corners[3] = value;}




	int getSymbol(){ return m_symbol;}
	void setSymbol(int symbol){ m_symbol = symbol;}

	void setPosition(int i, int j){ m_i= i; m_j=j;}

	bool isCollision(sf::Vector2f pos){
		
		for(int i=0; i<4; i++){
			if(m_corners[i].position.x == pos.x || m_corners[i].position.y == pos.y)
				return true;
		}

		return false;
	}





private:
	bool m_isSolid;		//if the tile is solid or not (like a wall)
	bool m_isBreakable;	//if the tile is breakable or not	
	sf::VertexArray m_corners; //the four corners of the square
	int m_symbol; //It's number in the grid of a TileMap

	int m_i;
	int m_j;

};
#endif //ENGINE_TILE_HPP