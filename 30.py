
c = [(x, y, z)
	for x in range(1, 20)
	for y in [1,5,7,20]
	for z in range(10, 20)
	if x+y+z==30 and x!=y!=z]
print(c)

# c = [(x, y, z)
# 	for x in [12, 15, 4, 2, 3, 5, 13,27,21,16,11]
# 	for y in [12, 15, 4, 2, 3, 5, 13,27,21,16,11]
# 	for z in [12, 15, 4, 2, 3, 5, 13,27,21,16,11]
# 	if x+y+z==30 and x!=y!=z]
# print(c)


