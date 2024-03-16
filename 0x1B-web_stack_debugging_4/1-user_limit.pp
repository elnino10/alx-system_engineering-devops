# Change Operating System configuration to enable login and
# open file without an error message.

exec {'OS configuration':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}

