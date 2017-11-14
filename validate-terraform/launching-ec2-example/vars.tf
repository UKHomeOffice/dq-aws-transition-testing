variable "AWS_ACCESS_KEY" {}
variable "AWS_SECRET_KEY" {}

variable "AWS_REGION" {
  default = "eu-west-1"
}

variable "AMIS" {
  type = "map"

  default = {
    eu-west-1 = "ami-add175d4"
  }
}
