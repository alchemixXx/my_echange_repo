from typing import Any

class OurAwesomeException(Exception):
    pass



def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise OurAwesomeException

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        OurAwesomeException

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
#     # try:
#     if (type(first_value) == int or type(first_value) == float or type(first_value) == str) and \
#             (type(second_value) == int or type(second_value) == float or type(second_value) == str):
#         return int(first_value) * int(second_value)
#     else:
#         raise OurAwesomeException
#     # except OurAwesomeException:
#     #     print("Not valid input data")
#
#
# multiple_ints_with_conversion(True, 2)


# first = 120
# print(type(first))
# # first = int(first)
# # print(type(first))
#
#
# if 120 == int(first):
#     print('yes')



new_dict = {1 : "privet", "bab": "asdasda"}
print(new_dict)