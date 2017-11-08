require 'test'

RSpec.describe Test do
  context '#output' do
    it 'prints hello world' do
      expect(subject.output).to eq('Hello World!')
    end
  end
end
