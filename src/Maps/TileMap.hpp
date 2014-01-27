#ifndef MAPS_TILE_MAP_HPP
#define MAPS_TILE_MAP_HPP

/*- STL INCLUDES -*/
#include <iostream>
#include <string>


/*- SFML INCLUDES -*/
#include <SFML\Graphics.hpp>
#include "../Engine/SettingParser.hpp"

/*- PROJECT INCLUDES -*/
#include "Tile.hpp"
#include "../Background.hpp"

class TileMap : public sf::Drawable, public sf::Transformable
{
public:
	TileMap();
	~TileMap();

	void load(const std::string& configFileName, ResourceManager& resMgr);
	

	/* GETTERS & SETTERS */
	
	
	Tile getTileID(int posX, int posY){

		return m_tiles[ posX + posY * m_width];
	}

	Tile getTileID(sf::Vector2f pos){

		return m_tiles[ (pos.x/m_tileSize.x) + (pos.y/m_tileSize.y) * m_width];
	}


private:
	void loadFromSettings(ResourceManager& resMgr);

	void loadFromTileset();

	 void draw(sf::RenderTarget& target, sf::RenderStates states) const;

	 
	
public:
	/* DATA MEMBERS */
	SettingParser::ConfigurationFile m_dataFile;

	//The configuration of the map (numbers)
	std::vector<int> m_data;

	std::string m_name;
	int m_height;
	int m_width;
	sf::Vector2u m_tileSize;

	std::vector<Tile> m_tiles;
	sf::VertexArray m_vertices;
	sf::Texture m_tileset;
	
	Background m_background;

};

#endif //MAPS_TILE_MAP_HPP
