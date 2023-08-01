#! /usr/bin/env ruby
# NOTE: The question mark is meant to find one or more elements
# The '*' searches for anything within the case 
# anything else won't be picked
puts ARGV[0].scan(/hbt*n/).join
