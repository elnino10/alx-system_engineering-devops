#!/usr/bin/env ruby
# script for repetition token

if ARGV.empty?
    puts ""
else
    input_string = ARGV[0]
    regex = /hbt{2,5}n/

    pattern_match = input_string.scan(regex)
    if pattern_match.empty?
        puts ""
    else
        puts "#{pattern_match.join("")}"
    end
end
