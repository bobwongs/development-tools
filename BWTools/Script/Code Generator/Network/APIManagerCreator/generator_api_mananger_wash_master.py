
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
prefix_name = 'BM'
suffix_name = 'APIManager'
user_name = getpass.getuser()
author_name = user_name
import_file = '#import "BMBaseAPIManager.h"'
base_class = 'BMBaseAPIManager'
module_name = 'APIManager'

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
                        '#import "BMUserCenter.h"\n' +
                        '#import "BMConstantMacroMessage.h"\n' +
                        '\n' +
                        '@interface %s () <BMAPIManager, BMAPIManagerInterceptor, BMAPIManagerValidator>\n' % api_manager_name +
                        '\n' +
                        '@property (nonatomic, copy, readwrite) NSString *errorMessage;\n' +
                        '\n' +
                        '@end\n' +
                        '\n' +
                        '@implementation %s\n' % api_manager_name +
                        '\n' +
                        '#pragma mark - 生命周期\n' +
                        '\n' +
                        '- (instancetype)init\n' +
                        '{\n' +
                        '    self = [super init];\n' +
                        '    if (self) {\n' +
                        '        self.validator = self;\n' +
                        '        self.interceptor = self;\n' +
                        '    }\n' +
                        '    return self;\n' +
                        '}\n' +
                        '\n' +
                        '#pragma mark - BMAPIManager manager\n' +
                        '\n' +
                        '- (NSString *)methodName\n' +
                        '{\n' +
                        '    return @"%s";\n' % api_manager_name +
                        '}\n' +
                        '\n' +
                        '- (NSString *)serviceIdentifier\n' +
                        '{\n' +
                        '    return kBMServiceId%s;\n' % api_manager +
                        '}\n' +
                        '\n' +
                        '- (BMAPIManagerRequestType)requestType\n' +
                        '{\n' +
                        '    return BMAPIManagerRequestTypeJSONPost;\n' +
                        '}\n' +
                        '\n' +
                        '- (BOOL)shouldCache\n' +
                        '{\n' +
                        '    return NO;\n' +
                        '}\n' +
                        '\n' +
                        '#pragma mark - BMAPIManagerValidator 验证器\n' +
                        '\n' +
                        '- (BOOL)manager:(BMBaseAPIManager *)manager isCorrectWithCallBackData:(NSDictionary *)data\n' +
                        '{\n' +
                        '    if (!isAPICallingSuccess(data)) {\n' +
                        '        self.errorMessage = getAPICallingResponseMsg(data);\n' +
                        '        return NO;\n' +
                        '    }\n' +
                        '    return YES;\n' +
                        '}\n' +
                        '\n' +
                        '- (BOOL)manager:(BMBaseAPIManager *)manager isCorrectWithParamsData:(NSDictionary *)data\n' +
                        '{\n' +
                        '    return YES;\n' +
                        '}\n' +
                        '\n' +
                        '#pragma mark - BMAPIManagerInterceptor 拦截器\n' +
                        '//是否允许调用api\n' +
                        '- (BOOL)manager:(BMBaseAPIManager *)manager shouldCallAPIWithParams:(NSDictionary *)params\n' +
                        '{\n' +
                        '    if (![BMUserCenter sharedInstance].isLogined) {\n' +
                        '        self.errorMessage = BMMessageNotAllowCallingAPI;\n' +
                        '        [[NSNotificationCenter defaultCenter] postNotificationName:BMNOTIFICATION_REQUEST_LOGIN object:@{kBMManager: manager,kBMLoginReason:@(LoginReasonUserLoginAndPrompt)}];\n' +
                        '        return NO;\n' +
                        '    }\n' +
                        '    if (![BMUserCenter sharedInstance].istokenValid) {\n' +
                        '        [[NSNotificationCenter defaultCenter] postNotificationName:BMNOTIFICATION_REQUEST_LOGIN object:@{kBMManager: manager,kBMLoginReason:@(LoginReasonTokenInvalidAndPrompt)}];\n' +
                        '        return NO;\n' +
                        '    }\n' +
                        '    return YES;\n' +
                        '}\n' +
                        '\n' +
                        '#pragma mark - 重写父类格式化参数方法\n' +
                        '\n' +
                        '- (NSDictionary *)reformParams:(NSDictionary *)params\n' +
                        '{\n' +
                        '    NSMutableDictionary *mutableParams = params?[[super reformParams:params] mutableCopy]:[[NSMutableDictionary alloc] init];\n' +
                        '    NSString *token = [BMUserCenter sharedInstance].token;\n' +
                        '    [mutableParams setObject:token forKey:kBMToken];\n' +
                        '    return mutableParams;\n' +
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
    file = open(path_source + '/source.txt', 'r')  # 这里使用相对路径
    array_line = file.readlines()
    file.close()

#    array_macro_interface = []
    macro_definition = ''
    for line in array_line:
        macro = createAPIManager(line)
#        array_macro_interface.append(macro)
        macro_definition = '%s%s\n' % (macro_definition, macro)

    file_macro = open(path_generation + '/generation_interface_definition.txt', 'wb', 1)
    file_macro.write(macro_definition)
    file_macro.close()

    print '完成APIManager的生成操作'


# ------------Main-------------
if __name__=='__main__':
    main()
