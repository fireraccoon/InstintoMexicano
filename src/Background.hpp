#pragma once

#include <SFML\Graphics\VertexArray.hpp>
#include <SFML\Graphics\Transformable.hpp>
#include <SFML\Graphics\Drawable.hpp>
#include <SFML\Graphics\RenderTarget.hpp>

class Background : public sf::Transformable, public sf::Drawable
{
public:
	Background();
	~Background();

	void setTexture(sf::Texture* texture);

	void draw(sf::RenderTarget& target, sf::RenderStates states) const;

private:
	sf::VertexArray m_vertices;
	sf::Texture* m_texture;
};

