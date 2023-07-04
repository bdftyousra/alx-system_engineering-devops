#!/usr/bin/env ruby

log_file = ARGV[0]

File.open(log_file, 'r') do |file|
  file.each_line do |line|
    match = line.match(/\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/)
    if match
      sender = match[1]
      receiver = match[2]
      flags = match[3]
      puts "#{sender},#{receiver},#{flags}"
    end
  end
end

