#! /usr/bin/env ruby

# NOTE: This will select everything within a range
# [A-Z] only looks for caps
# * finds everything else after
puts ARGV[0].scan(/[A-Z]*/).join
