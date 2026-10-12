players = ["Messi", "Ronaldo", "Doue", "Neymar", "Mbappe"]
print(players[0])
players.append("Lewandoski")
print(players[-1])
players.insert(2, "Saint-Maximin")
print(players)
print(len(players))
players.remove("Neymar")
print(players)
players.pop(5)
print(players)
#2d-list
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix)
print("Number of rows :", len(matrix))
print("Number of columns: ", len(matrix[0]))
print(matrix[1][1])
print(matrix[2][0])

for i in range(3):
    for j in range(3):
        print(matrix[i][j], end= " ")
    print("\n")

row = int(input("How many rows do you want? "))
column = int(input("How many columns do you want? "))
matrix1 = []
for a in range(row):
    temp = []
    for b in range(column):
        x = int(input("Enter the numbers" ))
        temp.append(x)
    matrix1.append(temp)
print(matrix1)
for c in range(row):
    for d in range(column):
        print(matrix1[c][d], end = " ")
    print("\n")

matrixA = [[1, 2], [3, 4]]
matrixB = [[5, 6], [8, 9]]
result = [[0, 0], [0, 0]]
for i in range(0,2):
    for j in range(0,2):
        result[i][j] = matrixA[i][j] + matrixB[i][j]
print(result)
    