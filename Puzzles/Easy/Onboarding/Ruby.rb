# https://www.codingame.com/training/easy/onboarding

STDOUT.sync = true # DO NOT REMOVE

loop do
  e1 = gets.chomp
  d1 = gets.to_i
  e2 = gets.chomp
  d2 = gets.to_i
  puts d1<d2 ? e1 : e2
end
