
# Codewars 6 kyu challenge - 'Delete occurrences of an element if it occurs more than n times'.
# Delete occurrences of an element if it occurs more than n times


from collections import defaultdict

def delete_nth(lst, n):
    final_lst = []
    for elem in lst:
        if final_lst.count(elem) < n:
            final_lst.append(elem)
        else:
            continue
    return final_lst


delete_nth([20,37,20,21, 20],2)