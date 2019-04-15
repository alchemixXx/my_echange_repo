from typing import List, Dict, Union, Generator
import random
import string

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    #pass
    for member in data:
        if 'name' in member:
            member["name"] = member["name"].capitalize()
    return data



def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for member in data:
        for key in redundant_keys:
            member.pop(key)
    return data
    # pass



def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    # for member in data:
    #     if value in member.values():
    #         return [{key: value for key, value in member.items()}]
    return [({key: value for key, value in member.items()}) for member in data if value in member.values()]




def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    # return min([x['age'] for x in data])
    # if len(data) != 0:
    #     return min([x['age'] for x in data])
    # pass
    try:
        return min([x['age'] for x in data])
    except TypeError:
        return min(data)
    except:
        return None


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    created_dict = {str(item):len(str(item)) for item in data}
    try:
        return list(created_dict.keys())[list(created_dict.values()).index(min(created_dict.values()))]
    except:
        return None

def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    # return min([member.get('age', None) for member in data if 'age' in member.keys()])
    # minimal = min([member.get('age', None) for member in data if 'age' in member.keys()])
    minimal = min([member.get('age', None) for member in data if 'age' in member.keys()])

    # for member in data:
    #     if minimal in member.values():
    #         return member
    return [member for member in data if minimal in member.values()][0]

    # pass


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    # new_list = []
    # for list in data:
    #     for item in list:
    #         new_list.append(item)
    # return max(new_list)
    return max([item for sublist in data for item in sublist])
    # pass


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data)
    # pass


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    return sum([ord(item) for item in text])
    # pass


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    i = 2
    yield i
    while True:
        i += 1
        if i == 3 or i == 5 or i == 7 or i == 11:
            yield i
        elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0:
            continue
        elif i > 200:
            break
        else:
            yield i
    # pass


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """
    return [random.choice(string.ascii_lowercase) for _ in range(20)]
    # pass
