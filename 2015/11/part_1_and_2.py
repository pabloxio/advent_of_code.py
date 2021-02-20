#  Usage: From root folder
#  $ python 2015/11/part_1_and_2.py INPUT
#
#  Tests:
#  $ python -m doctest 2015/11/part_1_and_2.py

import sys
import re


class SantaNumber:
    """
    >>> sp = SantaNumber("a")
    >>> sp + 1
    0
    >>> sp = SantaNumber("z")
    >>> sp + 1
    1
    >>> str(sp)
    'a'
    >>> sp = SantaNumber("h")
    >>> sp + 1
    0
    >>> str(sp)
    'i'
    """

    def __init__(self, letter: str):
        self.letter = ord(letter)

    def __add__(self, increment: str = 1) -> int:
        self.letter = self.letter + increment
        if self.letter > 122:
            self.letter = 97
            return 1
        return 0

    def __str__(self):
        return chr(self.letter)

    def __int__(self):
        return self.letter


class SantaPassword:
    """
    >>> sp = SantaPassword("abcdefgh")
    >>> while not sp.valid():
    ...     sp.count()
    ...
    >>> print(sp)
    abcdffaa
    >>> sp = SantaPassword("ghijklmn")
    >>> while not sp.valid():
    ...     sp.count()
    ...
    >>> print(sp)
    ghjaabcc
    >>> sp = SantaPassword("hepxcrrq")
    >>> while not sp.valid():
    ...     sp.count()
    ...
    >>> print(sp)
    hepxxyzz
    >>> sp = SantaPassword("hepxxyzz")
    >>> sp.count()
    >>> while not sp.valid():
    ...     sp.count()
    ...
    >>> print(sp)
    heqaabcc
    """

    def __init__(self, pwd):
        self.pwd = [SantaNumber(l) for l in pwd]

    def count(self):
        """
        >>> sp = SantaPassword("hijklmmn")
        >>> sp.count()
        >>> print(sp)
        hjaaaaaa
        >>> sp = SantaPassword("aiaabbbb")
        >>> sp.count()
        >>> print(sp)
        ajaaaaaa
        >>> sp = SantaPassword("abcdefgh")
        >>> sp.count()
        >>> print(sp)
        abcdefgj
        >>> sp = SantaPassword("abcdefga")
        >>> sp.count()
        >>> print(sp)
        abcdefgb
        """
        temp = 1
        for sn in reversed(self.pwd):
            temp = sn + temp

        match = re.search("[iol]", str(self))
        if match:
            start = match.start()
            self.pwd[start] + 1
            self.pwd = self.pwd[0 : start + 1] + [
                SantaNumber("a") for _ in self.pwd[start + 1 :]
            ]

    def valid(self) -> bool:
        """
        >>> SantaPassword("hijklmmn").valid()
        False
        >>> SantaPassword("abbceffg").valid()
        False
        >>> SantaPassword("abbcegjk").valid()
        False
        >>> SantaPassword("abcdffaa").valid()
        True
        >>> SantaPassword("ghjaabcc").valid()
        True
        """
        return (
            self._policy_three_straight_letters()
            and self._policy_not_iol()
            and self._policy_pairs_letters()
        )

    def _policy_three_straight_letters(self) -> bool:
        temp = [int(sp) for sp in self.pwd]
        for i in range(len(temp) - 2):
            if temp[i] + 1 == temp[i + 1] and temp[i + 1] + 1 == temp[i + 2]:
                return True
        return False

    def _policy_not_iol(self) -> bool:
        return not bool(re.search("[iol]", str(self)))

    def _policy_pairs_letters(self) -> bool:
        return len(re.findall(r"([a-z])\1", str(self))) == 2

    def __str__(self):
        return "".join([str(np) for np in self.pwd])


if __name__ == "__main__":
    sp = SantaPassword(sys.argv[1])
    sp.count()
    while not sp.valid():
        sp.count()
    print(sp)
