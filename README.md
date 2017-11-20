# DQ AWS Transition Testing

Exploring testing for Terraform. Using the [dq-terraform-demo](https://github.com/UKHomeOffice/dq-terraform-demo) code as a starting point to test. Focusing on the acceptance criteria of the [mock application](https://github.com/UKHomeOffice/dq-aws-transition/issues/38) and the AWS status check criteria.

Based on the findings below, we pursued the route of parsing Terrafom script ouputted by the ```plan``` command into Python. The repo for this tool can be found here: [tf-testrunner](https://github.com/UKHomeOffice/tf-testrunner).

## Potential Testing Frameworks

**Unit Testing Frameworks:**

* Parse HCL script and use [RSpec](https://github.com/rspec/rspec), with [SimpleCov](https://github.com/colszowka/simplecov) to check code coverage
* Parse JSON script (Terraform supports reading JSON) and then test
* [Terraform Validate](https://github.com/elmundio87/terraform_validate)

Provider dependent unit testing tools are very scarce, but Terraform Validate is regularly updated.

**Unit Testing using Terraform:**

* ```terraform plan -out <filename>.terraform```
* ```terraform apply <filename>.terraform```

The Terraform subcommand ```plan -out <filename>.terraform``` displays and saves to a separate file the changes that will occur on running ```terraform apply``` without executing those changes.

If you use the two separate commands, Terraform will first show you what changes it will make without executing those actual changes. The second command, will ensure that only the changes you saw on screen and saved to file are applied. If you would just use ```terraform apply```, more changes could have been added, because the remote infrastructure can change or the files could have been edited.

**Integration Testing Frameworks:**

* [Kitchen Terraform](https://github.com/newcontext-oss/kitchen-terraform)

Negatives: slow feedback loops, potentially costly having to mirror entire infrastructure in a sandbox. Without a code coverage supporting framework currently available, will have to be fastidious!

**Acceptance/compliance Testing Frameworks:**

* [Goss](https://github.com/aelsabbahy/goss)
* [Serverspec](https://github.com/mizzy/serverspec)


## Resources Used

* [Top 3 Terraform Testing Strategies...](https://www.contino.io/insights/top-3-terraform-testing-strategies-for-ultra-reliable-infrastructure-as-code)
* [Terraform - Up and Running...](https://www.amazon.co.uk/Terraform-Running-Writing-Infrastructure-Code/dp/1491977086)
* [Infrastructure Automation with Terraform](https://www.udemy.com/learn-devops-infrastructure-automation-with-terraform/?couponCode=TERRAFORM_YTB)
* [Verify AWS Infrastructure...](http://ec2dream.blogspot.co.uk/2017/01/verify-aws-infrastructure-with-test.html)
* [AWS Documentation](https://aws.amazon.com/documentation/)
* [Cloud Watch](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html)
* [AWS Spec](https://github.com/k1LoW/awspec)
