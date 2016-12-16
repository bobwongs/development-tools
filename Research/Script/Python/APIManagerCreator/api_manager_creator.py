
# coding: utf-8
# Author: Bobwong

import os
import shutil

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
    interface = line[line.find(find_words_interface)+len(find_words_interface) : ]
    return (url, name, api_manager, interface)

def createApiManager(source):
    url = 'URL: washMall/appointment/getExpressCompanyList Name: 获取快递公司列表 APIManager: GetExpressCompanyList Interface: GET_EXPRESS_COMPANY_LIST'
    (url, name, api_manager, interface) = getTuple(url)
    
    api_manager_name = 'BM' + api_manager + 'APIManager' #目录名即为APIManager的类名
    
    if os.path.exists(api_manager_name):
        print 'Directory ' + api_manager_name + ' exits'
        print 'Remove Old APIManager'
        shutil.rmtree(api_manager_name)
    #        return
    
    os.mkdir(api_manager_name)  #创建目录

# 接口宏定义
macro_interface_definition = '#define INTERFACE_%s @"%s"  // %s' % (interface, url, name)
    print macro_interface_definition
    
    # 头文件.h
    file_header_write = open('%s/%s.h' % (api_manager_name, api_manager_name), 'wb', 1)
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
                      file_implement_write = open('%s/%s.m' % (api_manager_name, api_manager_name), 'wb', 1)
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


# ------------ Main -------------
def main():
    
    # 读取文件
    file = open('resource.txt', 'r')  # 这里使用相对路径
    array_line = file.readlines()
    file.close()
    

# ------------Main-------------


if __name__=='__main__':
    main()
