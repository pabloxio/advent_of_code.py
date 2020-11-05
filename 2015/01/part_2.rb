# Usage: From root folder
# $ ruby 2015/01/part_1.rb 2015/01/input

DIRS = {"(" => 1, ")" => -1}

def final_floor dirs
  dirs.inject(0){|loc, dir| loc + DIRS[dir]}
end

def reach_basement dirs, pos = 0
  return pos+1 if final_floor(dirs[0..pos]) == -1

  reach_basement(dirs, pos+1)
end

File.open(ARGV[0]).readlines.each do |line|
  puts reach_basement(line.strip.chars)
end