#ifndef ENGINE_RESOURCE_MANAGER_TYPE_HPP
#define ENGINE_RESOURCE_MANAGER_TYPE_HPP

/*- STL INCLUDES -*/
#include <iostream>
#include <map>

/*- SFML INCLUDES -*/
#include <SFML\Graphics\Texture.hpp>

/*- PROJECT INCLUDES -*/
#include "Log.hpp"


template <typename ResourceType>
class ResourceManagerType
{
public:
	typedef std::map<std::string, ResourceType> Library;

	ResourceManagerType(){};
	~ResourceManagerType(){};



	void init(){
		//The main directory of the game
		addDirectory("/"); 

	}

	/**
	* Adds a directory in which we have to look for resources
	* Directory names should always end with a /
	*/
	void addDirectory(const std::string& directory)
	{
		//Is the directory in the list?
		for(unsigned int i=0; i< m_resourceDirectories.size(); i++)
			if(directory == m_resourceDirectories[i])
				return; //No need to add it then

		m_resourceDirectories.push_back(directory);
	}

	/**
	* Remove a directory from the list
	*/
	void removeDirectory(const std::string& directory)
	{
		//Is the directory in the list?
		for(int i=0; i< m_resourceDirectories.size(); i++)
			if(directory == m_resourceDirectories[i])
			{
				// Then we delete it
				m_resourceDirectories.erase(directory); 
				return;
			}
	}


	/**
	* Loads a resource and returns it
	*/
	ResourceType& ResourceManagerType<ResourceType>::get(const std::string& filename)
	{
		// Check, whether the Resource already exists in the Library
		for( Library::iterator it = m_resources.begin();it != m_resources.end();  ++it)
			if( filename == it->first )	
				return it->second; //We use the image in memory
	

		// The Texture doesn't exists in memory. Let's find it load it and save it
		//First we check the main directory
		ResourceType resource;
		if( resource.loadFromFile( filename ) )
		{
			m_resources[filename] = resource;
			Log::debug("Resource Manager: loading " + filename);
			return m_resources[filename];
		}


		//Then lets find it in all the directories we know
		for(std::vector<std::string>::iterator it = m_resourceDirectories.begin(); 
			  it != m_resourceDirectories.end(); it++)
		{
			if( resource.loadFromFile( (*it) + filename) ){
				m_resources[filename] = resource;
				Log::debug("Resource Manager: loading " + filename);
				return m_resources[filename];
			}
		}



		//We will fill it with an empty resource, because we could not load it
		Log::error("Resource Manager:  " + filename + " was not found");
		m_resources[filename] = resource;
		return m_resources[filename];
}


	




private:




	Library m_resources; //contains all the Resources with their filename as a key
	std::vector<std::string> m_resourceDirectories;	   //Contains all the directory in which we need to look for the resources 




};











#endif //ENGINE_RESOURCE_MANAGER_TYPE_HPP