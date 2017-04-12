
# coding: utf-8
# author: BobWong
# use for: Generate APIManager file

' APIManager Generator '

__author__ = 'BobWong'

import os
import shutil
import sys
import time
import getpass
import getopt
import re

# ---------- Help ----------

def help():
    help = (
            'This is help!\n' +
            'Parameters Usage:\n'
            '   -c: Copy Right Name\n' +
            '   -p: Project Name\n' +
            '   -P: Prefix Name\n' +
            '   -s: Suffix Name\n' +
            '   -a: Author Name\n' +
            '   -i: Import File\n' +
            '   -b: Basic ViewController\n' +
            '   -m: Module Name\n' +
            '   -h: Help'
            )
    print help

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

# Basic
copyright_name = '月亮小屋（中国）有限公司'
project_name = 'Bluemoon'
prefix_name = 'BM'
suffix_name = 'APIManager'
user_name = getpass.getuser()
author_name = user_name
import_file = '#import "BMBaseAPIManager.h"'
base_class = 'BMBaseAPIManager'
module_name = 'APIManager'

options, arguments = getopt.getopt(sys.argv[1:], "hc:p:P:a:i:b:m:h:")
for option, value in options:
    if isBlank(value):
        continue
    if option == "-c":
        copyright_name = value
    elif option == "-p":
        project_name = value
    elif option == "-P":
        prefix_name = value
    elif option == "-s":
        suffix_name = value
    elif option == "-a":
        author_name = value
    elif option == "-i":
        import_file = value
    elif option == "-b":
        base_vc = value
    elif option == "-m":
        module_name = value
    elif option == "-h":
        help()
        sys.exit()

# Path
path_base = '/Users/'+ user_name +'/Desktop/Generator/APIManager'

path_source_dir = path_base + '/Source'
path_source_file = path_source_dir + '/source.txt'

path_generation = path_base + '/Generation'
path_generation_history = '%s/History' % path_generation
path_generation_temp = '%s/Temporary' % path_generation
path_module = '%s/%s' % (path_generation_temp, module_name)
path_generation_file = '%s/generation.txt' % path_generation

year_string = time.strftime('%Y')  # 获得当前年份
date_string = time.strftime("%y/%m/%d")  # 获得当前日期，转换为字符串
time_string = time.strftime("%Y%m%d%H%M%S")


#path_generation = 'Generation'
path_generation_api_manager = path_generation + '/APIManager'

year_string = time.strftime('%Y')  # 获得当前年份
date_string = time.strftime("%Y/%m/%d")  # 获得当前日期，转换为字符串

# 创建的APIManager文件目录名称，前者为从输入参数中获取，后者为定值
dir_name = 'APIManager'

# ---------- Function ----------
def getTuple(line):
    find_words_url = 'URL: '
    find_words_name = 'Name: '
    find_words_api_manager = 'APIManager: '
    find_words_interface = 'Interface: '
    regex = r'%s|%s|%s|%s|\n' % (find_words_url, find_words_name, find_words_api_manager, find_words_interface)  # 这种方式可以解决，最后一行没有“\n”换行符的时候，少截取一个字符的问题
    array = re.split(regex, line)
    for item in array:
        if item.strip() =='':
            array.remove(item)

    url = stripSpace(array[0])
    name = stripSpace(array[1])
    api_manager = stripSpace(array[2])
    interface = stripSpace(array[3])
    return (url, name, api_manager, interface)


# 创建APIManager，并且返回接口宏定义的代码
def createAPIManager(source):
    (url, name, api_manager, interface) = getTuple(source)
    
    dir_path = path_module
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    api_manager_name = prefix_name + api_manager + 'APIManager' #目录名即为APIManager的类名
    
    path_api_manager = '%s/%s' % (dir_path, api_manager_name)
    if os.path.exists(path_api_manager):
        print 'Directory ' + api_manager_name + ' exits'
        print 'Remove Old ' + api_manager_name + '\n'
        shutil.rmtree(path_api_manager)  #移除旧目录
    
    os.mkdir(path_api_manager)  #创建目录
    
    # 头文件.h
    file_header_write = open('%s/%s/%s.h' % (dir_path, api_manager_name, api_manager_name), 'wb', 1)
    content_header = (
                      '//\n' +
                      '//  ' + api_manager_name + '.h\n' +
                      '//  ' + project_name + '\n' +
                      '//\n' +
                      '//  Created by BobWong on '+ date_string + '.\n' +
                      '//  Copyright © %s年 %s. All rights reserved.\n' % (year_string, copyright_name) +
                      '//\n' +
                      '\n' +
                      '#import "' + base_class + '.h"\n' +
                      '\n' +
                      '@interface ' + api_manager_name +' : ' + base_class + '\n' +
                      '\n' +
                      '@end\n'
                      )
    file_header_write.write(content_header)
    file_header_write.close()

    # 实现文件.m
    file_implement_write = open('%s/%s/%s.m' % (dir_path, api_manager_name, api_manager_name), 'wb', 1)
    content_implement = (
                       '//\n' +
                       '//  ' + api_manager_name + '.m\n' +
                       '//  ' + project_name + '\n' +
                       '//\n' +
                       '//  Created by BobWong on '+ date_string + '.\n' +
                       '//  Copyright © %s年 %s. All rights reserved.\n' % (year_string, copyright_name) +
                       '\n' +
                       '#import "%s.h"\n' % api_manager_name +
                       '\n' +
                       '@implementation %s\n' % api_manager_name +
                       '\n' +
                       '- (NSString *)interfaceUrl\n' +
                       '{\n' +
                       '    return INTERFACE_%s;\n' % interface +
                       '}\n' +
                       '\n' +
                       '- (BOOL)useToken\n' +
                       '{\n' +
                       '    return YES;\n' +
                       '}\n' +
                       '\n' +
                       '@end\n'
                       )
    file_implement_write.write(content_implement)
    file_implement_write.close()

    # 接口宏定义
    macro_interface_definition = '#define INTERFACE_%s @"%s"  // %s' % (interface, url, name)
    return macro_interface_definition
# ---------- Function ----------


# ------------ Main -------------
def main():
    # 文件判断和创建
    hasDirectory(path_source_dir)
    hasFile(path_source_file)
    
    hasDirectory(path_generation_history)
    hasFile(path_generation_file)
    
    # 有旧目录
    if os.path.exists(path_generation_temp):
        print 'Directory ' + path_generation_temp + ' exits!'
        print 'Move Old ' + path_generation_temp + ' to History!\n'
        path_last = path_generation_history + '/%s' % (time_string)
        hasDirectory(path_last)
        shutil.move(path_generation_temp,path_last)  # 移动
    
    # 创建目录
    hasDirectory(path_generation_temp)
    os.mkdir(path_module)
    
    # 读取文件
    file = open(path_source_file, 'r')  # 这里使用相对路径
    array_line = file.readlines()
    file.close()

    macro_definition = ''
    for line in array_line:
        macro = createAPIManager(line)
        macro_definition = '%s%s\n' % (macro_definition, macro)

    path_generation_txt_file = path_generation + '/generation_interface_definition.txt'
    file_macro = open(path_generation_txt_file, 'wb', 1)
    file_macro.write(macro_definition)
    file_macro.close()

    print '完成APIManager的生成操作'

    os.system('open %s' % path_generation_temp)  # 打开生成目录
    os.system('open -a Xcode %s' % path_generation_txt_file)  # 用Xcode打开生成的txt文件

# ------------ Execute Main -------------
if __name__=='__main__':
    main()
