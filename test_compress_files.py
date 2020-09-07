import unittest
import os
import shutil
from compress_files import gzip_files, get_files


class CompressFilesTestCase(unittest.TestCase):
    test_dir = "test_dir"
    test_file = "test_file.txt"

    def setUp(self):
        """

        Setup test dir with test file

        """
        try:
            shutil.rmtree(self.test_dir)
        except:
            pass
        os.mkdir(self.test_dir)
        with open(self.test_dir + os.sep + self.test_file, 'w') as f_out:
            f_out.write("123456789")

    def test_compress_files(self):
        """
        Test if .gz file is created
        """
        test_list = [self.test_dir + os.sep + self.test_file]
        gzip_files(test_list)
        self.assertEqual(os.path.exists(self.test_dir + os.sep + self.test_file + ".gz"), True)

    def test_get_files(self):
        """
        Test if get_files returns test_file.txt
        """
        self.assertIn(self.test_dir+os.sep+self.test_file, (get_files(self.test_dir)))


