def isPalBitWise(s):
    p1, p2 = 0, len(s)-1
    while(p1 < p2):
        if ord(s[p1]) ^ ord(s[p2]) != 0:
            return False
        p1 += 1
        p2 -= 1
    return True


if __name__ == "__main__":
    print(isPalBitWise('racecar'))
    print(isPalBitWise('madam'))
    print(isPalBitWise('hello'))
