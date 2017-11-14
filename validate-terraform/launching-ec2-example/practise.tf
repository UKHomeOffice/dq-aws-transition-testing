resource "aws_instance" "foo" {
  # This would fail the test
  ebs_block_device{
    encrypted = false
  }
}

resource "aws_ebs_volume" "bar" {
  # This would fail the test
  encrypted = false
}
