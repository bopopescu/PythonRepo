

f = open("download.jpg","rb")

f1 = open("CopyImage.jpg","wb")

for data in f:
    f1.write(data)