

def sort(suffix_array, rank_array, string_len, k):
    max_length = max(2**7 - 1, string_len)
    count = [0] * max_length

    for i in range(len(rank_array)):
        if i + k < string_len:
            count[rank_array[i + k]] += 1
        else:
            count[0] += 1

    cumsum = 0
    for i in range(max_length):
        t = count[i]
        count[i] = cumsum
        cumsum += t

    temp_suffix_array = [-1] * string_len
    for i in range(len(suffix_array)):
        if suffix_array[i] + k < string_len:
            target_index = rank_array[suffix_array[i] + k]
        else:
            target_index = 0

        temp_suffix_array[count[target_index]] = suffix_array[i]
        count[target_index] += 1

    return temp_suffix_array

def rerank(suffix_array, rank_array, k):
    temp_rank_array = [0] * len(rank_array)
    r, s = rank_array, suffix_array

    rank = 0
    for i in range(1, len(rank_array)):
        if r[s[i]] == r[s[i-1]] and r[s[i] + k] == r[s[i-1] + k]:
            temp_rank_array[s[i]] = rank
        else:
            rank += 1
            temp_rank_array[s[i]] = rank

    return temp_rank_array

def suffix_array(string):
    string += '$'

    string_len = len(string)
    suffix_array = list(range(string_len))
    rank_array = [ord(c) for c in string]

    k = 1
    while k < string_len:
        suffix_array = sort(suffix_array, rank_array, string_len, k)
        suffix_array = sort(suffix_array, rank_array, string_len, 0)
        rank_array = rerank(suffix_array, rank_array, 1)
        k *= 2

    return suffix_array

def random_char():
    import random
    return ['A', 'T', 'G', 'C'][random.randint(0, 3)]

if __name__ == '__main__':
    suffix_array = suffix_array(''.join([random_char() for _ in range(10**5)]))
    # suffix_array = suffix_array('GATAGACA')
    # print(suffix_array)


