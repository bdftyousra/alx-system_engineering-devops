#!/usr/bin/env ruby

regex = /[A-Z]/

input = ARGV[0]

matches = input.scan(regex)

result = matches.join

if result.empty?
  puts ""
else
  puts result
end

