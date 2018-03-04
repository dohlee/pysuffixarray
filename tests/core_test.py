import random
import time

import pysuffixarray.core as psa

def random_character():
    return ['A', 'C', 'G', 'T'][random.randint(0, 3)]

def given_short_string_when_asked_to_construct_suffix_array_test():
    short_string = 'MISSISSIPPI'

    start_time = time.time()
    sa = psa.SuffixArray(short_string)
    end_time = time.time()

    assert end_time - start_time < 1  # Shoud done in 1 seconds.
    assert sa.suffix_array() == [11, 10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]

def given_long_string_when_asked_to_asked_to_construct_suffix_array_test():
    long_string = ''.join([random_character() for _ in range(10**5)])  # String with 100,000 characters.

    start_time = time.time()
    psa.SuffixArray(long_string)
    end_time = time.time()

    assert end_time - start_time < 10  # Shoud be done in 10 seconds.

def given_short_string_when_asked_to_match_test():
    short_string = 'MISSISSIPPI'

    start_time = time.time()
    sa = psa.SuffixArray(short_string)
    end_time = time.time()

    assert end_time - start_time < 1  # Shoud be done in 1 seconds.
    assert sa.match('ISS') == [1, 4]

def given_short_string_when_asked_to_get_longest_common_prefix_test():
    short_string = 'MISSISSIPPI'

    start_time = time.time()
    sa = psa.SuffixArray(short_string)
    end_time = time.time()

    assert end_time - start_time < 1  # Shoud be done in 1 seconds.
    assert sa.longest_common_prefix() == [0, 0, 1, 1, 4, 0, 0, 1, 0, 2, 1, 3]

def given_short_string_when_asked_to_find_longest_repeated_substring_test():
    short_string = 'MISSISSIPPI'

    start_time = time.time()
    sa = psa.SuffixArray(short_string)
    end_time = time.time()

    assert end_time - start_time < 1  # Shoud be done in 1 seconds.
    assert sa.longest_repeated_substring() == 'ISSI'

