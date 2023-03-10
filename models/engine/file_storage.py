#!/usr/bin/python3
"""Module for FileStorage class"""                                                                                                                                     
from models.base_model import BaseModel                                                                                                                                
from models.user import User                                                                                                                                           
from models.state import State                                                                                                                                         
from models.city import City                                                                                                                                           
from models.place import Place                                                                                                                                         
from models.amenity import Amenity                                                                                                                                     
from models.review import Review                                                                                                                                       
import json                                                                                                                                                            
import os                                                                                                                                                              
                                                                                                                                                                       
classes = {"BaseModel": BaseModel, "User": User, "State":State, "City": City,                                                                                          
           "Place": Place, "Amenity": Amenity, "Review": Review,}                                                                                                      
                                                                                                                                                                       
                                                                                                                                                                       
class FileStorage:                                                                                                                                                     
    """Class for serialization and deserialization"""                                                                                                                  
    __file_path = "file.json"                                                                                                                                          
    __objects = {}                                                                                                                                                     
                                                                                                                                                                       
    def all(self):                                                                                                                                                     
        """return the dictionary __objects"""                                                                                                                          
        return self.__objects                                                                                                                                          
                                                                                                                                                                       
    def new(self, obj):                                                                                                                                                
        """ instantiates a new object and saves it                                                                                                                     
        to the dictionary with its new key """                                                                                                                         
        key = obj.__class__.__name__ + "." + obj.id                                                                                                                    
        self.__objects[key] = obj                                                                                                                                      
                                                                                                                                                                       
    def save(self):                                                                                                                                                    
        """ serializes the object to the JSON file """                                                                                                                 
        json_objects = {}                                                                                                                                              
        for key in self.__objects:                                                                                                                                     
            json_objects[key] = self.__objects[key].to_dict()                                                                                                          
        with open(self.__file_path, 'w') as f:                                                                                                                         
            json.dump(json_objects, f)                                                                                                                                 
                                                                                                                                                                       
    def reload(self):                                                                                                                                                  
        """deserializes the JSON file to __objects"""                                                                                                                  
        try:                                                                                                                                                           
            with open(self.__file_path, 'r') as f:                                                                                                                     
                jf = json.load(f)                                                                                                                                      
            for key in jf:                                                                                                                                             
                self.__objects[key] = classes[jf[key]["__class__"]](**jf[key])                                                                                         
        except:                                                                                                                                                        
            pass
