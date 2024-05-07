#1-D and 2-D even parity checking
"""def get_parity(value):
    count = 0
    for i in range(len(value)):
       if value[i]== '1':
           count = count + 1
       else:
           continue
    if count % 2 == 0:
       return 0
    else:
       return 1
 
#1-D parity
in_par = input('Enter the parity: ')
parity = get_parity(in_par)

new_par= input('Enter a new parity to check: ')
new_parity = get_parity(new_par)
if (new_parity == parity):
    print("\nThis is a valid segment")
else:
    print("\nThis is an invalid segment")"""
    
def get_parity(segment):
    # Function to calculate even parity for a given segment
    count_ones = segment.count('1')
    parity_bit = '1' if count_ones % 2 != 0 else '0'
    return parity_bit

def get_2Dparity(mat):
    # Function to calculate 2-D parity
    empty_string = ''
    for j in range(len(mat[0])):
        temp = ''
        for i in range(len(mat)):
            temp = temp + mat[i][j]
        empty_string = empty_string + str(get_parity(temp))
    mat.append(empty_string)

mat = []
size = int(input('Enter the number of data-segments: '))
for j in range(size):
    par = input("Enter the segment seq_number, all must be of the same length: ")
    mat.append(par + str(get_parity(par)))
    
get_2Dparity(mat)
print('')

mat1 = []
for j in range(size):
    par = input('Enter the new segment seq_number, all must be of the same length: ')
    mat1.append(par + str(get_parity(par)))
    
get_2Dparity(mat1)

for k in range(len(mat)):
    if mat[k][-1] == mat1[k][-1]:
        continue
    elif mat[-1] == mat1[-1]:
        continue
    else:
        print('\nError during transmission occurred')
        break
