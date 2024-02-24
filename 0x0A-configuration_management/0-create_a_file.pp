# This is a manifest specifying the creation of a file

file { 'school'
    path => '/tmp/school',
    mode => '0744',
    owner => 'www-data',
    group => 'www-data',
    content => 'I love Puppet'
}
