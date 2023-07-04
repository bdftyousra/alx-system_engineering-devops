#!/usr/bin/env ruby

regex = /hbt+n/

input = ARGV[0]

match = input.match(regex)

if match
  puts match[0]
else
  puts ""
end
