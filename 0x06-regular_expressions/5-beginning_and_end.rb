#!/usr/bin/env ruby

regex = /^h.n$/

input = ARGV[0]

match = input.match(regex)

if match
  puts match[0]
else
  puts ""
end

