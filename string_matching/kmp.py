class KMP:

    @staticmethod
    def find(target: str, substring: str):
        """Return the lowest index of T at which substring P begins (or else -1)."""
        n, m = len(target), len(substring)  # introduce convenient notations
        if m == 0: return 0  # trivial search for empty string
        fail = KMP.compute_kmp_fail(substring)  # rely on utility to precompute
        j = 0  # index into text
        k = 0  # index into pattern
        while j < n:
            if target[j] == substring[k]:  # P[0:1+k] matched thus far
                if k == m - 1:  # match is complete
                    return j - m + 1
                j += 1  # try to extend match
                k += 1
            elif k > 0:
                k = fail[k - 1]  # reuse suffix of P[0:k]
            else:
                j += 1
        return -1  # reached end without match

    @staticmethod
    def compute_kmp_fail(value: str):
        """Utility that computes and returns KMP 'fail' list."""
        m = len(value)
        fail = [0] * m  # by default, presume overlap of 0 everywhere
        j = 1
        k = 0
        while j < m:  # compute f(j) during this pass, if nonzero
            if value[j] == value[k]:  # k + 1 characters match thus far
                fail[j] = k + 1
                j += 1
                k += 1
            elif k > 0:  # k follows a matching prefix
                k = fail[k - 1]
            else:  # no match found starting at j
                j += 1
        return fail
