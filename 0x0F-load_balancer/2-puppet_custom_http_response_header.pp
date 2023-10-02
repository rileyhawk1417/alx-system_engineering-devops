# Use puppet to write custom headers for nginx
# Its possible to use chained tasks that depend on each other

exec {'apt_update':
command => '/usr/bin/apt-get update',
}
package {'nginx':
ensure => 'present'
}

file_line {'set custom http header':
path  => '/etc/nginx/sites-enabled/default',
match => 'server_name _;'
line  => "server_name _;\n\tadd_header X-Served-By \'${hostname}';"
}

exec {'restart nginx':
command => 'usr/sbin/service nginx restart'
}


