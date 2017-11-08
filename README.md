# DQ AWS Transition Testing

Exploring testing for Terraform. Using the [dq-terraform-demo](https://github.com/UKHomeOffice/dq-terraform-demo) code as a starting point to test. Focusing on the acceptance criteria of the [mock application](https://github.com/UKHomeOffice/dq-aws-transition/issues/38) and the AWS status check criteria.

## Potential Tools

Unit Testing:
* [RSpec](https://github.com/rspec/rspec)

Integration Testing:
* [Kitchen Terraform](https://github.com/newcontext-oss/kitchen-terraform) / [Test Kitchen](https://github.com/test-kitchen/test-kitchen)

Testing AWS:
* [AWS Spec](https://github.com/k1LoW/awspec) / [Cloud Watch](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html)
