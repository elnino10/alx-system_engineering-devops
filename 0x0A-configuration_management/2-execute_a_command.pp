# kill the process killmenow
exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => '/usr/bin/:/bin/',
}

