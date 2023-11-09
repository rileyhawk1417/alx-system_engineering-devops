# Puppet manifest to fix wp-setings.php & solve Error 500

exec { 'resolve wp-settings':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
