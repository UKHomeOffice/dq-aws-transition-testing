import terraform_validate

class TestEncryptionAtRest(unittest.TestCase):

    def setUp(self):
        # Tell the module where to find your terraform configuration folder
        self.path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"practise")
        self.v = terraform_validate.Validator(self.path)

    def test_aws_ebs_volume(self):
        # Assert that all resources of type 'aws_ebs_volume' are encrypted
        self.v.error_if_property_missing() #Fail any tests if the property does not exist
        self.v.resources('aws_ebs_volume').property('encrypted').should_equal(True)

    def test_instance_ebs_block_device(self):
        # Assert that all resources of type 'ebs_block_device' that are inside a 'aws_instance' are encrypted
        self.v.error_if_property_missing()
        self.v.resources('aws_instance').property('ebs_block_device').property('encrypted').should_equal(True)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEncryptionAtRest)
    unittest.TextTestRunner(verbosity=0).run(suite)
