# fix the nginx configuration
exec { 'Update ulimit in nginx default config':
  command => 'sed -i "/^ulimit=-n/d;/^ulimit=/a ulimit=-n 4096" /etc/default/nginx',
  path    => ['/usr/bin', '/bin'],
}

exec { 'Restart nginx':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => Exec['Update ulimit in nginx default config'],
}
