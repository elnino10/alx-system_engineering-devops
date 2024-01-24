# Install `flask` from `pip3`
# flask version must be `2.1.0`
 
$flask_package = 'flask'
$flask_version = '2.1.0'
$werkzeug_package = 'werkzeug'
$werkzeug_version = '2.1.1'

# install flask with version 2.1.0
package { $flask_package:
  ensure   => $flask_version,
  provider => 'pip3',
}

# install werkzeug
package { $werkzeug_package:
  ensure   => $werkzeug_version,
  provider => 'pip3',
}

