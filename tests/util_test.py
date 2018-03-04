import random
import time

import pysuffixarray.util as util

def random_character():
    return ['A', 'C', 'G', 'T'][random.randint(0, 3)]

def given_short_string_when_asked_util_to_find_match_test():
    assert util.match('MISSISSIPPI', 'ISSI') == [1, 4]

def given_long_string_when_asked_to_find_match_test():
    long_string = ''.join([random_character() for _ in range(10**5)])
    pattern = ''.join([random_character() for _ in range(100)])
    
    start_time = time.time()
    util.match(long_string, pattern)
    end_time = time.time()

    assert end_time - start_time < 10  # Shoud done in 10 seconds.

def given_short_string_when_asked_util_to_find_longest_repeated_substring_test():
    assert util.longest_repeated_substring('MISSISSIPPI') == 'ISSI'

def given_short_string_when_asked_util_to_find_no_longest_repeated_substring_test():
    assert util.longest_repeated_substring('ABCD') == ''

def given_long_string_when_asked_util_to_find_longest_repeated_substring_test():
    long_string = ''.join([random_character() for _ in range(10**5)])
    pattern = 'X' * 1000

    # Embed two artificial patterns in the string.
    long_string += pattern
    long_string = long_string[:5000] + pattern + long_string[5000:] 
    
    start_time = time.time()
    match = util.longest_repeated_substring(long_string)
    end_time = time.time()

    assert end_time - start_time < 10  # Shoud be done in 10 seconds.
    assert long_string.count('X') == 2000, 'Long string does not contain valid patterns.'
    assert match == 'X' * 1000, 'Match should be length %d, but found %d' % (len(pattern), len(match))