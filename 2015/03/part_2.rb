# Usage: From root folder
# $ ruby 2015/03/part_2.rb 2015/03/input

class Position
  def initialize
    @x, @y = [0, 0]
  end

  def get_key
    "#{@x}#{@y}"
  end

  def move direction
    case direction
    when "<"
      @x-=1
    when ">"
      @x+=1
    when "^"
      @y+=1
    when "v"
      @y-=1
    end
  end
end

File.open(ARGV[0]).readlines.each do |directions|
  santa  = Position.new
  robo_santa  = Position.new
  houses = {santa.get_key => true}

  directions.split("").each_slice(2) do |dir_santa, dir_robo|
    santa.move dir_santa
    houses[santa.get_key] = true

    robo_santa.move dir_robo
    houses[robo_santa.get_key] = true
  end

  puts(houses.size)
end
