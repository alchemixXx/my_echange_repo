

data = [{'age': 43, 'name': 'denis', 'sex': 'male'},
              {'age': 49, 'name': 'Roman', 'sex': 'male'},
              {'age': 36, 'name': 'Godzilla', 'sex': 'male'},
              {'age': 47, 'name': 'spike', 'sex': 'female'},
              {'age': 31, 'name': 'SuperMan', 'sex': 'female'},
              {'age': 49, 'name': 'Batman', 'sex': 'male'},
              {'age': 37, 'name': 'claus', 'sex': 'male'},
              {'age': 55, 'name': 'Frank', 'sex': 'female'},
              {'age': 83, 'name': 'homer', 'sex': 'male'}
              ]

data2 = []
data3 = [1, 29, 5, 9]
data5 = "So the normal way you might go about doing this task in python is using a basic for loop:".split()
data6 =['Year', 'has', 12, 'months']
data7 = [[97, 34, -35, -80, 77, -19, 71], [76, -93, 36, -76, -1, -51], [-82, -12, 63, 48], [96, -89],
                      [-91, 10, 44, 17], [-55, -36, 93, -91], [-96]]
data8 = [97, 34, -35, -80, 77, -19, 71]
data9 = "Generators are iterators, but you can only iterate over them once."

value3 = 'SuperMan'

key6 = 'age'

# task 1
def task_1_fix_names_start_letter(data):
    # return [ for member in data]
    # print('Hello world')
    for member in data:
        member["name"] = member["name"].capitalize()
    # print(data)
    return data
    # pass



# # task 2
# redundant_keys = ['sex', 'name']
# for member in data:
#     for key in redundant_keys:
#         member.pop(key)
# print(data)


# task 3 - DONE

# value = 'SuperMan'
# result = None
# for member in data:
#     for exist_value in member.values():
#         if exist_value == value:
#             result = member
#             break
def task_3_find_item_via_value(data, value):


    # for member in data:
    #     if value in member.values():
    #         return [{key: value for key, value in member.items()}]

    # ((x for x in range(10) if x % 2 == i) for i in range(2))
    return [({key: value for key, value in member.items()}) for member in data if value in member.values()]

# task 4 - DONE

# x = min(data, key=data.get)
# def task_4_min_value_integers(data) -> int:
#     try:
#         return min([x['age'] for x in data])
#     except TypeError:
#         return min(data3)
#     except:
#         return None

# print(task_4_min_value_integers(data3))

# task 5 - DONE

# def test_task_5_valid_value(self):
#     given_data = "So the normal way you might go about doing this task in python is using a basic for loop:".split()
#     self.assertEqual(task_5_min_value_strings(given_data), 'a')

def task_5_min_value_strings(data) -> str:
    created_dict = {item:len(str(item)) for item in data}
    # min_value = min(created_dict.values())
    return list(created_dict.keys())[list(created_dict.values()).index(min(created_dict.values()))]
    # return min([len(str(x)) for x in data])
    # return list(created_dict.values()).index(min(created_dict.values()))
    # return list(created_dict.keys())    [list(created_dict.values()).       index(min(created_dict.values()))]
    #       ['So', 'the', 'normal',]        #[2, 3, 6, 3, 3]                         index of searched element
    # [list(created_dict.values()).index(min(created_dict.values()))]  ==> [15]



# task 6 - DONE

def task_6_min_value_list_of_dicts(data, key):
    # for member in data:
    #     print(member['age'])
    # new_min = min([member.get('age', None) for member in data])
    # return min([member.get('age', None) for member in data])
    minimal = min([member.get('age', None) for member in data if 'age' in member.keys()])

    # for member in data:
    #     if minimal in member.values():
    #         return member
    #
    return [member for member in data if minimal in member.values()][0]

    # return [({key: value for key, value in member.items()}) for member in data if minimal in member.values()]


    # return data[][list(member.values()).index(minimal)]

    # return new_min

# Task 7 - DONE

def task_7_max_value_list_of_lists(data) -> int:
    """
    Find max value from list of lists
    """
    # given_data = [[97, 34, -35, -80, 77, -19, 71], [76, -93, 36, -76, -1, -51], [-82, -12, 63, 48], [96, -89],
    #               [-91, 10, 44, 17], [-55, -36, 93, -91], [-96]]

    # new_list = []
    # for list in data:
    #     for item in list:
    #         new_list.append(item)

    #[item for sublist in l for item in sublist]

    # new_list = [item for sublist in data for item in sublist]
    return max([item for sublist in data for item in sublist])
    # return new_list
    # return max(new_list)
    # return max(new_list)

    # return [([item for item in list]) for list in data]

    # pass



def task_8_sum_of_ints(data) -> int:
    """
    Find sum of all items in given list
    """
    # print("hello world")
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
    pass

# print(task_1_fix_names_start_letter(data))
# print(task_6_min_value_list_of_dicts(data, key6))
# print(task_3_find_item_via_value(data, value3))
# print(task_5_min_value_strings(data6))
# print(task_7_max_value_list_of_lists(data7))
# print(task_8_sum_of_ints(data8))
print(task_9_sum_characters_positions(data9))