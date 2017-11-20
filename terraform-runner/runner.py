# go get github.com/wybczu/tfjson
import json
import os
import shutil
import subprocess
import tempfile


class Runner(object):
    """Terraform converter, converting .tf files into JSON and Python"""

    def __init__(self, snippet):
        self.snippet = snippet
        self.run()

    def _removetmpdir(self):
        shutil.rmtree(self.tmpdir)

    def _mktmpdir(self):
        self.tmpdir = tempfile.mkdtemp()
        print(self.tmpdir)

    def _terraform_init(self):
        subprocess.call(["terraform", "init", self.tmpdir])

    def _copy_in_fixtures(self):
        subprocess.call(["cp", "vars.tf", self.tmpdir])
        subprocess.call(["cp", "terraform.tfvars", self.tmpdir])

    def _write_test_tf(self):
        fh = open("%s/mytf.tf" % (self.tmpdir), "w")
        fh.write(self.snippet)
        fh.close()

    def _teraform_plan(self):
        os.system("terraform plan -out=%s/mytf.tfplan %s" % (self.tmpdir, self.tmpdir))

    def run(self):
        self._mktmpdir()
        self._copy_in_fixtures()
        self._write_test_tf()
        self._terraform_init()
        self._teraform_plan()
        json = self.snippet_to_json()
        result = self.json_to_dict(json)
        self.result = result
        self._removetmpdir()

    def snippet_to_json(self):
        return subprocess.check_output(["tfjson", "%s/mytf.tfplan" % (self.tmpdir)])

    @staticmethod
    def json_to_dict(json_file):
        return json.loads(json_file)


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
