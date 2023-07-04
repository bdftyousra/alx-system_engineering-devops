#!/usr/bin/env ruby

regex = /hbt{2,5}n/

input = ARGV[0]

match = input.match(regex)

if match
  puts match[0]
else
  puts ""
end
