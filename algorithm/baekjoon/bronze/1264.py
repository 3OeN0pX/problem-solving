import sys
input = sys.stdin.readline

def is_vowel(char: str) -> bool:
    vowel = "aeiou"
    return char.lower() in vowel

def solve():
    lines = sys.stdin.readlines()
    count = 0

    for line in lines:
        clean_line = line.strip()
        if clean_line == "#":
            break
        
        for char in clean_line:
            if is_vowel(char):
                count += 1
        
        print(count)
        count = 0

if __name__ == "__main__":
    solve()