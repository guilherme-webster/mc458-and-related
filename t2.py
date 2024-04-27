def merge_count_inv(arr, temp, left, mid, right):
    inv_count = 0

    # copiamos os elementos para dois subarrays temporários que estão armazenados em temp
    for p in range(left, mid + 1):
        temp[p] = arr[p]
    for q in range(mid + 1, right + 1):
        temp[right + mid + 1 - q] = arr[q] # aqui a cópia é feita na ordem inversa

    i = left
    j = right

    for k in range(left, right + 1):
        if(temp[i] <= temp[j]):
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j -= 1
            inv_count += (mid - i + 1) # aqui, cada elemento do subarray esquerdo ordenado (a partir do i) será maior que o j-ésimo elemento do array direito, e esta conta nos dá o número de flips

    return inv_count

def merge_sort_and_count(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        inv_count += merge_count_inv(arr, temp, left, mid, right)

    return inv_count

n = int(input())
array = list(map(int, input().strip().split()))

temp = [0] * n 

result = merge_sort_and_count(array, temp, 0, n - 1)
print(result)