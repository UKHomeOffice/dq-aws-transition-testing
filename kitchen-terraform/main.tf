provider "aws" {
	access_key = "${var.access_key}"
	secret_key = "${var.secret_key}"
	region = "${var.region}"
}

resource "aws_instance" "example" {
	ami = "${var.ami}"
	instance_type = "${var.instance_type}"
	key_name = "${var.key_name}"
}
