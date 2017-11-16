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

    # @classmethod
    # def setup(cls):
        # Add other file creations
        #

    def _removeTmpDir(self):
        # if dir exists
        shutil.rmtree("./.tmp")

    def _mkTmpDir(self):
        os.mkdir("./.tmp")

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
        # self._removeTmpDir()
        # self._mkTmpDir()
        # self._teraform_init()
        # self._copy_in_fixtures()
        # self._write_test_tf()
        # self._teraform_plan()
        result = self.snippet_to_json()
        self.result = result

    def snippet_to_json(self):
        json_parser = subprocess.check_output(['/Users/ottern/go/bin/tfjson', './.tmp/mytf.tfplan'])
        return json.loads(json_parser)

    # @staticmethod
    # def json_to_py(self):
    #     # Parsing
    #     fjs = open("./.tmp/myjson.json", "r")
    #     fpy = open("./.tmp/mypy.py", "w")
    #     parse = json.load(fjs)
    #
    #     with open("./.tmp/mypy.py", "w") as fpy:
    #         print(json.dump(parse, fpy))

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

# runner = Runner(snippet)
# runner.setup()
# runner.snippet_to_json(runner)
# runner.json_to_py(runner)
