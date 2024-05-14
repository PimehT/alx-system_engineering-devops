# Define the Apache configuration variables
$apache_lock_dir = "/var/lock/apache2"
$apache_pid_file = "/var/run/apache2.pid"
$apache_run_user = "www-data"
$apache_run_group = "www-data"
$apache_log_dir = "/var/log/apache2"

# Ensure the lock directory exists
file { $apache_lock_dir:
  ensure => directory,
  owner  => $apache_run_user,
  group  => $apache_run_group,
  mode   => '0755',
}

# Ensure the PID file directory exists
file { File.dirname($apache_pid_file):
  ensure => directory,
  owner  => $apache_run_user,
  group  => $apache_run_group,
  mode   => '0755',
}

# Ensure the log directory exists
file { $apache_log_dir:
  ensure => directory,
  owner  => $apache_run_user,
  group  => $apache_run_group,
  mode   => '0755',
}

# Ensure Apache is configured with the correct variables
template { '/etc/apache2/apache2.conf':
  source => 'puppet:///modules/your_module/apache2.conf.erb',
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
  notify => Service['apache2'],
}

# Ensure the Apache service is enabled and running
service { 'apache2':
  ensure => running,
  enable => true,
}
