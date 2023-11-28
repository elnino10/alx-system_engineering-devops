#!/usr/bin/env ruby
# script for 6-phone_number

if ARGV.empty?
    puts ""
else
    input_string = ARGV[0]
    regex = /^[0-9]{10}$/
    pattern_match = input_string.scan(regex)

    if pattern_match.empty?
        puts ""
    else
        puts "#{pattern_match.join("")}"
    end
end
