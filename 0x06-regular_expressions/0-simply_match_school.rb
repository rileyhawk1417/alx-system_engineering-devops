#! /usr/bin/env ruby

=begin
#NOTE: This code still doesnt behave well.
So a one liner is better
name = ARGV[0]
counter = 0
while ARGV do
  if "#{name}".match(/School/)
    puts ARGV[counter].scan(/School/).join
    break
  else
    break
  end
end
=end
puts ARGV[0].scan(/School/).join
