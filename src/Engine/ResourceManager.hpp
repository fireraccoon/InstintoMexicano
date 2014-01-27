#ifndef ENGINE_RESSOURCE_MANAGER_HPP
#define ENGINE_RESSOURCE_MANAGER_HPP

/*- STL INCLUDES -*/
#include <iostream>
#include <string>
#include <map>
#include <utility> //pair
#include <vector>


/*- SFML -*/
#include <SFML\Graphics\Image.hpp>
#include <SFML\Graphics\Font.hpp>
#include <SFML\Graphics\Sprite.hpp>
#include <SFML\Graphics\Texture.hpp>

#include <SFML\Audio\Music.hpp>
#include <SFML\Audio\Sound.hpp>

/*- PROJECT INCLUDE -*/
#include "ResourceManagerType.hpp"


class ResourceManager{

public:
	ResourceManager(){}
	~ResourceManager(){}



	ResourceManagerType<sf::Texture>* textures(){  return &m_textureManager; }
	ResourceManagerType<sf::Image>*   images()  {  return &m_imageManager; }
	ResourceManagerType<sf::Font>*    fonts()   {  return &m_fontManager; }
	ResourceManagerType<sf::Sprite>*  sprites() {  return &m_spriteManager; }

	ResourceManagerType<sf::Music>*   music()   {  return &m_musicManager; }
	ResourceManagerType<sf::Sound>*   sounds()  {  return &m_soundManager; }

private:
	//Graphics
	ResourceManagerType<sf::Texture> m_textureManager;
	ResourceManagerType<sf::Image>   m_imageManager;
	ResourceManagerType<sf::Font>    m_fontManager;
	ResourceManagerType<sf::Sprite>  m_spriteManager;

	//Audio
	ResourceManagerType<sf::Music>  m_musicManager;
	ResourceManagerType<sf::Sound>  m_soundManager;


};

#endif //ENGINE_RESOURCE_MANAGER_HPP