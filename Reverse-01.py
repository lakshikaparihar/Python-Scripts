'''
Test 1
Input : 4
Expected output : 15

Test 2
Input : 1
Expected output : 1

Test 3
Input : 20
Expected output : 1048575

Test 4
Input : 39
Expected output : 549755813887

Test 5
Input :2
Expected output : 3

Test 6
Input :9
Expected output :511


'''

n = int(input())

print(int(pow(2,n)-1))
