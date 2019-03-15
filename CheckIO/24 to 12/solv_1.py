def time_converter(time):
    new_time = ""
    work = time.split(":")
    if int(work[1]) == 0:
        mins = "00"
    else:
        mins = work[1]
    if int(work[0]) == 0 and int(work[1]) == 0:
        new_time = "12:00 a.m."
    elif int(work[0]) <= 12:
        if int(work[0]) == 12:
            new_time = work[0] + ":" + mins + " p.m."
        else:
            new_time = str(int(work[0])) + ":" + mins + " a.m."
    else:
        new_time = str(int(work[0]) - 12) + ":" + mins + " p.m."
    return new_time




    # work[0] = int(work[0])
    # if work[0] <= 12:
    #     if int(work[1]) < 30:
    #         return (str(work[0]) + ":" + work[1] + ' a.m.')
    #     elif work[0] == 0:
    #         return ("12:" + work[1] + ' a.m.')
    #     else:
    #         return (str(work[0]) + ":" + work[1] + ' p.m.')
    # else:
    #     return ((str(work[0] - 12)) + ":" + str(work[1]) + ' p.m.')


print(time_converter("15:30"))
# if __name__ == '__main__':
#     print("Example:")
#     print(time_converter('00:00'))
#
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert time_converter('12:30') # == '12:30 p.m.'
#     assert time_converter('09:00') # == '9:00 a.m.'
#     assert time_converter('23:15') # == '11:15 p.m.'
#     print("Coding complete? Click 'Check' to earn cool rewards!")
