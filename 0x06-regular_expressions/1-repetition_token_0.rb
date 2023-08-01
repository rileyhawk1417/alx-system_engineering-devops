#! /usr/bin/env ruby
#Match 2-5 characters of the letter 't'
puts ARGV[0].scan(/hbt{2,5}n/).join
