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


exec {'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.duckduckgo.com permanent;" /etc/nginx/sites-enabled/default':
provider => shell,
}

exec {'run':
command  => 'sudo service nginx restart',
provider => shell,
}



