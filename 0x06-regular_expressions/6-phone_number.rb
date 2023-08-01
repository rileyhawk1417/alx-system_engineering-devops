#! /usr/bin/env ruby

# NOTE: This will select everything within a range
# \d only look for digits
# ^ is the start of the range
# $ marks the end of the range
puts ARGV[0].scan(/^\d{10,10}$/).join
