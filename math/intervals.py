import math

# N = 181
# arr = [135, 133, 124, 132, 104, 152, 134, 130, 129, 120, 122, 124,
#        117, 123, 123, 129, 121, 122, 125, 131, 147, 124, 137, 112,
#        126, 128, 111, 129, 115, 147, 131, 132, 137, 119, 125, 120,
#        129, 125, 123, 127, 132, 118, 133, 132, 132, 134, 131, 120,
#        135, 132, 125, 132, 108, 114, 121, 133, 133, 135, 131, 125,
#        114, 115, 122, 131, 125, 132, 120, 126, 115, 117, 118, 188,
#        132, 134, 127, 127, 124, 135, 128, 127, 115, 144, 129, 120,
#        137, 127, 125, 116, 132, 120, 117, 127, 118, 109, 127, 122,
#        120, 135, 116, 118, 133, 136, 125, 126, 119, 126, 129, 127,
#        129, 124, 127, 132, 126, 131, 127, 130, 126, 124, 135, 127,
#        124, 123, 123, 130, 132, 143, 122, 139, 120, 134, 108, 132,
#        121, 111, 123, 140, 137, 120, 125, 131, 118, 120, 120, 136,
#        129, 127, 116, 138, 128, 133, 122, 131, 128, 140, 138, 134,
#        120, 126, 109, 137, 111, 115, 117, 130, 113, 126, 115, 124,
#        125, 118, 115, 128, 123, 129, 128, 120, 115, 134, 118, 135,
#        134]
# start = 102
# step = 4

# N = 167
# arr = [71, 62, 43, 80, 70, 44, 42, 25, 48, 55, 58, 44, 74, 55, 56,
#        49, 54, 63, 60, 57, 70, 52, 74, 65, 61, 60, 72, 69, 68, 47,
#        30, 62, 81, 56, 55, 38, 68, 55, 74, 50, 29, 35, 55, 52, 27,
#        58, 50, 62, 80, 49, 68, 68, 81, 66, 64, 41, 45, 48, 68, 79,
#        56, 82, 76, 84, 47, 44, 72, 58, 58, 80, 61, 55, 66, 36, 69,
#        44, 88, 88, 73, 39, 70, 70, 35, 51, 69, 50, 59, 35, 43, 71,
#        54, 65, 85, 63, 59, 52, 88, 64, 60, 61, 31, 64, 48, 49, 50,
#        41, 62, 42, 76, 81, 76, 70, 76, 75, 53, 66, 87, 74, 61, 68,
#        73, 44, 61, 53, 46, 69, 71, 58, 63, 73, 56, 65, 53, 77, 39,
#        83, 45, 55, 77, 61, 42, 72, 49, 52, 67, 62, 68, 72, 46, 76,
#        67, 53, 70, 76, 56, 62, 38, 59, 53, 50, 76, 52, 73, 34, 51, 
#        60, 61]
# start = 23
# step = 5

N = 204
arr = [52, 40, 47, 54, 40, 54, 41, 74, 45, 45, 51, 76, 58, 37, 40,
        42, 53, 54, 65, 46, 65, 61, 55, 38, 66, 42, 56, 54, 40, 60,
        43, 49, 77, 64, 53, 64, 58, 54, 56, 53, 43, 35, 56, 34, 59,
        58, 66, 49, 49, 57, 48, 42, 46, 52, 59, 50, 62, 50, 55, 55,
        46, 53, 51, 50, 60, 30, 48, 56, 29, 74, 52, 60, 44, 62, 23,
        54, 40, 33, 20, 55, 42, 61, 54, 41, 45, 75, 59, 41, 51, 45,
        54, 52, 62, 69, 65, 49, 48, 63, 52, 46, 44, 55, 60, 54, 39,
        82, 67, 68, 34, 56, 51, 56, 48, 53, 48, 59, 51, 59, 66, 48,
        61, 42, 54, 33, 39, 47, 46, 47, 73, 63, 34, 44, 51, 46, 40,
        43, 30, 60, 61, 53, 47, 42, 56, 70, 48, 45, 65, 48, 48, 51,
        40, 57, 56, 33, 44, 43, 45, 35, 35, 56, 59, 66, 56, 52, 44,
        53, 49, 55, 25, 53, 48, 73, 28, 58, 72, 57, 46, 54, 55, 59,
        38, 53, 48, 68, 36, 53, 41, 55, 51, 50, 45, 50, 29, 60, 39,
        50, 59, 33, 56, 49, 31, 70, 56, 56]
start = 17 
step = 7

# ????????????
if min(arr) == 0:
    print("????????????:", max(arr)-min(arr)+1)
else:
    print("????????????:", max(arr)-min(arr))

# ????????????????
arr.sort()
# ???????????????????? ??????-???? ????????????????????:
# ?????????????????????? ??????????????, ???????????????? ?? ?????????????????? ??????????????????, ???????? ??????????????????
if min(arr) == 0:
    IntervalsNumber = math.ceil((1+max(arr)-start)/step) 
else:
    IntervalsNumber = math.ceil((max(arr)-start)/step)
    
print("\t x\t|\t n\t|\t n_i/N")
vers = []
amounts = []
inters = []
for i in range(IntervalsNumber):
    inter = start + i*step
    amount = 0
    s = inter
    inters.append(inter)
    while s < inter+step:
        try:
            arr.remove(s)
            amount += 1
            s -= 1
        except ValueError:
            s += 1
            continue
    ver = amount/N
    vers.append(ver)
    sumVer = sum(vers)
    amounts.append(amount)
    sumAmount = sum(amounts)
    print("\t{:}\t|\t{:}\t|\t {:} \t|\t {:}".format(inter, amount, round(ver, 5), round(sum(vers), 5)))


print("\tsum:\t|\t{:}\t|\t {:}\t".format(sumAmount, round(sumVer, 5)))


# ????. ????????. X
C = 60 # ???????????????? ???????????????????? ?????????? ??????????
difSA = []
j = 0
for i in amounts:
    difSA.append(((inters[j]+math.ceil(step/2) - C)/step * i))
    j+=1
X = sum(difSA)/N * step + C
print(difSA)
print("?????????????? ????????????????????????????:", X)