# go get github.com/wybczu/tfjson
import json
import sys
import os
import shutil
import subprocess
from subprocess import call

class Runner(object):
    'Terraform converter, converting .tf files into JSON and Python'
    def __init__(self, snippet):
        self.snippet = snippet
        self.run()

    def _removeTmpDir(self):
        # if dir exists
        shutil.rmtree("./.tmp")

    def _mkTmpDir(self):
        os.mkdir("./.tmp")
        self.tmpdir = tempfile.mkdtemp()
        print(self.tmpdir)

    def _teraform_init(self):
        call(["terraform", "init", ".tmp"])

    def _copy_in_fixtures(self):
        call(["cp", "vars.tf", "./.tmp"])
        call(["cp", "terraform.tfvars", "./.tmp"])

    def _write_test_tf(self):
        fh = open("./.tmp/mytf.tf","w")
        fh.write(self.snippet)
        fh.close()

    def _teraform_plan(self):
        os.system("terraform plan -out=./.tmp/mytf.tfplan ./.tmp ")

    def run(self):
        result = self.snippet_to_json()
        self.result = result

    def snippet_to_json(self):
        json_parser = subprocess.check_output(['tfjson', './.tmp/mytf.tfplan'])
        return json.loads(json_parser)


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

