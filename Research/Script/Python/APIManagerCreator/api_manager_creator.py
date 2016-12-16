
# coding: utf-8
# Author: Bobwong

import os
import shutil
import sys

#dir_name = sys.argv[1]
dir_name = 'APIManager'

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
    interface = line[line.find(find_words_interface)+len(find_words_interface) : line.find('\n')]
    return (url, name, api_manager, interface)

# 创建APIManager，并且返回接口宏定义的代码
def createAPIManager(source):
    (url, name, api_manager, interface) = getTuple(source)
    
#    dir_path = 'BMExpress'
    dir_path = dir_name
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    api_manager_name = 'BM' + api_manager + 'APIManager' #目录名即为APIManager的类名
    
    path_api_manager = '%s/%s' % (dir_path, api_manager_name)
    if os.path.exists(path_api_manager):
        print 'Directory ' + api_manager_name + ' exits'
        print 'Remove Old ' + api_manager_name + '\n'
        shutil.rmtree(path_api_manager)
    
    os.mkdir(path_api_manager)  #创建目录
    
    # 头文件.h
    file_header_write = open('%s/%s/%s.h' % (dir_path, api_manager_name, api_manager_name), 'wb', 1)
    content_header = (
                      '//\n' +
                      '//  ' + api_manager_name + '.h\n' +
                      '//  BMWash\n' +
                      '//\n' +
                      '//  Created by BobWong on 16/12/16.\n' +
                      '//  Copyright © 2016年 月亮小屋（中国）有限公司. All rights reserved.\n' +
                      '//\n' +
                      '\n' +
                      '#import "BMBaseAPIManager.h"\n' +
                      '\n' +
                      '@interface %s : BMBaseAPIManager\n' % (api_manager_name) +
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
                       '//  BMWash\n' +
                       '//\n' +
                       '//  Created by BobWong on 16/12/16.\n' +
                       '//  Copyright © 2016年 月亮小屋（中国）有限公司. All rights reserved.\n' +
                       '//\n' +
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
    
    # 读取文件
    file = open('resource.txt', 'r')  # 这里使用相对路径
    array_line = file.readlines()
    file.close()

#    array_macro_interface = []
    macro_definition = ''
    for line in array_line:
        macro = createAPIManager(line)
#        array_macro_interface.append(macro)
        macro_definition = '%s%s\n' % (macro_definition, macro)

    file_macro = open('macro.txt', 'wb', 1)
    file_macro.write(macro_definition)
    file_macro.close()

    print '完成APIManager的生成操作'

# ------------Main-------------


if __name__=='__main__':
    main()
