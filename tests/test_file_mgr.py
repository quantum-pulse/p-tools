
from ptools.iowpr.file_mgr import file_mgr as fmgr
import unittest
import os

class test_file_mgr(unittest.TestCase):
    
    def setUp(self): 
        self.fmgr=fmgr()
        #os.mkdir("temp")

    def test_read(self):
        """
        Tests if the read method is correctly wrapped
        """
        l_list=self.fmgr.read("rc/sample.txt")
        self.assertEqual(len(l_list),1)
        self.assertEqual(l_list[0],"decoy to run test\n")

    def test_write(self):
        """
        Tests if the write is correctly wrapped 
        """
        l_list_buffer=["running writing test\n","for the file manager\n"]
        self.fmgr.write("rc/temp_buffer.txt",l_list_buffer)
        l_list=self.fmgr.read("rc/temp_buffer.txt")
        
        self.assertEqual(len(l_list),2)
        self.assertEqual(l_list[0],"running writing test\n")
        self.assertEqual(l_list[1],"for the file manager\n")

    def test_readjson(self):
        """
        Tests if the write is correctly wrapped 
        """
        #pass

    def tearDown(self):
        #os.remove("r
        pass
