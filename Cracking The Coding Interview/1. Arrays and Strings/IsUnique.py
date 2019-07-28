"""
Is Unique: implement an algorithm to determine if a string has all unique values.
"""

# this solution levarages standard python library functions
def isUnique(s):
    return len(set(s)) == len(s)

def main():
    print(isUnique("SABY"))
    print(isUnique("SABHYA"))

if __name__ == "__main__":
    main()
