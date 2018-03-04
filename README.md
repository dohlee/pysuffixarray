# pysuffixarray
Suffix array implementation in python.

## Usage
### pysuffixarray.core.SuffixArray(*string*)
Constructs a suffix array.
```python
from pysuffixarray.core import SuffixArray
sa = SuffixArray('MISSISSIPPI')
```

### SuffixArray.suffix_array()
Returns a suffix array.
```python
sa = SuffixArray('MISSISSIPPI')
sa.suffix_array()
>>> [11, 10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
```

### SuffixArray.longest_common_prefix()
Returns an array of longest common prefix(LCP).
LCP[i] contains the length of common prefix between SA[i] and SA[i-1].
```python
sa = SuffixArray('MISSISSIPPI')
sa.longest_common_prefix()
>>> [0, 0, 1, 1, 4, 0, 0, 1, 0, 2, 1, 3]
```

### SuffixArray.longest_repeated_substring()
Returns one of the longest repeated substrings within the string.
```python
sa = SuffixArray('MISSISSIPPI')
sa.longest_repeated_substring()
>>> 'ISSI'
```

