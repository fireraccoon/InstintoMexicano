#include "SettingParser.hpp"


namespace SettingParser
{

//configuration file


ConfigurationFile::ConfigurationFile(const std::string fileName)
{
	m_fileName = fileName;
}


void ConfigurationFile::load(){
	extractKeys();
}

bool ConfigurationFile::keyExists(const std::string &key) const
{
	return m_content.find(key) != m_content.end();
}

std::string ConfigurationFile::readArray() const{

	std::string returnedArray;
	std::ifstream fin;
	fin.open(m_fileName.c_str());
	if(!fin)
		Engine::exitWithError(":: Setting Parser :: could load the file \"" + m_fileName + "\"");

	char next;
	while( (next = fin.get()) != EOF)
	{
		if(next != '\n')
			returnedArray += next;
	}

	return returnedArray;
}



void ConfigurationFile::removeComments(std::string &line) const
{
		
	if(line.find(COMMENT_CHAR) != line.npos)
		line.erase(line.find(COMMENT_CHAR));
}



bool ConfigurationFile::onlyWhiteSpace(const std::string &line) const
{
	return (line.find_first_not_of(' ') == line.npos);
}


bool ConfigurationFile::validLine(const std::string &line) const
{
	std::string temp = line;
	// We strip all the non space characters or tab to have only key=value
	temp.erase(0, temp.find_first_not_of("\t "));
	//if it starts with the affectation sign, it means with dont have no key
	if(temp[0] == AFFECTATION_SIGN)
		return false;

	//see if we have a value
	for(size_t i = temp.find(AFFECTATION_SIGN) + 1; i < temp.length(); i++)
		if(temp[i] != ' ');
			return true;

	return false; //we didnt find any value
}


void ConfigurationFile::extractKey(std::string &key, size_t const &separatorPos, const std::string &line) const
{
	key = line.substr(0, separatorPos);
	if(key.find('\t') != line.npos || key.find(' ') != line.npos)
		key.erase(key.find_first_not_of("\t "));

}


void ConfigurationFile::extractValue(std::string &value, size_t const &sepPos, const std::string &line) const
{
	value = line.substr(sepPos + 1);
	value.erase(0, value.find_first_not_of("\t "));
	value.erase(value.find_last_not_of("\t ") + 1);
}

void ConfigurationFile::extractContents(const std::string &line) 
{
	std::string temp = line;
		// Erase leading whitespace from the line.
	temp.erase(0, temp.find_first_not_of("\t "));
	size_t sepPos = temp.find('=');

	std::string key, value;
	extractKey(key, sepPos, temp);
	extractValue(value, sepPos, temp);

	if (!keyExists(key))
		m_content.insert(std::pair<std::string, std::string>(key, value));
	else
		Engine::exitWithError(":: Setting Parser :: : Can only have unique key names!\n");
}





void ConfigurationFile::parseLine(const std::string &line, size_t const lineNo)
{
	if (line.find('=') == line.npos)
		Engine::exitWithError(":: Setting Parser :: : Couldn't find separator at line: " + Convert::toString(lineNo) + "\n");

	if (!validLine(line))
			Engine::exitWithError(":: Setting Parser :: : Bad format for line: " + Convert::toString(lineNo) + "\n");

	extractContents(line);
}

void ConfigurationFile::extractKeys()
{
	std::ifstream file;
	file.open(m_fileName.c_str());
	if (!file)
		Engine::exitWithError(":: Setting Parser :: : File " + m_fileName + " couldn't be found!\n");

	std::string line;
	size_t lineNo = 0;
	while (std::getline(file, line))
	{
		lineNo++;
		std::string temp = line;

		if (temp.empty())
			continue;

		removeComments(temp);
		if (onlyWhiteSpace(temp))
			continue;

		parseLine(temp, lineNo);
	}

	file.close();
}




}; //namespace SettingParser