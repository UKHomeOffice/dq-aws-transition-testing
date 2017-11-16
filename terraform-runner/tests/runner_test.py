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


class TestE2E(unittest.TestCase): # pragma: no cover
    def test_the_full_e2e(self):
        snippet = """
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
        result = Runner(snippet).result
        self.assertEqual(result["destroy"], False)
        self.assertEqual(result["aws_instance.foo"]["instance_type"], "t2.micro")
        self.assertEqual(result["aws_instance.foo"]["ami"], "foo")
        self.assertEqual(result["aws_instance.foo"]["destroy"], False)
        self.assertEqual(result["aws_instance.foo"]["destroy_tainted"], False)

if __name__ == '__main__':
    unittest.main()
