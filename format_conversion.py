#!/usr/bin/env python
# -*- coding: utf-8 -*-
# time: 2023/9/13 20:13
# file: format_conversion.py
# author: qinxi
# email: 1023495336@qq.com
import os

# 检查host.txt文件是否存在
if not os.path.exists('host.txt'):
    print("host.txt文件不存在。请将host.txt文件放在当前路径并重新运行程序。")
    #return

def convert_host_file():
    # 打开输入文件host.txt和输出文件output.txt
    with open('host.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
        lines = input_file.readlines()

        # 遍历文件行
        i = 0
        while i < len(lines):
            # 获取主机名
            hostname = lines[i].strip()
            i += 1

            # 获取IP地址
            ip = lines[i].strip()
            i += 1

            # 写入格式化后的数据到输出文件
            output_file.write(f'[{hostname}]\n{ip}\n')
            print(f'[{hostname}]\n{ip}\n')
    print("文件已添加主机名，IP，生成：output.txt")

def list_ip_addresses():
    # 打开输入文件host.txt
    with open('host.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
        lines = input_file.readlines()

        # 遍历文件行，输出IP地址列表
        i = 0
        while i < len(lines):
            i += 1  # 跳过主机名
            ip = lines[i].strip()
            i += 1
            # 写入格式化后的数据到输出文件
            output_file.write(f'{ip}\n')
            print(f'{ip}\n',end='')
    print("文件已列表显示，生成：output.txt")

def comma_ip_list():
    # 打开输入文件host.txt
    with open('host.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
        lines = input_file.readlines()

        # 遍历文件行，输出IP地址列表
        i = 0
        while i < len(lines):
            i += 1  # 跳过主机名
            ip = lines[i].strip()
            i += 1

            # 写入格式化后的数据到输出文件
            output_file.write(f'{ip}')
            print(f'{ip}',end='')

            if i <len(lines):
                output_file.write(',')
                print(',',end='')
        print('\n')
    print("文件已经添加逗号分隔，生成：output.txt")


choose = input("please choose the option (1 主机名+IP地址 2 IP列表 3 逗号分割IP列表): ")

if choose == '1':
    # 调用函数
    convert_host_file()  # 将host.txt文件转换为所需格式并保存到output.txt
elif choose == '2':
    list_ip_addresses()  # 输出IP地址列表
elif choose == '3':
    comma_ip_list()
else:
    print('nothing to do....')
