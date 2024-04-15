# increase both file limits for the holberton user

exec{ 'increase-hard-limits':
    command => "sed -i '/^holberton hard/s/5/5000/' /etc/security/limits.conf",
    path    => 'usr/local/bin/:/bin/'
}

exec{ 'increase-soft-limits':
    command => "sed -i '/^holberton soft/s/4/5000/' /etc/security/limits.conf",
    path    => 'usr/local/bin/:/bin/'
}
