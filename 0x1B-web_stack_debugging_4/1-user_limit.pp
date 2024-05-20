# increase the user limit
exec { 'increase the user limit':
  command => '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf',
}