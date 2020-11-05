# Usage: From root folder
# $ ruby 2019/01/part_1.rb 2019/01/input

def required_fuel mass
  (mass.to_i/3).floor - 2
end

puts File.open(ARGV[0]).readlines.inject(0){|sum, n| sum + required_fuel(n)}