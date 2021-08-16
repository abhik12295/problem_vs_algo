def sqrt(num):
    if num == 0 and num == 1:
        return num
    start = 1
    end = num

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == num:
            return mid
        if mid * mid > num:
            end = mid - 1
        else:
            start = mid + 1
    return end


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")