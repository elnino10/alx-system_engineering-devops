#!/usr/bin/env ruby
# script for 7-OMG_WHY_ARE_YOU_SHOUTING

if ARGV.empty?
    puts ""
else
    input_string = ARGV[0]
    regex = /[A-Z]/
    pattern_match = input_string.scan(regex)

    if pattern_match.empty?
        puts ""
    else
        puts "#{pattern_match.join("")}"
    end
end
