# https://www.codingame.com/training/easy/next-car-license-plate

def plate_to_idx(p: str) -> int:
    def letter_duo_to_idx(d: str) -> int:
        return (ord(d[0]) - ord("A")) * 26 + (ord(d[-1]) - ord("A"))

    p_s = p.split("-")
    prefix, number, suffix = str(p_s[0]), int(p_s[1]), str(p_s[2])

    return (letter_duo_to_idx(prefix) * 676 + letter_duo_to_idx(suffix)) * 999 + (number - 1)


def idx_to_plate(i: int) -> str:
    def idx_to_letter_duo(i: int) -> str:
        a, b = divmod(i, 26)
        return chr(a + ord("A")) + chr(b + ord("A"))

    letters, number = divmod(i, 999)
    prefix, suffix = divmod(letters, 676)

    return "-".join([idx_to_letter_duo(prefix), str(number + 1).zfill(3), idx_to_letter_duo(suffix)])


plate, n = str(input()), int(input())

print(idx_to_plate(plate_to_idx(plate)+n))
