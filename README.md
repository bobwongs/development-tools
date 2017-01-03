# BWiOSDevelopmentTools
iOS开发工具

## 目录

- 开发工具
- 设计
- 实现
- 运用
- 优化方向
- Follow Me

## 开发工具

避免开发过程中重复性的工作，减少人为的失误，提升开发效率；

开发经验形成开发的一套模板，通过生成模板代码，进行快速的编码。

## 设计

### MVC文件和代码的生成器设计

#### 设计理念

> Xcode中的iOS项目本身就是设计成MVC模式的，因此创建和编写Controller、Model、View都是在iOS功能界面的开发中很频繁的操作，而且每次创建文件和编写代码都有很多重复性的工作，如Controller的Title，在此通过一个文件的配置，脚本去该文件中解析和提取字符串信息，生成文件和模板代码，可以很大程度上提升开发效率。

#### 必须创建的文件和编写的代码

Controller、Model、View目录

Controller的模板代码

#### 配置参数设计

Controller：Controller Name、Title

优化：头文件导入配置、导航条配置、TableView配置

#### 源文件数据格式



### Property的Getter和Setter方法的生成器

#### 设计理念

> 为Property快速生成Getter和Setter方法，也可以为UI生成setUI和基于Masonry的setConstraints方法

#### 参数配置设计

源文件中读取Property，生成代码到目标文件，再从目标文件把代码拷贝到项目中

### 接口文件的生成器

#### 设计理念

> 接口设计为，每个接口都是一个类，而且要对接口链接进行宏定义，这些是创建一个接口都需要的步骤，所以通过开发工具，只要在源文件做好配置就能快速生成文件和项目代码，之后直接导入接口文件进入项目和拷贝宏定义接口代码到项目接口配置文件中

#### 参数设计

URL、类文件名称、注释、接口宏定义命名

## 实现

技术选用——Python脚本

## 运用



## 优化方向

脚本参数配置项设置，增加脚本的参数配置项，让生成器更加强大；

作为Xcode插件的形式；

用Swift直接开发一个Mac OS的程序，进行快速的生成；

iOS Xcode项目脚本生成，只需要配置一些参数，就可以把基础性的配置和代码编写好；

## Follow Me

Github:[https://github.com/bobwongs](https://github.com/bobwongs)

简书: [http://www.jianshu.com/users/9d21ec83358a/top_articles](http://www.jianshu.com/users/9d21ec83358a/top_articles)