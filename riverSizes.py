def riverSizes(matrix):
    rivers = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 1:
                rivers.append(riverDFS(matrix, y, x))
    return rivers

def riverDFS(matrix, y, x):
	#if out of bounds
	if y < 0 or x < 0 or y >= len(matrix) or x >= len(matrix[0]):
		return 0 
	
	#if not 1
	if matrix[y][x] != 1:
		return 0
	
	sum = 1 #since sum == 1
	matrix[y][x] = 2 #since it has been checked
	
	for neighbor in [(y,x+1),(y,x-1),(y+1,x),(y-1,x)]:
		sum += riverDFS(matrix, neighbor[0], neighbor[1])
		
	return sum