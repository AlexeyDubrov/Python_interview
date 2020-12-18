List_1 = [1, 5, 6, 15, 21, 77]
List_2 = [2, 21, 33, 44]
i = j = 0
result = []
while i < len(List_1) and j < len(List_2):
    if List_1[i] < List_2[j]:
        result.append(List_1[i])
        i += 1
    else:
        result.append(List_2[j])
        j += 1

while i < len(List_1):
    result.append(List_1[i])
    i += 1
while j < len(List_2):
    result.append(List_2[j])

print(*result)