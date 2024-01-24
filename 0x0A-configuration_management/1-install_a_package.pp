# Install `flask` from `pip3`
# flask version must be `2.1.0`

# install flask with version 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# install werkzeug
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

