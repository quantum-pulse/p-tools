# -----------------------------------------------------------
# small wrapper for file handling 
#
# 2022 Robert KING, Berlin, Germany
# email: ro.king.eu@gmail.com 
# -----------------------------------------------------------

import json
import os
"""
class that handles json & text files 

read & write, etc ... methods
"""
class file_mgr:
    def __init__(self):
        pass
    
    def read(self, _filename):
        """ reads text,csv files 
        parameter:
           file name  
            
        return:
           a list the contains the file's content 
        """ 
        l_file = open(_filename,"r")
        l_bufferlist = l_file.readlines()
        l_file.close()
        return l_bufferlist

    def write(self, _filename , _bufferlist):
        """ writes text in a file
            parameter:
               list of strings to be dumped into a file    
            return:
               none
        """
        l_newfile = open(_filename,"w")
        l_newfile.writelines(_bufferlist)
        l_newfile.close()

    def readjson(self,_json):
        """ reads json files
            parameter:
               name of json file    
            return:
                a dictionnary that contains the json file's content
        """
        l_data=None
        with open(_json,'r') as json_data:
            l_data = json.load(json_data)
        return l_data

    def is_file(self,_filename):
        """ check if object is a file 
            parameter:
               file name    
            
            return:
                a dictionnary that contains the json file's content
        """
        return os.path.isfile(_filename)

    def rid(self,_filename):
        """ removes file
            parameter:
               file name
            return:
                none
        """
        if(self.is_file(_filename)):
            os.remove(_filename)
