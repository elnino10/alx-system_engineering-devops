#!/usr/bin/env ruby
# script for 5-beginning_and_end

if ARGV.empty?
    puts ""
else
    input_string = ARGV[0]
    regex = /^h.n$/
    pattern_match = input_string.scan(regex)

    if pattern_match.empty?
        puts ""
    else
        puts "#{pattern_match.join("")}"
    end
end
