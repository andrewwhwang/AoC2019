def increasing(num):
    numstr = str(num)
    for i in range(1,len(numstr)):
        if numstr[i] < numstr[i-1]:
            return False
    return True

def containsRepeat(num):
    record = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

    # record number of adj pairs
    numstr = str(num)
    for i in range(1,len(numstr)):
        if numstr[i] == numstr[i-1]:
            record[numstr[i]] += 1

    # if true if at least one adj pair exists
    recordList = [i == 1 for i in record.values()]
    return any(recordList)

start, end = 123257, 647015
valids = [num for num in range(start,end+1) if increasing(num) and containsRepeat(num)]

print(len(valids))