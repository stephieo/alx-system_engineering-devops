# puppet file to automate configuration of Nginx server (http response)

exec { 'apt-update':
  command => 'sudo apt-get -y update',
  provider=> shell,
  before  => Package['nginx']
#   path    => ['/usr/bin', '/bin'],
}

package { 'nginx':
  ensure => installed,
  require   => Exec['update'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

exec { 'restart_server':
  provider => shell,
  command  => '/usr/sbin/service nginx restart',
}

service { 'nginx':
  ensure => running,
}