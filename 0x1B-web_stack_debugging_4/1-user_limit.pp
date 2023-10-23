# remove upper limit
exec { 'remove upper limit':
  provider => shell,
  command  => 'sed -i s/holberton/"# holberton"/ /etc/security/limits.conf'
}
