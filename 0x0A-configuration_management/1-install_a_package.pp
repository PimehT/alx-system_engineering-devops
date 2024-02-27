# Use puppet to install the software package Flask 2.1.0 from pip3

package { 'install flask':
  ensure    => '2.1.0',
  provider  => 'pip3',
}