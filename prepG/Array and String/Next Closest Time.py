# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

 

# Example 1:

# Input: time = "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:

# Input: time = "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
 

# approach

# eg: "19:34"
# hour : "19"
# minute : "34"

# after_merger = sorted(hour + minute) = "1934"

# all_possibilities = [i+j for i in nums for j in nums] = ['11', '13', '14', '19', '31', '33', '34', '39', '41', '43', '44', '49', '91', '93', '94', '99']

# now first check for minute
# Find the index where minute (34 is present)
# at index 6 "34" is present, now check whether the value at index 7 is not out of range and value is < 60
# if yes return hour + all_possibilities[7] --> 19:39


# Similarly for hour : find index and then next index inside range and value < 24 


# At last if both not true
# then return the first time possible in the next day
# Eg: "23:59"
# hour : 23
# minute : 59
# all = [22,23,.............]
# for both minute and hour the condition will fail
# so return "22:22"  (smallest time next day)



class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour, minute = time.split(":")
        
        # Generate all possible 2 digit values
        # There are at most 16 sorted values here
        nums = sorted(set(hour + minute))
        two_digit_values = [a+b for a in nums for b in nums]

        # Check if the next valid minute is within the hour
        i = two_digit_values.index(minute)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "60":
            return hour + ":" + two_digit_values[i+1]

        # Check if the next valid hour is within the day
        i = two_digit_values.index(hour)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < "24":
            return two_digit_values[i+1] + ":" + two_digit_values[0]
        
        # Return the earliest time of the next day
        return two_digit_values[0] + ":" + two_digit_values[0]