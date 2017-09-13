# coding=utf-8
import os
print os.name #显示当前使用平台
#'nt'表示windows,'posix'表示LINUX
print os.getcwd()#显示当前python脚本工作路径
print os.listdir('C:\Users\zhang\Documents\GitHub\python_os_module')#返回指定目录下的所有文件
print os.sep #显示当前平台下路径分隔符
print os.linesep #给出平台使用的行终止符
print os.path.abspath('os_example.py') #显示当前绝对路径
print os.path.dirname('os_example.py')#返回该路径的父目录
os.stat('file')#获取文件或目录信息
os.path.join('path','name')#连接目录与文件名或目录 结果为path/name
os.curdir #返回当前目录：（'.')
os.chdir('dirname')#用于改变当前工作目录到指定路径相当于shell cd
os.path.splitext('path')#分离文件名和扩展名
os.path.isdir('path')#如果存在这个目录为true
str.startswith('str')#判断一个文本是否以某个或几个字符开始，返回TRUE 或false
str.endswith('str')#同上
assert os.remove('dirname')#删除一个文件
assert os.makedirs('dirname/dirname')#可生成多层递归目录
assert os.rmdir('dirname') #删除单级目录
assert os.rename('oldname','newname')
assert os.system() #运行shell命令