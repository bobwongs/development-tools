
# coding:utf-8

# Python进行中文注释，在Python脚本文件的第一行或第二行添加如上一句，一定是这两行之一

import sys

#str1 = '@property (nonatomic, strong) UILabel *label;  ///< My Label'
str1 = sys.argv[1]

type = str1[str1.find(") ") +2:str1.find(" *")]  # rfind重复查找，直到查到最后一个，find为找到的第一个，数字2为找到位置加2开始，:为拼接后面找到的位置
object = str1[str1.find("*") +1:str1.find(";")]

print type
print object

output = ('- (' + type + ' *)' + object + ' ' + '{\n' +
          '   if (!_' + object + ') {\n\n' +
          '   }\n' +
          '   return _' + object + ';\n}')

print output
