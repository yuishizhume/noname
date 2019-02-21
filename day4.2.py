# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:02:48 2019

@author: Administrator
"""
#day4.2

#模块
#在Python中，一个.py文件就称之为一个模块（Module）。
#https://docs.python.org/2/library/functions.html
#为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
#假设我们的模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。
#方法是选择一个顶层包名，比如mycompany，在目录下存放：
#模块的名字就变成了mycompany.模块
#__init__.py
#请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的
#否则，Python就把这个目录当成普通目录，而不是一个包。
#__init__.py可以是空文件，也可以有Python代码
#因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
#可以有多级目录，组成多级层次的包结构。

#使用模块
#Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。
#我们以内建的sys模块为例，编写一个hello的模块：
#查看hello.py