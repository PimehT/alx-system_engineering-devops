# Create a file in /tmp with some requirements in its
# path, permission mode, owner, group, and content

file {'/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content =>'I love Puppet',
}