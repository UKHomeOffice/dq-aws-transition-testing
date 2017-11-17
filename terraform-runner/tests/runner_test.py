import unittest
from unittest import mock
from unittest.mock import patch, mock_open
from unittest.mock import MagicMock
from runner import Runner


class TestRunnerMethods(unittest.TestCase):

    @mock.patch("shutil.rmtree")
    def test_removeTmpDir(self, shutil_mock):
        Runner._removeTmpDir(self)
        shutil_mock.assert_called_once_with("./.tmp")

    @mock.patch("subprocess.call")
    def test__terraform_init(self, subprocess_mock):
        Runner._terraform_init(self)
        subprocess_mock.assert_called_once_with(["terraform", "init", ".tmp"])

    @mock.patch("subprocess.call")
    def test__copy_in_fixtures(self, subprocess_mock):
        Runner._copy_in_fixtures(self)
        subprocess_mock.assert_any_call(["cp", "vars.tf", "./.tmp"])
        subprocess_mock.assert_any_call(["cp", "terraform.tfvars", "./.tmp"])

    @mock.patch("os.system")
    def test_teraform_plan(self, os_mock):
        Runner._teraform_plan(self)
        os_mock.assert_called_once_with("terraform plan -out=./.tmp/mytf.tfplan ./.tmp ")

    @mock.patch("subprocess.check_output")
    def test_snippet_to_json(self, subprocess_mock):
        Runner.snippet_to_json(self)
        subprocess_mock.assert_called_once_with(['/Users/ottern/go/bin/tfjson', './.tmp/mytf.tfplan'])

    @mock.patch("json.loads")
    def test_json_to_dict(self, mock_json):
        mock_json.return_value = {}
        json_file = {}

        self.assertEqual(Runner.json_to_dict(self, json_file), {})


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
