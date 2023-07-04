#!/usr/bin/env ruby

regex = /School/

input = ARGV[0]

if input.match(regex)
  puts input
end