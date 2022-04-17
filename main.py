
import os
from subprocess import STD_ERROR_HANDLE, STD_INPUT_HANDLE
from tkinter import E
from turtle import color
from getexcel import *
import tkinter as tk
from tkinter import filedialog
import time
from os import system, name
import ctypes
import sys

print("请选择花名册文件与作业文件夹（若曾经选择过花名册文件，则只需选择作业文件夹）")

'''打开选择文件夹对话框'''
classmates_info = get_infos()

root = tk.Tk()
root.withdraw()
filePath = filedialog.askdirectory()  # 获得选择好的文件夹
filenames = os.listdir(filePath)

"""控制输出颜色代码"""
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_RED = 0x0c
FOREGROUND_GREEN = 0x0a
FOREGROUND_BLUE = 0x09

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool


def resetColor():
    set_cmd_text_color(FOREGROUND_GREEN | FOREGROUND_RED | FOREGROUND_BLUE)


def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()
    print()


def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess)
    print()
    resetColor()


"""清屏函数"""


def clear():
    if name == "nt":
        _ = system("cls")


"""输出函数"""


def output():
    mits = []
    n = 0
    for classmate in classmates_info:
        for filename in filenames:
            if classmate["id"] in filename:
                mits.append(classmate)
                n += 1
    printGreen(f"\n已交同学的名单为，共{n}人:")

    for i in range(1, len(mits)+1):
        print(mits[i-1]["name"], end=" ")
        if i % 6 == 0:
            print()  # 输出已交作业同学名字

    umits = []
    m = len(classmates_info)-n

    for classmate in classmates_info:
        if classmate not in mits:
            umits.append(classmate)
    if len(umits) == 0:
        printGreen("\n\n已全部交齐")

    else:
        print()
        printRed(" ")
        printRed(f"未交同学的名单为,共{m}人:")
        # print(f"\033[31m\n\n未交同学的名单为,共{m}人:\033[0m")

        for i in range(1, len(umits)+1):
            print(umits[i-1]["name"], end=" ")
            if i % 6 == 0:
                print()


output()
while True:
    filenames_change = os.listdir(filePath)
    if filenames != filenames_change:
        filenames = filenames_change
        clear()
        output()
