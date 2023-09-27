# Install nginx, configure root, configure redirect & restart the server

package {'nginx':
ensure => 'present',
}

exec {'install':
command  => 'sudo apt-get update -y; sudo apt-get install nginx -y;',
provider => shell,
}

exec {'Hello World!':
command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
provider => shell,
}

exec {'run':
command  => 'sudo service nginx restart',
provider => shell,
}


