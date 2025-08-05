# https://www.codingame.com/training/easy/temperatures

n = gets.to_i
t = gets.split.map(&:to_i)

if t.empty?
  puts 0
else
  o = 5526
  t.each do |temp|
    if temp.abs == o.abs
      o = [temp, o].max
    elsif temp.abs < o.abs
      o = temp
    end
  end
  puts o
end
