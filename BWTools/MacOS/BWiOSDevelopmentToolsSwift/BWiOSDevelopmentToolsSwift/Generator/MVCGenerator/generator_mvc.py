
# coding: utf-8
# author: BobWong
# Use for: Generate MVC file efficiently

' MVC Generator '

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

# ---------- Parameters Setting ----------

# Basic
copyright_name = 'BobWongStudio'
project_name = 'BWiOSProject'
prefix_name = 'BW'
suffix_vc = 'ViewController'
user_name = getpass.getuser()
author_name = user_name
import_file = '#import <UIKit/UIKit.h>'
base_vc = 'UIViewController'
mvc_module_name = 'MVC'

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
        mvc_module_name = value
    elif option == "-h":
        help()
        sys.exit()


# Path
path_base = '/Users/'+ user_name +'/Desktop/Generator/MVC'

path_source_dir = path_base + '/Source'
path_source_file = path_source_dir + '/source.txt'

path_generation = path_base + '/Generation'
path_generation_history = '%s/History' % path_generation
path_generation_temp = '%s/Temporary' % path_generation
path_mvc = '%s/%s' % (path_generation_temp, mvc_module_name)
path_generation_file = '%s/generation.txt' % path_generation

name_prefix = ''
name_controller = '%sController' % name_prefix
name_model = '%sModel' % name_prefix
name_view = '%sView' % name_prefix

year_string = time.strftime('%Y')  # 获得当前年份
date_string = time.strftime("%y/%m/%d")  # 获得当前日期，转换为字符串
time_string = time.strftime("%Y%m%d%H%M%S")

# ---------- Function Definition ----------

def getTuple(line):
    # ---------Controller----------
    find_words_vc = 'VC:'
    find_words_title = 'Title:'
    find_words_comment = 'Comment:'
    regex = r'%s|%s|%s|\n' % (find_words_vc, find_words_title, find_words_comment)
    array = re.split(regex, line)
    for item in array:
        if item.strip() =='':
            array.remove(item)
    print array
    # VC
    vc = stripSpace(array[0])
    # Title
    title = stripSpace(array[1])
    # Comment
    comment = stripSpace(array[2])

    return (vc, title, comment)
    # ---------Controller----------

# 创建VC
def generateMVC(Source):
    (vc, title, comment) = getTuple(Source)
    vc_name = '%s%s%s' % (prefix_name, vc, suffix_vc)
    
    # 创建vc文件目录
    path_vc = '%s/%s' % (path_mvc, vc_name)
    path_controller = '%s/%s' % (path_vc, name_controller)
    path_model = '%s/%s' % (path_vc, name_model)
    path_view = '%s/%s' % (path_vc, name_view)
    os.mkdir(path_vc)
    os.mkdir(path_controller)
    os.mkdir(path_model)
    os.mkdir(path_view)
    
    # vc头文件.h
    file_vc_header = open('%s/%s.h' % (path_controller, vc_name), 'wb', 1)
    content_header = (
                      '//\n' +
                      '//  %s.h\n' % (vc_name) +
                      '//  %s\n' % (project_name) +
                      '//\n' +
                      '//  Created by %s on %s.\n' % (author_name, date_string) +
                      '//  Copyright © %s年 %s. All rights reserved.\n' % (year_string, copyright_name) +
                      '//\n' +
                      '\n' +
                      '%s\n' % (import_file) +
                      '\n' +
                      '/**\n' +
                      ' * %s\n' % comment +
                      ' */\n' +
                      '@interface %s : %s\n' % (vc_name, base_vc) +
                      '\n' +
                      '@end\n'
                      )
    file_vc_header.write(content_header)
    file_vc_header.close()

    # vc实现文件.m
    file_vc_implement = open('%s/%s.m' % (path_controller, vc_name), 'wb', 1)
    content_implement = (
                         '//\n' +
                         '//  %s.m\n' % (vc_name) +
                         '//  %s\n' % (project_name) +
                         '//\n' +
                         '//  Created by %s on %s.\n' % (author_name, date_string) +
                         '//  Copyright © %s年 %s. All rights reserved.\n' % (year_string, copyright_name) +
                         '//\n' +
                         '\n' +
                         '#import "%s.h"\n' % vc_name +
                         '\n' +
                         '@interface %s () <#<>#>\n' % (vc_name) +
                         '\n' +
                         '<#Code#>\n' +
                         '\n' +
                         '@end\n' +
                         '\n' +
                         '@implementation %s\n' % vc_name +
                         '\n' +
                         '#pragma mark - View Cycle\n' +
                         '\n' +
                         '- (void)viewDidLoad\n' +
                         '{\n' +
                         '    [super viewDidLoad];\n' +
                         '    \n' +
                         '    self.title = @"%s";\n' % title +
                         '    \n' +
                         '    [self setData];\n' +
                         '    [self setUI];\n' +
                         '    [self setConstraints];\n' +
                         '    [self loadData];\n' +
                         '}\n' +
                         '\n' +
                         '#pragma mark - Public Method\n' +
                         '\n' +
                         '#pragma mark - Action\n' +
                         '\n' +
                         '#pragma mark - Network\n' +
                         '\n' +
                         '#pragma mark - Custom Delegate\n' +
                         '\n' +
                         '#pragma mark - System Delegate\n' +
                         '\n' +
                         '#pragma mark - Private Method\n' +
                         '\n' +
                         '- (void)setData\n' +
                         '{\n' +
                         '    <#Code#>\n' +
                         '}\n' +
                         '\n' +
                         '- (void)setUI\n' +
                         '{\n' +
                         '    <#Code#>\n' +
                         '}\n' +
                         '\n' +
                         '- (void)setConstraints\n' +
                         '{\n' +
                         '    <#Code#>\n' +
                         '}\n' +
                         '\n' +
                         '- (void)loadData\n' +
                         '{\n' +
                         '    <#Code#>\n' +
                         '}\n' +
                         '\n' +
                         '#pragma mark - Getter and Setter\n' +
                         '\n' +
                         '@end\n'
                         )

    file_vc_implement.write(content_implement)
    file_vc_implement.close()

    # 占坑文件
    file_model = open('%s/%s' % (path_model, name_model), 'wb', 1)
    file_model.close()

    file_view = open('%s/%s' % (path_view, name_view), 'wb', 1)
    file_view.close()


# ---------- Main ----------

def main():
    # 文件判断和创建
    hasDirectory(path_source_dir)
    hasFile(path_source_file)
    
    hasDirectory(path_generation_history)
    hasFile(path_generation_file)
    
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
    os.mkdir(path_mvc)
    
    for line in array_line:
        generateMVC(line)

    text_success = 'MVC Generation Finished'
    file_generation = open(path_generation_file, 'wb', 1)
    file_generation.write(text_success)
    file_generation.close()
    print text_success

    os.system('open %s' % path_generation_temp)  # 打开生成目录

if __name__=='__main__':
    main()
