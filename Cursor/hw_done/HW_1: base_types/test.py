# import string
# r =string.ascii_lowercase
# print(r[1])


print({key: value for key, value in enumerate(string.ascii_lowercase, 1)})



def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    pass

l2 = []
    lenght = len(listok)
    while lenght > 0:
        sp = None
        for r in listok:
            if sp == None:
                sp = r
            else:
                if r < sp:
                    sp = r
        l2.append(sp)
        listok.remove(sp)
    return l2