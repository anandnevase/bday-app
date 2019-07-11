control 'Birthday App testing - PUT Request' do
  title 'Automation testing'
  desc  'TEST Bday App - Automation testing'

  describe http('http://localhost:7777/hello/anand',
                method: 'PUT',
                headers: {'Content-Type' => 'application/json'},
                data: '{"dateOfBirth": "2018-07-08"}') do
    its('status') { should cmp 204 }
    #its('body') { should eq 'username successfully updated!' }
  end

  describe http('http://localhost:7777/hello/anand124',
    method: 'PUT',
    headers: {'Content-Type' => 'application/json'},
    data: '{"dateOfBirth": "2018-07-08"}') do
      its('status') { should cmp 400 }
      #its('body') { should eq "{'message':'Username shoud contains only letters'}" }
  end

  describe http('http://localhost:7777/hello/anand',
    method: 'PUT',
    headers: {'Content-Type' => 'application/json'},
    data: '{"dateOfBirth": "2018/07/08"}') do
    its('status') { should cmp 400 }
    #its('body') { should eq "{'message':'Username shoud contains only letters'}" }
  end
end
