try:
    fread=open("001.jpg","rb")
    fwrite=open("copypython.jpg","wb")
    bytedata=fread.read()
    fwrite.write(bytedata)
    fread.close()
    fwrite.close()
except IoError:
    print("source file does not exists")
