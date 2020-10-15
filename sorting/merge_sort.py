class MergeSort:

    @staticmethod
    def merge(first_list: list, second_list: list, result: list) -> None:
        """
        Merge two sorted Python lists S1 and S2 into properly sized list S.
        """
        i = j = 0
        while i + j < len(result):
            if j == len(second_list) or (i < len(first_list) and first_list[i] < second_list[j]):
                result[i + j] = first_list[i]  # copy ith element of S1 as next item of S
                i += 1
            else:
                result[i + j] = second_list[j]  # copy jth element of S2 as next item of S
                j += 1

    @staticmethod
    def merge_sort(target: list) -> None:
        """
        Sort the elements of Python list S using the merge-sort algorithm.
        """
        n = len(target)
        if n < 2:
            return  # list is already sorted
        # divide
        mid = n // 2
        first_half = target[0:mid]  # copy of first half
        second_half = target[mid:n]  # copy of second half
        # conquer (with recursion)
        MergeSort.merge_sort(first_half)  # sort copy of first half
        MergeSort.merge_sort(second_half)  # sort copy of second half
        # merge results
        MergeSort.merge(first_half, second_half, target)  # merge sorted halves back into S
