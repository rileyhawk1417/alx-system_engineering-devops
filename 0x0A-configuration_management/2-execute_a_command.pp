# Execute pkill command in ruby
exec {'pkill':
command => 'pkill -9 -f killmenow',
path    => ['/usr/bin', '/bin'],
}
