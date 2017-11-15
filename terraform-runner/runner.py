# go get github.com/wybczu/tfjson
import json
from pprint import pprint
import sys
import os
import shutil
import subprocess
from subprocess import call

class Runner(object):
    'Terraform converter, converting .tf files into JSON and Python'
    def __init__(self, snippet):
        self.snippet = snippet

    def setup(self):
        shutil.rmtree("./.tmp")
        os.mkdir("./.tmp")
        call(["terraform", "init", ".tmp"])
        call(["cp", "vars.tf", "./.tmp"])
        call(["cp", "terraform.tfvars", "./.tmp"])
        fh = open("./.tmp/mytf.tf","w")
        fh.write(snippet)
        fh.close()
        # Add other file creations
        os.system("terraform plan -out=./.tmp/mytf.tfstate ./.tmp ")

    def snippet_to_json(self):
        # Parsing
        parse = subprocess.Popen(['/Users/ottern/go/bin/tfjson', './.tmp/mytf.tfstate'],
                            stdout=subprocess.PIPE).stdout.read()
        # Saving to file
        fjs = open("./.tmp/myjson.json","w")
        print(parse)
        print >>fjs, parse
        fjs.close()

    def json_to_py(self):
        # Parsing
        with open('./.tmp/myjson.json') as myjson:
            data = json.load(myjson)

        # Saving to file and prettifying
        fpy = open("./.tmp/mypy.py", "w")
        pprint(data, stream=fpy)
        fpy.close()


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

runner = Runner(snippet)
runner.setup()
runner.snippet_to_json()
runner.json_to_py()
