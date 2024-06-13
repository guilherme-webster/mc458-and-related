class Box:

    def __init__(self, h, w, l):
        self.h = h
        self.w = w
        self.l = l

    def __lt__(self, other):
        return self.w * self.l < other.w * other.l
    
def rotateRight(box):
    rotated = Box(0, 0, 0)

    rotated.h = box.w
    rotated.l = max(box.h, box.l)
    rotated.w = min(box.h, box.l)

    return rotated

def rotateLeft(box):
    rotated = Box(0, 0, 0)

    rotated.h = box.l
    rotated.l = max(box.h, box.w)
    rotated.w = min(box.h, box.w)

    return rotated

def createBoxList(arr, n):

    newArray = []

    for i in range(n):
        newArray.append(arr[i])
        newArray.append(rotateLeft(arr[i]))
        newArray.append(rotateRight(arr[i]))

    return newArray

def maxHeight(arr, n):

    newArray = createBoxList(arr, n)

    newArray.sort(reverse = True)

    newLenght = len(newArray)

    lds = [0] * (newLenght)

    for i in range(newLenght):
        lds[i] = newArray[i].h

    for i in range(1, newLenght):
        for j in range(i):
            if(newArray[i].w < newArray[j].w and 
               newArray[i].l < newArray[j].l and
               lds[i] < lds[j] + newArray[i].h):
                lds[i] =  lds[j] + newArray[i].h

    max = -1
    for i in range(newLenght):
        if lds[i] > max:
            max = lds[i]
    
    return max


# Driver Code
if __name__ == "__main__":
    arr = [Box(4, 6, 7), Box(1, 2, 3),
           Box(4, 5, 6), Box(10, 12, 32)]
    n = len(arr)
    print("The maximum possible height of stack is",
           maxHeight(arr, n))