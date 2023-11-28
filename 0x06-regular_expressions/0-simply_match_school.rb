#!/usr/bin/env ruby
# regular expression matching school

if ARGV.empty?
    puts ""
else
    input_string = ARGV[0]
    regex = /School/

    pattern_match = input_string.scan(regex)

    if pattern_match.empty?
        puts ""
    else
        puts "#{pattern_match.join("")}"
    end
end
