
# coding:utf-8

# Function Definition

def getTypeAndObject(str):
    type = str[str.find(") ") +2:str.find(" *")]
    object = str[str.find("*") +1:str.find(";")]
    return (type, object)

# 把一行property的定义生成对应的一个getter方法
def createGetter(str):
    (type, object) = getTypeAndObject(str)
    output = (
              '- (' + type + ' *)' + object + ' ' + '{\n' +
              '   if (!_' + object + ') {\n' +
              '      _' + object + ' = [' + type + ' <#Method#>];\n' +
              '   }\n' +
              '   return _' + object + ';\n}'
              )
    return output

# 把一行ui property生成添加到父视图的方法
def createAddToSuperView(str):
    (type, object) = getTypeAndObject(str)
    output = (
#              '[<#view#> addSubview:' + '<#view#>.' + object + '];'
              '[<#view#> addSubview:' + '_' + object + '];'
              )
    return output

# 把一行ui property生成Masonry方法
def createMasonry(str):
    (type, object) = getTypeAndObject(str)
    output = (
              '[_' + object + ' mas_makeConstraints:^(MASConstraintMaker *make) {\n' +
              '    make.left.mas_equalTo(<#CGFloat#>);\n' +
              '    make.right.mas_equalTo(<#CGFloat#>);\n' +
              '    make.top.mas_equalTo(<#CGFloat#>);\n' +
              '    make.bottom.mas_equalTo(<#CGFloat#>);\n' +
              '}];\n'
              )
    return output

# 生成setUI中的对UI控件初始化的方法
def createInitInSetUI(str):
    (type, object) = getTypeAndObject(str)
    output = (
              '_' + object + ' = [' + type + ' <#Method#>];'
              )
    return output


# ------Main--------

# 读取文件
file = open('resource.m', 'r')  # 这里使用相对路径
array_line = file.readlines()  # 只能调用一次read类型的方法，可能是读取完之后这里read的指针到了最末尾，再读也只能为空方法了
file.close()

# 生成Array
array_getter = []  # Getter Code Array
array_addToView = []
array_masonry = []
array_initInSetUI = []
for line in array_line:
    if line.strip() =='': continue  # 非空判断
    getter = createGetter(line)
    addToView = createAddToSuperView(line)
    masonry = createMasonry(line)
    initInSetUI = createInitInSetUI(line)
    
    array_getter.append(getter)
    array_addToView.append(addToView)
    array_masonry.append(masonry)
    array_initInSetUI.append(initInSetUI)

# 生成Getter
str_getter = ''  # 所有Getter拼在一起的字符串
for getter in array_getter:
#    print getter, '\n'
#    str_getter = str_getter, getter  # 使用此方法不会识别“\n”进行换行
    str_getter = '%s%s\n\n' % (str_getter, getter)  # 使用此方法是可以识别“\n”进行换行
#print str_getter

# 生成添加进父视图的方法
str_setUI = ''

str_initInSetUI = ''
str_addToView = ''

for initInSetUI in array_initInSetUI:
    str_initInSetUI = '%s%s\n' % (str_initInSetUI, initInSetUI)
for addToView in array_addToView:
    str_addToView = '%s%s\n' % (str_addToView, addToView)

str_setUI = '%s\n%s' % (str_initInSetUI, str_addToView)
#print str_addToView

# 生成约束方法
str_masonry = ''
for masonry in array_masonry:
    str_masonry = '%s%s\n' % (str_masonry, masonry)
#print str_masonry

# 写入文件
contentToWrite = 'Getter:\n%s\n\n  setUI:\n%s\n\n  Masonry:\n%s\n\n' % (str_getter, str_setUI, str_masonry)
file_write = open('temp.m', 'wb', 1)
file_write.write(contentToWrite)
file_write.close()

print contentToWrite

# ------Main--------
