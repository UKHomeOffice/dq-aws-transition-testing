# pylint: disable=missing-docstring, line-too-long, protected-access
import unittest
from unittest import mock
from runner import Runner


class TestRunnerMethods(unittest.TestCase):
    def setUp(self):
        self.snippet = "string"
        self.tmpdir = "foo"

    @mock.patch("tempfile.mkdtemp")
    def test_mktmpdir(self, tempfile_mock):
        tempfile_mock.return_value = "path"
        Runner._mktmpdir(self)
        self.assertEqual(self.tmpdir, "path")

    @unittest.skip # @TODO
    def test_run(self):
        # runner.run()
        self.assertEqual('{dict}', '{dict}')

    @mock.patch("shutil.rmtree")
    def test_removetmpdir(self, shutil_mock):
        Runner._removetmpdir(self)
        shutil_mock.assert_called_once_with(self.tmpdir)

    @mock.patch("subprocess.call")
    def test__terraform_init(self, subprocess_mock):
        Runner._terraform_init(self)
        subprocess_mock.assert_called_once_with(["terraform", "init", self.tmpdir])

    @mock.patch("subprocess.call")
    def test__copy_in_fixtures(self, subprocess_mock):
        Runner._copy_in_fixtures(self)
        subprocess_mock.assert_any_call(["cp", "vars.tf", self.tmpdir])
        subprocess_mock.assert_any_call(["cp", "terraform.tfvars", self.tmpdir])

    @mock.patch("os.system")
    def test_teraform_plan(self, os_mock):
        Runner._teraform_plan(self)
        os_mock.assert_called_once_with("terraform plan -out=" + self.tmpdir + "/mytf.tfplan " + self.tmpdir)

    @mock.patch("subprocess.check_output")
    def test_snippet_to_json(self, subprocess_mock):
        Runner.snippet_to_json(self)
        subprocess_mock.assert_called_once_with(['tfjson', self.tmpdir + '/mytf.tfplan'])

    @mock.patch("json.loads")
    def test_json_to_dict(self, mock_json):
        mock_json.return_value = {}
        json_file = {}
        self.assertEqual(Runner.json_to_dict(json_file), {})

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
