#include "Weapons.hpp"

int Weapons::getRemainingAmmo()
{
	return m_ammo;
}
bool Weapons::canShoot()
{
	if (m_ammo > 0)
		return true;
	else
		return false;
}
void Weapons::shoot()
{
	m_ammo--;
}