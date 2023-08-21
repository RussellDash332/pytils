def merge(arr, left, mid, right):
    i, j, inv_count, temp = left, mid + 1, 0, []
    while i <= mid and j <= right:
        if arr[i] <= arr[j]: temp.append(arr[i]); i += 1
        else: temp.append(arr[j]); inv_count += (mid - i + 1); j += 1
    temp.extend(arr[i:mid+1])
    temp.extend(arr[j:right+1])
    for idx in range(left, right + 1): arr[idx] = temp[idx - left]
    return inv_count

def inv_idx(arr, left=None, right=None):
    if left == right == None: return inv_idx(arr, 0, len(arr)-1)
    inv_count = 0
    if left < right: mid = (left + right) // 2; inv_count += inv_idx(arr, left, mid) + inv_idx(arr, mid + 1, right) + merge(arr, left, mid, right)
    return inv_count

arr = [0, 1, 2, 3, 4]
print(inv_idx(arr)) # is sorted
arr = [0, 1, 2, 3, 4][::-1]
print(inv_idx(arr)) # is reverse-sorted
arr = [2, 3, 4, 1, 0]
print(inv_idx(arr))