# -----------------------------------------------------------
# small wrapper for directory handling 
#
# 2022 Robert KING, Berlin, Germany
# email: ro.king.eu@gmail.com 
# -----------------------------------------------------------

import os
import shutil
"""
class that handles tasks related to read and write directories

creates, removes, etc ... methods
"""
class dir_mgr:
    def __init__(self):
        pass
    
    def make(self, _dirname):
        """ creates directory
        parameter:
           directory name

        return:
            none
        """
        if(not os.path.isdir(_dirname)):
            os.mkdir(_dirname)

    def is_dir(self,_dirname):
        """ check if directory exists
        parameter:
           directory name

        return:
            boolean
        """
        return os.path.isdir(_dirname)

    def is_empty(self,_dirname):
        """ creates directory 
        parameter:
           directory name  
            
        return:
            boolean , if directory exist or not 
        """

        if len(os.listdir(_dirname)) == 0:
            return True
        else:
            return False

    def remove(self,_dirname):
        """ remove directory 
            parameter:
               directory name    
            return:
               none
        """
        if(self.is_empty(_dirname)):
            os.rmdir(_dirname)
        else:
            shutil.rmtree(_dirname)
