control 'Birthday App testing - PUT Request' do
  title 'Automation testing'
  desc  'TEST Bday App - Automation testing'

  describe http('http://localhost:7777/hello/anand',
                method: 'PUT',
                headers: {'Content-Type' => 'application/json'},
                data: '{"dateOfBirth": "2018-07-08"}') do
    its('status') { should cmp 204 }
  end

  describe http('http://localhost:7777/hello/anand124',
    method: 'PUT',
    headers: {'Content-Type' => 'application/json'},
    data: '{"dateOfBirth": "2018-07-08"}') do
      its('status') { should cmp 400 }
  end

  describe json(content: http('http://localhost:7777/hello/anand124',
                method: 'PUT',
                headers: {'Content-Type' => 'application/json'},
                data: '{"dateOfBirth": "2018-07-08"}').body) do
    its('message') { should eq "Username shoud contains only letters" }
  end

  describe http('http://localhost:7777/hello/anand',
    method: 'PUT',
    headers: {'Content-Type' => 'application/json'},
    data: '{"dateOfBirth": "2018/07/08"}') do
    its('status') { should cmp 400 }
  end
end

control 'Birthday App testing - GET Request' do
  title 'Automation testing'
  desc  'TEST Bday App - Automation testing'

  describe http('http://localhost:7777/hello/anand') do
    its('status') { should cmp 200 }
  end

  describe http('http://localhost:7777/hello/anand124') do
      its('status') { should cmp 400 }
  end

  describe json(content: http('http://localhost:7777/hello/anand124').body) do
    its('message') { should eq "username anand124 not found" }
  end
end
