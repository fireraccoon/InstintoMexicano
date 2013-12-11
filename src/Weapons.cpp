#include "Weapons.hpp"

int Weapons::getRemainingAmmo()
{
	return m_ammo;
}
bool Weapons::canShoot()
{
	return (m_ammo > 0);
}
void Weapons::shoot()
{
	m_ammo--;
}
