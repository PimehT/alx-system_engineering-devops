# Use puppet to install the software package Flask 2.1.0 from pip3

exec {
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/usr/bin'],
  environment => ['HOME=/root'],
  require     => Package['python3-pip'],
}