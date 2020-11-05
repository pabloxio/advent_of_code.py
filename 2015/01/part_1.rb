# Usage: From root folder
# $ ruby 2015/01/part_1.rb 2015/01/input

DIRS = {"(" => 1, ")" => -1}

def final_floor dirs
  dirs.inject(0){|loc, dir| loc + DIRS[dir]}
end

File.open(ARGV[0]).readlines.each do |line|
  puts final_floor(line.strip.chars)
end