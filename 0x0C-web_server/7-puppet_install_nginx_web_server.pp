package { 'nginx':
  ensure => installed,
}

service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
}

file { '/var/www/html/custom404.html':
    ensure  => file,
    content => "Ceci n'est pas une page",
}

$config_content="
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name ;

        location / {
                try_files \$uri \$uri/ =404;
        }

        error_page 404 /custom_404.html;
        location = /custom_404.html {
                root /var/www/html;
                internal;
        }

        location /redirect_me {
            return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
}
"
file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => $config_content,
    require => Package['nginx'],
    notify  => Service['nginx'],
}
