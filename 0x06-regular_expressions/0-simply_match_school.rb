#!/usr/bin/env ruby
regex = /School/

input = ARGV[0]

matches = input.scan(regex)

if matches.any?
  puts matches.join
else
  puts ""
end

