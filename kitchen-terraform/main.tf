resource "aws_key_pair" "example-key1" {
  key_name   = "example-key1"
  public_key = "${file("${var.PATH_TO_PUBLIC_KEY}")}"
}

provider "aws" {
	access_key = "${var.AWS_ACCESS_KEY}"
	secret_key = "${var.AWS_SECRET_KEY}"
	region = "${var.AWS_REGION}"
}

resource "aws_instance" "example" {
	ami = "${lookup(var.AMIS, var.AWS_REGION)}"
	instance_type = "t2.micro"
	key_name = "${aws_key_pair.example-key1.key_name}"
}
