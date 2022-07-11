"""Factor Of 3 Codevita 9 Solution
Problem Description
Given an array arr, of size N, find whether it is possible to rearrange the elements of array such that sum of no two adjacent elements is divisible by 3.

Constraints
1 <= T <= 10

2 <= N <= 10^5

1 <= arr[i] <= 10^5

Input
First line contains integer T denoting the number of testcases.

Each test cases consists of 2 lines as follows-

First line contains integer N denoting the size of the array.

Second line contains N space separated integers.

Output
For each test case print either ""Yes"" or ""No"" (without quotes) on new line.

Time Limit
1

Examples
Example 1

Input

1

4

1 2 3 3

Output

Yes

Explanation

Some of the rearrangements can be {2,1,3,3}, {3,3,1,2}, {2,3,3,1}, {1,3,3,2},...

We can see that there exist at least 1 combination {3,2,3,1} where sum of 2 adjacent number is not divisible by 3. Other combinations can be {1,3,2,3}, {2,3,1,3}.

Hence the output is Yes.

Example 2

Input

1

4

3 6 1 9

Output

No

Explanation

All possible combination of {3,6,1,9} are

{1,3,6,9}, {1,3,9,6}, {1,6,9,3}, {1,6,3,9}, {1,9,3,6}, {1,9,6,3},

{6,1,3,9}, {6,1, 9,3}, {6,3,1,9}, {6,3,9,1}, {6,9,1,3}, {6,9,3,1},

{3,1,6,9}, {3,1,9,6}, {3,9,1,6}, {3,9,6,1}, {3,6,1,9}, {3,6,9,1},

{9,1,3,6}, {9,1,6,3}, {9,3,1,6}, {9,3,6,1}, {9,6,1,3}, {9,6,3,1}.

Since none of these combinations satisfy the condition, the output is No
# A Python program to print all
# permutations using library function"""
from itertools import permutations
t=int(input())
n=int(input())
IntList=[]
inputs = list(map(str, input().split()))
for i in range(n):
    y=int(inputs[i])
    IntList.append(y)

perm = permutations(IntList)
count=0
mega_list=[]
# Print the obtained permutations
for i in list(perm):
    #print(i)
    listi=list(i)
    #print(listi)
    mega_list.append(listi)
count=0
for listi in mega_list:
    for i in range(len(listi)):
        if i!=(len(listi)-1):
            if (listi[i] + listi[i + 1]) % 3 != 0:
                count=count+1
    if count==3:
        break
    else:
        count=0
if count:
    print("yes")
else:
    print("no")



