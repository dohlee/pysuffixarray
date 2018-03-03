from core import SuffixArray

def match(string, pattern):
    return SuffixArray(string).match(pattern)

def longest_common_prefix(string):
    return SuffixArray(string).longest_common_prefix()

def longest_repeated_substring(string):
    return SuffixArray(string).longest_repeated_substring()

if __name__ == '__main__':
    print(longest_repeated_substring('MISSISSIPPI'))
