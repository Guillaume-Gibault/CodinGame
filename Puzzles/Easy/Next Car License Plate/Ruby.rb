# https://www.codingame.com/training/easy/next-car-license-plate

def letter_duo_to_idx(d)
    (d[0].ord - "A".ord) * 26 + (d[-1].ord - "A".ord)
end

def plate_to_idx(p)
    prefix, num_str, suffix = p.split("-")
    number = num_str.to_i
    (letter_duo_to_idx(prefix) * 676 + letter_duo_to_idx(suffix)) * 999 + (number - 1)
end

def idx_to_letter_duo(i)
    a = i / 26
    b = i % 26
    (a + 'A'.ord).chr + (b + 'A'.ord).chr
end

def idx_to_plate(i)
    letters = i / 999
    number = i % 999
    prefix = letters / 676
    suffix = letters % 676
    [
        idx_to_letter_duo(prefix),(number + 1).to_s.rjust(3, '0'),
        idx_to_letter_duo(suffix)
    ].join('-')
end

plate = gets.chomp
n = gets.to_i

puts idx_to_plate(plate_to_idx(plate)+n)
