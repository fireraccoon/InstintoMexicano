class Weapon
{
private:
	std::string name;
	float fireRate, damage, accuracy, range;
	int ammo;
public:
	Weapon(std::string name);
	int getRemainingAmmo();
	bool canShoot();
	void shoot();
};