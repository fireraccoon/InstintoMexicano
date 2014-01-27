#ifndef ENGINE_LOG_HPP
#define ENGINE_LOG_HPP


class Log
{
public:


	template <typename T>
	static void debug(T message){
		std::cout << message << std::endl;
	}

	template <typename T>
	static void error(T message){
		std::cout << "ERROR: " << message << std::endl;
	}



private:
	Log();
	~Log();




};

#endif