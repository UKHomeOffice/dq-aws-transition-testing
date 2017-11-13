variable "AWS_ACCESS_KEY" {}
variable "AWS_SECRET_KEY" {}
variable "AWS_REGION"{
  default = "eu-west-1"
}
variable "AMIS" {
  type = "map"
  default = {
    eu-west-1 = "ami-add175d4"
  }
}

variable "PATH_TO_PRIVATE_KEY" {
  default = "example-key1"
}
variable "PATH_TO_PUBLIC_KEY" {
  default = "example-key1.pub"
}
variable "INSTANCE_USERNAME" {
  default = "ubuntu"
}
