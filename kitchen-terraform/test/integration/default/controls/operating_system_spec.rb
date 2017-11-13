# Using InSpec Syntax
control 'operating_system' do
  describe command('lsb_release -a') do
    its('stdout') { should match (/Ubuntu/) }
    puts 'lsb_release -a'
  end
end
