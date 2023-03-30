import datetime
f = open("2021.srt", "w")
i = 0

for i in range(2021):
    f.write(str(i + 1) + "\n" + str(str(datetime.timedelta(milliseconds=(i) * (100 / 3)))[:11] + " --> " + str(datetime.timedelta(milliseconds=(i + 1) * (100 / 3)))[:11]).replace(".", ",") + "\n" + str(i + 1) + "\n\n")

f.close()
