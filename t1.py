global_max = 0
suffix_max= 0
begin_temp = 0
begin = 0
end = 0
max_length = 0

n = int(input())
niceness = input().split()

for i in range(n - 1):
    niceness[i] = int(niceness[i])
    suffix_max += niceness[i]
    # the or checks if we have a (end - begin) maximized
    if(suffix_max > global_max) or (suffix_max == global_max and (i - begin_temp) > max_length):
        global_max = suffix_max
        begin = begin_temp
        max_length = i - begin
        end = i
    elif suffix_max < 0:
        suffix_max = 0
        begin_temp = i + 1

if(global_max > 0):
    print(begin + 1, end + 1)
else:
    print(0, 0)