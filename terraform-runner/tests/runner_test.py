import unittest
from unittest import mock

from runner import Runner



class TestRunnerMethods(unittest.TestCase):


    @mock.patch("shutil.rmtree")
    def test_removeTmpDir(self, shutil_mock):
        Runner._removeTmpDir(self)
        shutil_mock.assert_called_once_with("./.tmp")

    @mock.patch("os.mkdir")
    def test_mkTmpDir(self, os_mock):
        Runner._mkTmpDir(self)
        os_mock.assert_called_once_with("./.tmp")


class TestE2E(unittest.TestCase):

    def setUp(self):
        self.snippet = """
        provider "aws" {
            access_key = "${var.AWS_ACCESS_KEY}"
            secret_key = "${var.AWS_SECRET_KEY}"
            region     = "us-west-2"
        }

        resource "aws_instance" "foo" {
          ami           = "foo"
          instance_type = "t2.micro"
        }
        """
        self.result = Runner(self.snippet).result

    def test_root_destroy(self):
        self.assertEqual(self.result["destroy"], False)

    def test_instance_type(self):
        self.assertEqual(self.result["aws_instance.foo"]["instance_type"], "t2.micro")

    def test_ami(self):
        self.assertEqual(self.result["aws_instance.foo"]["ami"], "foo")

    def test_destroy(self):
        self.assertEqual(self.result["aws_instance.foo"]["destroy"], False)

    def test_destroy_tainted(self):
        self.assertEqual(self.result["aws_instance.foo"]["destroy_tainted"], False)

if __name__ == '__main__':
    unittest.main()
