
from ptools.iowpr.file_mgr import file_mgr as fmgr
from ptools.iowpr.dir_mgr import dir_mgr as dmgr

import unittest

class test_file_mgr(unittest.TestCase):
    
    def setUp(self): 
        self.fmgr=fmgr()
        self.dmgr=dmgr()
        self.dmgr.make("temp")

    def test_read(self):
        """
        Tests if the read method is correctly wrapped
        """
        l_list=self.fmgr.read("rc/sample.txt")
        self.assertEqual(len(l_list),1)
        self.assertEqual(l_list[0],"decoy to run test\n")

    def test_write(self):
        """
        Tests if the write method is correctly wrapped 
        """
        l_list_buffer=["running writing test\n","for the file manager\n"]
        self.fmgr.write("temp/temp_buffer.txt",l_list_buffer)
        l_list=self.fmgr.read("temp/temp_buffer.txt")
        
        self.assertEqual(len(l_list),2)
        self.assertEqual(l_list[0],"running writing test\n")
        self.assertEqual(l_list[1],"for the file manager\n")

    def test_readjson(self):
        """
        Tests if the read json method is correctly wrapped 
        """
        l_json_file=self.fmgr.readjson("rc/langage.json")
        fields=[ field for field in l_json_file.keys()]
        search= lambda value: l_json_file[value] if(l_json_file[value]) else None

        langage=search("langage")
        compiler=search("compiler")
        debugger=search("debugger")

        self.assertEqual(langage,"cxx")
        self.assertEqual(compiler,"clang++-14")
        self.assertEqual(debugger,"gdb")

    def test_is_file(self):
        """
        Tests if the object is a file
        """
        self.assertEqual(self.fmgr.is_file("rc/sample.txt"),True)

    def test_rid(self):
        """
        Tests if the file has been removed
        """
        l_list_buffer=["fake content"]
        self.fmgr.write("temp/fake_file.txt",l_list_buffer)
        self.assertEqual(self.fmgr.is_file("temp/fake_file.txt"),True)
        self.fmgr.rid("temp/fake_file.txt")
        self.assertEqual(self.fmgr.is_file("temp/fake_file.txt"),False)

    def tearDown(self):
        self.dmgr.remove("temp")
