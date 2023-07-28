from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    h_index = 0
    citations = reversed(sorted(citations))
    
    for i, citation_count in enumerate(citations):
        if (citation_count >= (i + 1)) and citation_count >= 1:
            h_index += 1
    return h_index 


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
