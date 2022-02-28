
from ptools.iowpr.file_mgr import file_mgr as fmgr
import unittest

class test_file_mgr(unittest.TestCase):
    def test_read(self):
        """
        Tests if the read method works
        """
        l_file_mgr=fmgr()
        l_list=l_file_mgr.read("rc/sample.txt")
        self.assertEqual(l_list[0],"decoy to run test\n")
        self.assertEqual(len(l_list),1)

if __name__ == '__main__':
    unittest.main()

