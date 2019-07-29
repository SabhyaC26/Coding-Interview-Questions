"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to 
hold the additional characters, and that you are given the "true" length of the string.

Note: this question is really trivially with Python, so I'll try to do a java implementation as well.
"""


def URLify(s):
    return s.replace(' ', '%20')

def main():
    print(URLify("sabhya chhabria cornell university"))

if __name__ == "__main__":
    main()
