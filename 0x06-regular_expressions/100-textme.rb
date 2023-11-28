#!/usr/bin/env ruby
# script that extracts sender, receiver, and flags

if ARGV.empty?
    puts ""
else
    input_string = ARGV[0]
    regex = /\[from:([a-zA-Z0-9\+\-\:]*)\]|\[to:([a-zA-Z0-9\+\-\:]*)\]|\[flags:([a-zA-Z0-9\+\-\:]*)\]/

    matches = input_string.scan(regex)
    if matches.empty?
        puts ""
    else
        matches.each_with_index do |match, index|
            if index != 2
                print "#{match.join("")},"
            else
                print "#{match.join("")}"
            end
        end
        print "\n"
    end
end
