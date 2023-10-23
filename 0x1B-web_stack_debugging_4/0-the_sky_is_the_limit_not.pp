# increases the upper limit and restart nginx
exec { 'increase upper limit':
  provider => shell,
  command  => 'sed -i s/15/1000000/ /etc/default/nginx'
}
exec { 'restart nginx server':
  provider => shell,
  command  => 'service nginx restart'
}
