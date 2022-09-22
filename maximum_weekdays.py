'''
Given a list with N different integers, with each of those integers representing a day in the "day of the year" format (e.g. 1 = January 1st, 33 = February 2nd), 
your task is to output the maximum number of those days that can simultaneously be weekdays (Monday, Tuesday, Wednesday, Thursday or Friday).
Taking the the days 1, 4, 5 and 6 as an example, if Jan 1st falls on a Friday, then days 1, 4, 5 and 6 would fall on Friday, Monday, Tuesday and Wednesday respectively 
(in this case the expected answer would be 4).
On the other hand, taking the days 1, 3, 5, and 6 as an example, at least one of these will always fall on an weekend, regardless of which day of the week Jan 1st falls on 
(in this case the expected answer would be 3).

Input
Line 1: An integer N for the number of days.
Line 2: N different space separated integers D in ascending order.
Output
The maximum number of the given days that can simultaneously be weekdays.
'''
