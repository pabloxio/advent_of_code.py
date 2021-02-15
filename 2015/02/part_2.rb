# Usage: From root folder
# $ ruby 2015/02/part_2.rb 2015/02/input

class Present
  def initialize(dimensions)
    @dimensions = dimensions.split("x").map{|d| d.to_i}
  end

  def required_ribbon
    smallest_perimeter + volume
  end

  def self.required_ribbon_for_all(presents)
    presents.map{|p| Present.new(p).required_ribbon}.reduce(:+)
  end

  private

  def smallest_perimeter
    sides.map{|a, b| 2 * a + 2 *b}.min
  end

  def volume
    @dimensions.reduce(:*)
  end

  def sides
    @dimensions.combination(2).to_a
  end
end

puts Present.required_ribbon_for_all(File.open(ARGV[0]).readlines)
