#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    x = False
    # CODE GOES HERE

    for i in range(0, (len(nums) - 2)):
        one = nums[i]
        two = nums[i + 1]
        three = nums[i + 2]
        if one == 1 and  two == 2 and three == 3:
            x = True
            break
    return x

#print(arrayCheck([1, 1, 2, 1, 2, 3])) #→ True


# arrayCheck([1, 1, 2, 3, 1])) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  # CODE GOES HERE
  new_str = str[0::2]
  return new_str

#print(stringBits("Heeololeo"))

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    # CODE GOES HERE
    a = a.lower()
    b = b.lower()
    lenght_a = len(a)
    lenght_b = len(b)
    if a >= b:
        if a[-lenght_b:] == b:
            return True
        else:
            return False
    else:
        if b[-lenght_a:] == a:
            return True
        else:
            return False

#print( end_other('abc', 'abXabe'))


#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
    # CODE GOES HERE
    new_str = ""
    for i in str:
        new_str += i * 2
    return new_str
#print(doubleChar('Hi-There'))

#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
     # CODE GOES HERE
     summ = fix_teen(a) + fix_teen(b) + fix_teen(c)
     return summ

def fix_teen(n):
     # CODE GOES HERE
     """
         THIS IS DOCSTRING
         takes in an int value and returns
         that value fixed for the teen rule
     """
     if n in range(13,15):
         n = 0
     elif n in range(17,20):
         n = 0;
     else:
         n = n
     return n

print(no_teen_sum(2, 1, 20))


#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    # CODE GOES HERE
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count

#print(count_evens([1, 3, 5, 2]))
