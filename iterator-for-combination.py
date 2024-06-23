from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations: list = self.generate_combinations(characters, combinationLength)
        self.combinations_len: int = len(self.combinations)
        self.ptr: int  = 0

    def generate_combinations(self, s, length):
        # Ensure the string is sorted to get combinations in lexicographical order
        sorted_s = ''.join(sorted(s))

        # Generate combinations of the specified length
        comb_list = [''.join(comb) for comb in combinations(sorted_s, length)]

        return comb_list

    def next(self) -> str:
        if self.hasNext():
            self.ptr += 1
            return self.combinations[self.ptr - 1]

        return ""

    def hasNext(self) -> bool:
        if self.ptr >= self.combinations_len :
            return False

        return True


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self._comb_list = []
        self._cur_pos  = 0

        def comb(f: str, c: str):
            if len(f) == combinationLength:
                self._comb_list.append(f)
                return
            if len(c) == 0: return
            comb(f + c[0],
                 c[1:] if len(c) > 1 else "")
            comb(f,
                 c[1:] if len(c) > 1 else "")
            return
        comb("", characters)

    def next(self) -> str:

        e = self._comb_list[self._cur_pos]
        self._cur_pos += 1
        return e

    def hasNext(self) -> bool:
        return self._cur_pos < len(self._comb_list)


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def comb(chars, l):
            res = []
            def backtrack(i):
                if len(res) == l:
                    yield "".join(res)
                for j in range(i, len(chars)):
                    res.append(chars[j])
                    yield from backtrack(j + 1)
                    res.pop()
            yield from backtrack(0)

        self.values = comb(characters, combinationLength)
        self.cur = next(self.values, None)

    def next(self) -> str:
        res, self.cur = self.cur, next(self.values, None)
        return res

    def hasNext(self) -> bool:
        return self.cur is not None


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        l = []
        chars = list(characters)
        N = 2 ** len(characters)

        for i in range(N):
            nums = list(str(bin(i)).replace('0b','').zfill(len(chars)))
            if (list(nums).count('1') == combinationLength):
                ans = [int(nums[j]) * chars[j] for j in range(len(chars))]
                final = ''.join(ans)
                l.append(final)

        l.sort()
        self.p = l
        self.itr = 0
        self.end = len(l)


    def next(self) -> str:
        i = self.itr
        x = self.p[i]
        i += 1
        self.itr = i
        return x

    def hasNext(self) -> bool:
        return self.itr < self.end


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()