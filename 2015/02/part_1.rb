# Usage: From root folder
# $ ruby 2015/02/part_1.rb 2015/02/input

class Present
  def initialize(dimensions)
    @dimensions = dimensions.split("x").map{|d| d.to_i}
  end

  def required_paper
    sides.reduce(0){|sum, side|sum+2*side.reduce(:*)} + smallest_side_area
  end

  def self.required_paper_for_all(presents)
    presents.map{|p| Present.new(p).required_paper}.reduce(:+)
  end

  private

  def smallest_side_area
    sides.map{|a, b| a*b}.min
  end

  def sides
    @dimensions.combination(2).to_a
  end
end

puts Present.required_paper_for_all(File.open(ARGV[0]).readlines)
