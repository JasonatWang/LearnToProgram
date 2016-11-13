# 文件框架_1:适用于大文件
my_file = open("../test.txt", 'rb')
for fileline in my_file:
    # 处理的内容
    fileline = fileline.decode('utf-8').strip()
    print(fileline)
my_file.close()
# 文件框架_2:适用于小文件
my_file = open("../test.dat", 'rb')
for fileline in my_file.readlines():
    # 处理的内容
    fileline = fileline.decode('utf-8').strip()
    print(fileline)
my_file.close()