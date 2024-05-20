# fix error in Apache benchmark
exec { 'Update ulimit in nginx default config':
  command => "/bin/echo ULIMIT='-n 4096' > /etc/default/nginx && /usr/bin/sudo\
  service nginx restart"
}