sal_grs_inp = input("Enter your gross salary: ")
sal_grs = float(sal_grs_inp)

thrs1 = 12570
thrs2 = 50270
thrs3 = 150000

if sal_grs > thrs3 :
    sal_net = (.55 * (sal_grs - thrs3)) + (.6 * (thrs3 - thrs2)) + (.8 * (thrs2 - thrs1)) + thrs1
elif sal_grs > thrs2 :
    sal_net = (.6 * (sal_grs - thrs2)) + (.8 * (thrs2 - thrs1)) + thrs1
elif sal_grs > thrs1 :
    sal_net = (.8 * (sal_grs - thrs1)) + thrs1
else:
    sal_net = sal_grs

# if sal_grs >= 150000:
#     sal_net = 4
# elif sal_grs >= 50270:
#     sal_net = 3
# elif sal_grs >= 12570:
#     sal_net = 2
# else:
#     sal_net = 1

print("Your net pay is: ", sal_net)
