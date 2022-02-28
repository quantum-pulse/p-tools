# -----------------------------------------------------------
# small wrapper for file handling 
#
# 2022 Robert KING, Berlin, Germany
# email: ro.king.eu@gmail.com 
# -----------------------------------------------------------

import json
"""
class that handles json & text files 

read & write methods
"""
class file_mgr:
    def __init__(self):
        pass
    
    def read(self, _filename):
        """ reads text,csv files 
        parameter:
           filename  
            
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
               list of strings to be dumped into a file    
            return:
                a dictionnary that contains the json file's content
        """
        l_data=None
        with open(_json) as json_data:
            l_data = json.load(json_data)
        return l_data
