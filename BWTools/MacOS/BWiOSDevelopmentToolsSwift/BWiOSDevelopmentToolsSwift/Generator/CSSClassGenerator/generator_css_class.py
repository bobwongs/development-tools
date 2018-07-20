
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

def getNames(string):
    name = ''
    startTag = "class='"
    endTag = "'"
    if string.find(startTag) < 0:
        startTag = 'class="'
        endTag = '"'
        if string.find(startTag) < 0:
            return ''
    startIndex = string.find(startTag)+len(startTag)
    subString = string[startIndex : len(string)]
    endIndex = startIndex + subString.find(endTag)
    name = string[startIndex : endIndex]
    return name

def generateUnitCode(name):
    code = '.%s {\n  \n}\n' % (name)
    return code

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
        if name != '':
            array_names.append(name)
    
    template_code = ''
    for name in array_names:
        template_code = '%s\n%s' % (template_code, generateUnitCode(name))

    # 写入文件
    contentToWrite = template_code
    file_write = open(path_generation_file, 'wb', 1)
    file_write.write(contentToWrite)
    file_write.close()

    # 打开生成目录，不用打开文件，直接生成在面板上
#    os.system('open -a Xcode %s' % path_generation_file)

    print 'Generate Template Code Successfully!'

# ---------- Main ----------

def main():
    # 文件判断和创建
    hasDirectory(path_base)
    hasFile(path_source_file)
    hasFile(path_generation_file)
    
    # 生成
    generateTemplateCode()
    
    return


if __name__=='__main__':
    main()

