import copy

dimension = int(input('Sheiyvanet Matricis Rigi: '))
matrix = []
for i in range(dimension):
    row = [int(i) for i in input(f'Sheiyvanet {i + 1} Striqoni (Gtxovt ar gamoiyenot "," ricxvebi ertmanets daashoret msh: 1 2 3 4...): ').split()]
    if len(row) == dimension:
        matrix.append(row)
    else:
        raise Exception("--------------Matricis Striqoni Arasworia!!!----------------")

confirmationText = f'Sheyvanili Matricaa: '
for index, i in enumerate(matrix):
    confirmationText += f'\n{str(i)}'
    if index == len(matrix) - 1:
        confirmationText += '\nDaweret Y tu sworia da N tu arasworia. '
        
confirmation = input(confirmationText)

def minor(arr, m, n):
    tmpArr = copy.deepcopy(arr)
    tmpArr.pop(m-1)
    for item in tmpArr:
        item.pop(n-1)
    if len(tmpArr) > 2:
        return determinant(tmpArr)
    else:
        if len(tmpArr) == 1:
            return tmpArr[0][0]
        minorDet = (tmpArr[0][0] * tmpArr[1][1]) - (tmpArr[0][1] * tmpArr[1][0])
        return minorDet
    
def algAddition(arr, m, n):
    arr = copy.deepcopy(arr)
    sum = (-1)**(m+n) * minor(arr, m, n)
    return sum

def determinant(arr):
    arr = copy.deepcopy(arr)
    det = 0
    for index, item in enumerate(arr[0]):
        det += item * algAddition(arr, 1, index + 1)
    return det


if __name__ == '__main__':
    try:
        if confirmation.upper() == 'Y':
            print(f'Sheyvanili matricis determinantia: {determinant(matrix)}')
        elif confirmation.upper() == 'N': 
            print('Ok. Tavidan dzma...')
        else:
            print('TF?????? Eg ra jandabaaa....')
    except BaseException:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        print('')
        print("Glije Enters Da Vso...")
        input()



