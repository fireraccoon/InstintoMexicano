#include "Background.hpp"


Background::Background()
{
	m_vertices.setPrimitiveType(sf::Quads);
	m_vertices.resize(4);
}


Background::~Background(){}

void Background::setTexture(sf::Texture* texture){
	m_texture = texture;

}



void Background::draw(sf::RenderTarget& target, sf::RenderStates states) const
{
    // on applique la transformation
    states.transform *= getTransform();

    // on applique la texture du tileset
    states.texture = m_texture;

    // et on dessine enfin le tableau de vertex
    target.draw(m_vertices, states);
}
