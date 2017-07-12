
# coding: utf-8
# author: BobWong
# run: python generator_api_mananger.py ModuleName, ModuleName:The directory to include the generation

import os
import shutil  # 文件操作
import sys
import time
import getpass

# ---------- Parameters Setting ----------

# Basic
copyright_name = '月亮小屋（中国）有限公司'
project_name = 'BlueMoonHouse'
prefix_name = 'BMService'
suffix_name = ''
user_name = getpass.getuser()
author_name = user_name
import_file = '#import "BMService.h"'
base_class = 'BMService<BMService>'
module_name = 'BMService'

path_source = 'Source'
path_generation = 'Generation'
path_generation_api_manager = path_generation + '/%s' % module_name

year_string = time.strftime('%Y')  # 获得当前年份
date_string = time.strftime("%y/%m/%d")  # 获得当前日期，转换为字符串
time_string = time.strftime("%Y%m%d%H%M%S")

# 创建的APIManager文件目录名称，前者为从输入参数中获取，后者为定值
#dir_name = sys.argv[1]
dir_name = module_name

# ---------- Function ----------
def getTuple(line):
    # URL
    find_words_url = 'URL: '
    url = line[line.find(find_words_url)+len(find_words_url) : line.find(' Name: ')]
    # Name
    find_words_name = 'Name: '
    name = line[line.find(find_words_name)+len(find_words_name) : line.find(' APIManager: ')]
    # APIManager
    find_words_api_manager = 'APIManager: '
    api_manager = line[line.find(find_words_api_manager)+len(find_words_api_manager) : line.find(' Interface: ')]
    # Interface
    find_words_interface = 'Interface: '
    # 有无\n，有表示最后一行，没有表示不是最后一行
    if '\n' in line:
        interface = line[line.find(find_words_interface)+len(find_words_interface) : line.find('\n')]
    else:
        interface = line[line.find(find_words_interface)+len(find_words_interface) : ]

    return (url, name, api_manager, interface)

# 创建APIManager，并且返回接口宏定义的代码
def createAPIManager(source):
    (url, name, api_manager, interface) = getTuple(source)
    
    dir_path = path_generation_api_manager + '/' + dir_name
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    api_manager_name = prefix_name + api_manager + suffix_name #目录名即为APIManager的类名
    
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
                      '//  Created by %s on %s.\n' % (author_name, date_string) +
                      '//  Copyright © %s年 %s. All rights reserved.\n' % (year_string, copyright_name) +
                      '//\n' +
                      '\n' +
                      '%s\n' % (import_file) +
                      '\n' +
                      '@interface %s : %s\n' % (api_manager_name, base_class) +
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
                        '//  Created by %s on %s.\n' % (author_name, date_string) +
                        '//  Copyright © %s年 %s. All rights reserved.\n' % (year_string, copyright_name) +
                        '\n' +
                        '#import "%s.h"\n' % api_manager_name +
                        '\n' +
                        '@implementation %s\n' % api_manager_name +
                        '\n' +
                        '- (BOOL)isTestEnvironment\n' +
                        '{\n' +
                        '    return kBMIsTestEnvironment;\n' +
                        '}\n' +
                        '\n' +
                        '- (NSString *)formalApiBaseUrl\n' +
                        '{\n' +
                        '    return BASE_URL;\n' +
                        '}\n' +
                        '\n' +
                        '- (NSString *)testApiBasetUrl\n' +
                        '{\n' +
                        '#ifdef kISMockURL\n' +
                        '    return BASE_URL_MOCK_TEST;\n' +
                        '#else\n' +
                        '    return BASE_URL_TEST;\n' +
                        '#endif\n' +
                        '}\n' +
                        '\n' +
                        '- (NSString *)formalApiInterface\n' +
                        '{\n' +
                        '    return INTERFACE_%s;\n' % interface +
                        '}\n' +
                        '\n' +
                        '@end\n'
                       )
    file_implement_write.write(content_implement)
    file_implement_write.close()

    # 接口宏定义
#    macro_interface_definition = '#define INTERFACE_%s @"%s"  // %s' % (interface, url, name)

    # BMServiceFactory中的文件import
#    macro_interface_definition = '#import "BMService%s.h"' % api_manager

    # BMServiceFactory中的生成方法
    macro_interface_definition = (
                                 'if ([serviceIdentifier isEqualToString:kBMServiceId%s]) {\n' % api_manager +
                                 '    return [[BMService%s alloc] init];\n' % api_manager +
                                 '}'
                                  )

    # BMNetworkingConfiguration中的配置
#    macro_interface_definition = 'static NSString * const kBMServiceId%s = @"kBMServiceId%s";  // %s' % (api_manager, api_manager, name)

    # BMRequestGenerator中的签名方式
#    macro_interface_definition = '[serviceIdentifier isEqualToString:kBMServiceId%s] ||' % api_manager

    return macro_interface_definition
# ---------- Function ----------


# ------------ Main -------------
def main():
    
    # 读取文件
    file = open(path_source + '/source.txt', 'r')  # 这里使用相对路径
    array_line = file.readlines()
    file.close()

#    array_macro_interface = []
    macro_definition = ''
    for line in array_line:
        macro = createAPIManager(line)
#        array_macro_interface.append(macro)
        macro_definition = '%s%s\n' % (macro_definition, macro)

    path_generation_file = path_generation + '/generation_interface_definition.txt'
    file_macro = open(path_generation_file, 'wb', 1)
    file_macro.write(macro_definition)
    file_macro.close()

    os.system('open -a Xcode %s' % path_generation_file)  # 打开生成目录

    print '完成APIManager的生成操作'


# ------------Main-------------
if __name__=='__main__':
    main()
