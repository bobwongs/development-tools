#!/usr/bin/python
# -*- coding: utf-8 -*-

' Text Template Generator '

__author__ = 'BobWong'

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

path_base = '/Users/'+ user_name +'/Desktop/Generator/UIProperty'
path_source_file = path_base + '/source.json'
path_generation_file = path_base + '/generation.txt'

def main():
    source = 'adfsfji <#Name#> djfoijdofijsd <#Name#> djofjdiohewrpwei\n djfoie<#Address#>jwoijr <#Address#>'
    config_dict = {
        'Name': 'BobWong',
        'Address': 'Guangzhou',
    }
    for k in config_dict:
        source = source.replace('<#%s#>' % k, config_dict[k])

if __name__=='__main__':
    main()
