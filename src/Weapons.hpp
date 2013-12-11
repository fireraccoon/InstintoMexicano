class Weapon
{
	public:
		Weapon(std::string name);
		int getRemainingAmmo();
		bool canShoot();
		void shoot();

	private:
		std::string name;
		float m_fireRate, m_damage, m_accuracy, m_range;
		int m_ammo;
};