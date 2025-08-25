file = open("textFile1.txt", "r", encoding="utf-8")
content = file.read()
file.close()

print(content) 