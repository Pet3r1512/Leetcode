numRows = 5

rows, cols = (numRows, numRows)

arr = [ [ 0 for _ in range(numRows) ] for _ in range(numRows) ]

print()
for i in range(numRows):
    arr[i][0] = 1
    for j in range(1, i + 1):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

sliced_arr = [row[:i+1] for i, row in enumerate(arr)]

for row in sliced_arr:
    print(row)