#! /usr/bin/env ruby
# NOTE: The question mark is meant to find one or more elements
# The '+' just increments the search after the character
# in this case the letter 't'
puts ARGV[0].scan(/hbt+n/).join
