
# coding: utf-8
# author: BobWong
# Use for: Generate CSS template from html

' UI Property Generation '

__author__ = 'BobWong'

import os
import getpass

# ---------- Tool ----------

# 非空判断
def isBlank(string):
    if string.strip() =='':
        return True
    return False

# 去除空格
def stripSpace(string):
    return string.replace(' ', '')

# 文件目录判断和创建
def hasDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# 文件判断和创建
def hasFile(path):
    if not os.path.exists(path):
        file = open(path, 'wb', 1)
        file.close()

# ---------- Parameters Setting ----------

user_name = getpass.getuser()

path_base = '/Users/'+ user_name +'/Desktop/Generator/CSSClassTemplate'
path_source_file = path_base + '/source.txt'
path_generation_file = path_base + '/generation.txt'

# ---------- Function Definition ----------

# 获得类型和对象，截取字符串
def getTypeAndObject(str):
    type = str[str.find(") ") +2:str.find(" *")]
    object = str[str.find("*") +1:str.find(";")]
    return (type, object)

def getNames(string):
    name = ''
    startTag = "class='"
    endTag = "'"
    if string.find(startTag) < 0:
        startTag = 'class="'
        endTag = '"'
    name = string[str.find(startTag) + len(startTag : string.find(endTag))]
    return name

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
              '[<#view#> addSubview:' + 'self.' + object + '];'
              )
    return output

# 把一行ui property生成Masonry方法
def createMasonry(str):
    (type, object) = getTypeAndObject(str)
    output = (
              '[self.' + object + ' mas_makeConstraints:^(MASConstraintMaker *make) {\n' +
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
              'self.' + object + ' = [' + type + ' <#Method#>];'
              )
    return output

# 生成代码
def generateTemplateCode():
    # 读取文件
    file_source = open(path_source_file, 'r')  # 这里使用相对路径
    array_line = file_source.readlines()  # 只能调用一次read类型的方法，可能是读取完之后这里read的指针到了最末尾，再读返回的内容为空
    file_source.close()
    
    # 生成Array
    array_names = []
    for line in array_line:
        if line.strip() =='': continue  # 非空判断
        name = getNames(line)
        array_names.append(name)
    
    template_code = ''
    for name in array_names:
        template_code = '%s\n%s' % (template_code, )
    
    # 生成Getter
    str_getter = ''  # 所有Getter拼在一起的字符串
    for getter in array_getter:
#        str_getter = str_getter, getter  # 使用此方法不会识别“\n”进行换行
        str_getter = '%s%s\n\n' % (str_getter, getter)  # 使用此方法是可以识别“\n”进行换行

    # 写入文件
    contentToWrite = 'Getter:\n%s\n\nsetUI:\n%s\n\nMasonry:\n%s' % (str_getter, str_setUI, str_masonry)
    file_write = open(path_generation_file, 'wb', 1)
    file_write.write(contentToWrite)
    file_write.close()

    # 打开生成目录
    os.system('open -a Xcode %s' % path_generation_file)

    print 'Generate UI property code successfully!'


# ---------- Main ----------

def generateUnitCode(name):
    code = '''.%s {
        
        }
        ''' % (name)

def main():
    # 文件判断和创建
    hasDirectory(path_base)
    hasFile(path_source_file)
    hasFile(path_generation_file)
    
    # 生成
    generateTemplateCode()
    
    return
# ------Main--------


if __name__=='__main__':
    main()

