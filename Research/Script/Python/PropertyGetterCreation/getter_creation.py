
# coding:utf-8

# Function Definition，把一行property的定义生成对应的一个getter方法
def create_getter(str):
    type = str[str.find(") ") +2:str.find(" *")]  # rfind重复查找，直到查到最后一个，find为找到的第一个，数字2为找到位置加2开始，:为拼接后面找到的位置
    object = str[str.find("*") +1:str.find(";")]
    #print type
    #print object
    
    output = (
              '- (' + type + ' *)' + object + ' ' + '{\n' +
              '   if (!_' + object + ') {\n\n' +
              '   }\n' +
              '   return _' + object + ';\n}'
              )
    return output


# ------Main--------

# 读取文件和生成Getter
file = open('resource.txt', 'r')  # 这里使用相对路径
array_line = file.readlines()  # 只能调用一次read类型的方法，可能是读取完之后这里read的指针到了最末尾，再读也只能为空方法了
file.close()

array = []  # Getter Code Array
for line in array_line:
    if line.strip() =='': continue  # 非空判断
    getter = create_getter(line)
    array.append(getter)

str_getter = ''  # 所有Getter拼在一起的字符串
for getter in array:
#    print getter, '\n'
#    str_getter = str_getter, getter  # 使用此方法不会识别“\n”进行换行
    str_getter = '%s%s\n\n' % (str_getter, getter)  # 使用此方法是可以识别“\n”进行换行

print str_getter

# 写入文件
file_write = open('temp.txt', 'wb', 1)
file_write.write(str_getter)
file_write.close()

# ------Main--------
