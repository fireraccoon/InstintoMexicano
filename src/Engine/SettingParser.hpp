
// http://www.dreamincode.net/forums/topic/183191-create-a-simple-configuration-file-parser/

#ifndef ENGINE_SETTINGPARSER_HPP
#define ENGINE_SETTINGPARSER_HPP


/*- STL INCLUDES -*/
#include <iostream>
#include <string>
#include <map>
#include <sstream> //converstion from string to primitive types
#include <fstream> //file handling

#include "Engine.hpp"

namespace SettingParser
{


	

/**
* A converter convertingstring to primitives and vice-versa
*/
class Convert
{
public:
	// Convert a orimitive type to string
	template <typename T>
	static std::string toString(T const &value){

		std::ostringstream ostr; //output string stream
		ostr << value;
		return ostr.str();
	}



	// Convert a std::string to a primitive type
	template <typename T>
	static T stringTo(std::string const &value){

		std::istringstream istr(value); //input string stream
		T returnValue;

		if ( !(istr >> returnValue) )
			Engine::exitWithError(":: Setting Parser :: Not a valid " + (std::string)typeid(T).name() + " received!\n");
		return returnValue;
	}

	//Convert char to string
	static std::string charToString(char c)
	{	
		std::string s;
		std::stringstream ss;
		ss << c;
		ss >> s;
		return s;
	}



	static bool stringToBool(std::string str){
		return (str == "true");
	}




};





class ConfigurationFile
{

public:


	static const char COMMENT_CHAR     = '#';
	static const char AFFECTATION_SIGN = '=';

	/* ctor & dtor */
	ConfigurationFile(){}
	ConfigurationFile(const std::string fileName);


	/* METHODS */
	void ConfigurationFile::load();

	bool keyExists(const std::string &key) const;


	template <typename ValueType>
	ValueType getValueOfKey(const std::string &key, ValueType const &defaultValue = ValueType()) const
	{
		if (!keyExists(key))
			return defaultValue;

		return Convert::stringTo<ValueType>(m_content.find(key)->second);
	}


	std::string readArray() const;

	/* GETTERS & SETTERS */
	void setFileName(const std::string& fileName){ m_fileName = fileName; }



private:
	void removeComments(std::string &line) const;

	bool onlyWhiteSpace(const std::string &line) const;

	/**
	* Checks if the file has the correct structure of a config file
	* param line is a line WITHOUT comments
	*/
	bool validLine(const std::string &line) const;

	/*
	* separatorPos is the position of the ASSIGNATION_SIGN
	*/
	void extractKey(std::string &key, size_t const &separatorPos, const std::string &line) const;

	/*
	* separatorPos is the position of the ASSIGNATION_SIGN
	*/
	void extractValue(std::string &value, size_t const &sepPos, const std::string &line) const;

	void extractContents(const std::string &line);

	// lineNo = the current line number in the file.
	// line = the current line, with comments removed.
	void parseLine(const std::string &line, size_t const lineNo);

	void extractKeys();




private:
	/* DATA MEMBERS */
	std::string m_fileName;
	std::map<std::string, std::string> m_content; //Contains the key and the values

};




}; // namespace SettingParser





#endif //ENGINE_SETTINGPARSER_HPP