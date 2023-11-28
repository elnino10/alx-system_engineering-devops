#!/usr/bin/env ruby
# script for 2-repetition_token_1

if ARGV.empty?
    puts ""
else
    input_string = ARGV[0]
    regex = /hb?tn/
    pattern_match = input_string.scan(regex)

    if pattern_match.empty?
        puts ""
    else
        puts "#{pattern_match.join("")}"
    end
end
