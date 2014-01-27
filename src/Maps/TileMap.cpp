#include "TileMap.hpp"

TileMap::TileMap(){}

TileMap::~TileMap(){}


void  TileMap::load(const std::string& configFileName, ResourceManager& resMgr){
		
		m_dataFile.setFileName(configFileName);
		m_dataFile.load();
		loadFromSettings(resMgr);
		loadFromTileset();

		m_background.setTexture(&resMgr.textures()->get("bg.jpg"));


}

void TileMap::loadFromSettings(ResourceManager& resMgr){

			m_name = m_dataFile.getValueOfKey<std::string>("name");
			m_height = m_dataFile.getValueOfKey<int>("height");
			m_width = m_dataFile.getValueOfKey<int>("width");
			m_tileSize.x = m_dataFile.getValueOfKey<int>("tile_size");
			m_tileSize.y = m_tileSize.x;

			//tileset
			std::string tilesetName = m_dataFile.getValueOfKey<std::string>("tileset");
			m_tileset = resMgr.textures()->get(tilesetName);

			//config_file
			std::string mapConfig = m_dataFile.getValueOfKey<std::string>("data_file");
			SettingParser::ConfigurationFile mapConfigFile(mapConfig);
			mapConfig = mapConfigFile.readArray();

			//Now we need to convert the mapConfig to a vector of int
			for(int i=0; i< mapConfig.size();i++){
				std::string str = SettingParser::Convert::charToString(mapConfig[i]);
				int number = SettingParser::Convert::stringTo<int>(str);
				m_data.push_back(number);
			}
}


void TileMap::loadFromTileset(){
		m_vertices.setPrimitiveType(sf::Quads);		//using quads for the vertices;
		m_vertices.resize(m_width * m_height * 4);  
		m_tiles.resize(m_width * m_height); 

		//filling by height first, then by width
		for(unsigned int i=0; i<m_width;i++){ //x
			for(unsigned int j=0; j<m_height; j++){ //y
					Tile tile;
					tile.setPosition(i,j);
					
					int tileNumber = m_data[ i + j * m_width]; //The tile symbol
					tile.setSymbol(tileNumber);

					//Manage Solid
					for (int i =0; i< 10; i++){
						std::string key = SettingParser::Convert::toString(i);
						key +="_is_solid";

						if( m_dataFile.keyExists(key) && tile.getSymbol() == i ){
							tile.setSolid(SettingParser::Convert::stringToBool(m_dataFile.getValueOfKey<std::string>(key)));
						}
					}



					//Let's find the position of the tile in the texture according to it's number
					int tu = tileNumber % (m_tileset.getSize().x / m_tileSize.x);
					int tv = tileNumber / (m_tileset.getSize().x / m_tileSize.x);

					//We find a pointer of the concerned Vertex
					sf::Vertex* quad = &m_vertices[(i + j * m_width) * 4];

					//Defining the 4 corners
					quad[0].position = sf::Vector2f(i * m_tileSize.x, j * m_tileSize.y);
					quad[1].position = sf::Vector2f((i + 1) * m_tileSize.x, j * m_tileSize.y);
					quad[2].position = sf::Vector2f((i + 1) * m_tileSize.x, (j + 1) * m_tileSize.y);
					quad[3].position = sf::Vector2f(i * m_tileSize.x, (j + 1) * m_tileSize.y);
					


					//Coordinate in textures
					quad[0].texCoords = sf::Vector2f(tu * m_tileSize.x, tv * m_tileSize.y);
					quad[1].texCoords = sf::Vector2f((tu + 1) * m_tileSize.x, tv * m_tileSize.y);
					quad[2].texCoords = sf::Vector2f((tu + 1) * m_tileSize.x, (tv + 1) * m_tileSize.y);
					quad[3].texCoords = sf::Vector2f(tu * m_tileSize.x, (tv + 1) * m_tileSize.y);


					tile.setTopLeftVertex(quad[0]);
					tile.setTopRightVertex(quad[1]);
					tile.setBottomLeftVertex(quad[2]);
					tile.setBottomRightVertex(quad[3]);
					m_tiles[ i + j * m_width] = tile;
			}
		}
}





void TileMap::draw(sf::RenderTarget& target, sf::RenderStates states) const
{
    // on applique la transformation
    states.transform *= getTransform();

    // on applique la texture du tileset
    states.texture = &m_tileset;
	//Draw Background
	target.draw(m_background, states);

    // et on dessine enfin le tableau de vertex
    target.draw(m_vertices, states);
}
