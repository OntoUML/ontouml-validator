"""General functions to be used across the code."""


def intersection_lists(list1: list, list2: list) -> list:
    """Find the intersection of two lists.

    This function takes two input lists and returns a new list containing
    the elements that are common to both input lists.

    :param list1: The first list.
    :type list1: list
    :param list2: The second list.
    :type list2: list
    :return: A list containing the common elements of list1 and list2.
    :rtype: list
    """
    set1 = set(list1)
    set2 = set(list2)

    return list(set1.intersection(set2))
