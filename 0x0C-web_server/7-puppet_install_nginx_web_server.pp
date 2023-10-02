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


exec {"sudo sed -i 's/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.duckduckgo.com\/;\\n\\t}/' /etc/nginx/sites-available/default":
provider => shell,
}

exec {'run':
command  => 'sudo service nginx restart',
provider => shell,
}



