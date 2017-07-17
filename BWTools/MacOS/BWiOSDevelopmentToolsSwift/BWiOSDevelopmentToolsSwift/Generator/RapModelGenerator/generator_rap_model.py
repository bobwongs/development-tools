
# coding: utf-8
# author: BobWong
# Use for: Generate Rap Model efficiently

' Rap Model Generator '

__author__ = 'BobWong'

import sys
import re
import time
import os
import shutil
import getpass
import getopt

# ---------- Help ----------

def help():
    help = (
            'This is help!\n' +
            'Parameters Usage:\n'
            '   -c: Copy Right Name\n' +
            '   -p: Project Name\n' +
            '   -P: Prefix Name\n' +
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

# 判断文本中是否存在跟字典Key值相同的文本
def hasDictKeyInText(text, dict):
    for key in dict.keys():
        if key in text:
            return True
    return False

# ---------- Parameters Setting ----------

# Basic
copyright_name = 'BobWongStudio'
project_name = 'BWiOSProject'
prefix_name = 'BW'
suffix_vc = 'ViewController'
user_name = getpass.getuser()
author_name = user_name
import_file = '#import <Foundation/Foundation.h>'
base_vc = 'NSObject'
module_name = 'RapModel'

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
path_base = '/Users/'+ user_name +'/Desktop/Generator/RapModel'

path_source_dir = path_base + '/Source'
path_source_file = path_source_dir + '/source.txt'

path_generation = path_base + '/Generation'
path_generation_history = '%s/History' % path_generation
path_generation_temp = '%s/Temporary' % path_generation
path_generation_type = '%s/%s' % (path_generation_temp, module_name)
path_generation_file = '%s/generation.txt' % path_generation

name_prefix = ''
name_controller = '%sController' % name_prefix
name_model = '%sModel' % name_prefix
name_view = '%sView' % name_prefix

year_string = time.strftime('%Y')  # 获得当前年份
date_string = time.strftime("%y/%m/%d")  # 获得当前日期，转换为字符串
time_string = time.strftime("%Y%m%d%H%M%S")

'''
    数据源示例：
    anticipatedIncome	预计收益	number	@mock=0
    hasAccount	是否绑定账户	boolean	@mock=false
    '''
        
rap_type_dict = {'number': '@property (assign, nonatomic) NSInteger ',
                'boolean': '@property (assign, nonatomic) BOOL ',
                'string': '@property (strong, nonatomic) NSString *',
                'object': '@property (strong, nonatomic) ModelClass *',
                'array': '@property (strong, nonatomic) NSArray *'}

# ---------- Function Definition ----------

def getTuple(line):
    
    line = line.strip()
    array = re.split(r'\s*', line)  # 通过空格进行分割，获得需要的Model数据
    print array
    name = array[0]
    description = array[1]
    type = rap_type_dict[array[2]]
    line_string = '%s%s;  ///< %s' % (type, name, description)

    return line_string

# 创建VC
def generateFile(source_array, model_name):
    model_full_name = '%s%sModel' % (prefix_name, model_name)
    path_generation_model_dir = '%s/%s' % (path_generation_type, model_full_name)
    os.mkdir(path_generation_model_dir)
    
    generation_code = '\n'
    for item in source_array:
        line_string = getTuple(item)
        generation_code = '%s%s\n' % (generation_code, line_string)
    
    file_name = model_full_name

    # vc头文件.h
    file_vc_header = open('%s/%s.h' % (path_generation_model_dir, file_name), 'wb', 1)
    content_header = (
                      '//\n' +
                      '//  %s.h\n' % (file_name) +
                      '//  %s\n' % (project_name) +
                      '//\n' +
                      '//  Created by %s on %s.\n' % (author_name, date_string) +
                      '//  Copyright © %s年 %s. All rights reserved.\n' % (year_string, copyright_name) +
                      '//\n' +
                      '\n' +
                      '%s\n' % (import_file) +
                      '\n' +
                      '@interface %s : %s\n' % (file_name, base_vc) +
                      '%s\n' % (generation_code) +
                      '@end\n'
                      )
    file_vc_header.write(content_header)
    file_vc_header.close()

    # vc实现文件.m
    file_vc_implement = open('%s/%s.m' % (path_generation_model_dir, file_name), 'wb', 1)
    content_implement = (
                         '//\n' +
                         '//  %s.m\n' % (file_name) +
                         '//  %s\n' % (project_name) +
                         '//\n' +
                         '//  Created by %s on %s.\n' % (author_name, date_string) +
                         '//  Copyright © %s年 %s. All rights reserved.\n' % (year_string, copyright_name) +
                         '//\n' +
                         '\n' +
                         '#import "%s.h"\n' % file_name +
                         '\n' +
                         '@implementation %s\n' % file_name +
                         '\n' +
                         '@end\n'
                         )

    file_vc_implement.write(content_implement)
    file_vc_implement.close()

# ---------- Main ----------

def main():
    # 文件判断和创建
    hasDirectory(path_source_dir)
    hasFile(path_source_file)
    
    hasDirectory(path_generation_history)
    hasFile(path_generation_file)
    
    # 读多个文件去生成对应多个目标
    
    # 读取文件
    file = open(path_source_file, 'r')  # 这里使用相对路径
    array_line = file.readlines()
    file.close()
    
    # 有旧目录
    if os.path.exists(path_generation_temp):
        print 'Directory ' + path_generation_temp + ' exits!'
        print 'Move Old ' + path_generation_temp + ' to History!\n'
        path_last = path_generation_history + '/%s' % (time_string)
        hasDirectory(path_last)
        shutil.move(path_generation_temp,path_last)  # 移动

    # 创建目录
    hasDirectory(path_generation_temp)
    os.mkdir(path_generation_type)


    dict_all_models = {}
    array_model_source = []
    dict_key = ''
    for text in array_line:
        text = text.strip()
        if isBlank(text) != True:
            if "@mock" in text or hasDictKeyInText(text, rap_type_dict):
                array_model_source.append(text)
            else:
                if len(array_model_source) == 0:
                    dict_key = text
                    continue
                else:
                    dict_all_models[dict_key] = array_model_source
                    array_model_source = []
                    dict_key = text  # 两处都需要对Key值进行赋值

    dict_all_models[dict_key] = array_model_source

    for (key, value) in dict_all_models.items():
        generateFile(value, key)  # key即为Model名，创建文件

    text_success = 'Rap Model Generation Finished'
    file_generation = open(path_generation_file, 'wb', 1)
    file_generation.write(text_success)
    file_generation.close()
    print text_success

    os.system('open %s' % path_generation_type)  # 打开生成目录

if __name__=='__main__':
    main()
