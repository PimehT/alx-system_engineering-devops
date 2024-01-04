#!/usr/bin/env ruby
# Auth:Pimeh

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
