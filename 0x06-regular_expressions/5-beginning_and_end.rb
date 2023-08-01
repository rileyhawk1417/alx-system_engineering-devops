#! /usr/bin/env ruby

# NOTE: This will select everything within a range
# ^ is the start of the range
# . includes characters found in the range
# $ marks the end of the range
puts ARGV[0].scan(/^h.n$/).join
