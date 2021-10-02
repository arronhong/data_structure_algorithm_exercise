"""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

{'2': 'abc',
 '3': 'def',
 '4': 'ghi',
 '5': 'jkl',
 '6': 'mno',
 '7': 'pqrs',
 '8': 'tuv',
 '9': 'wxyz'}
"""

from typing import List


def letter_combinations(digits: str) -> List[str]:
    """
    if input "23", return all abc and def combinations
    '' -> a -> ad
            -> ae
            -> af
       -> b -> bd
            -> be
            -> bf
       -> c -> cd
            -> ce
            -> cf
    time complexity: O(4^n), n is length of digits
    """
    if not digits:
        return []
    ans = []
    m = {'2': 'abc',
         '3': 'def',
         '4': 'ghi',
         '5': 'jkl',
         '6': 'mno',
         '7': 'pqrs',
         '8': 'tuv',
         '9': 'wxyz'}

    def back_tracking(pre, remaining):
        if not remaining:
            ans.append(pre)
            return
        for c in m[remaining[0]]:
            back_tracking(pre+c, remaining[1:])
    back_tracking('', digits)
    return ans


if __name__ == '__main__':
    assert ["ad","ae","af","bd","be","bf","cd","ce","cf"] == letter_combinations('23')
    assert [] == letter_combinations('')
    assert ["a","b","c"] == letter_combinations('2')
