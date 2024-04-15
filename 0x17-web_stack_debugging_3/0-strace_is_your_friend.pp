# fix bad extension causing Apache error

exec { 'Worpress fix':
    command  => 'sed -i "s/phpp/php/g" var/www/html/wp-settings.php',
    path     => 'usr/local/bin/:/bin/'
}