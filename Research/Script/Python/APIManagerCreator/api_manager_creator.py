
# coding: utf-8
# Author: Bobwong

import os
import shutil

# Function
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


# Main
def main():
    dir_name = 'APIManager'

    url = 'URL: washMall/appointment/getExpressCompanyList Name: 获取快递公司列表 APIManager: GetExpressCompanyList Interface: GET_EXPRESS_COMPANY_LIST'
    (url, name, api_manager, interface) = getTuple(url)
    
    print url
    print name
    print api_manager
    print interface

    if os.path.exists(dir_name):
        print 'APIManager exits'
        return

    os.mkdir(dir_name)

    


if __name__=='__main__':
    main()
