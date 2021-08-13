# -*- coding: utf-8 -*-
import win32process#Process module
from win32con import PROCESS_ALL_ACCESS #Opencress Authority
import win32api#Call system module
import ctypes#CLanguage type
from win32gui import FindWindow#interface

#A read operation to the game, read the blood volume.。

def GetProcssID(address,bufflength):
    pid = ctypes.c_ulong() #//Set pid to unsigned single precision type
    kernel32 = ctypes.windll.LoadLibrary("kernel32.dll")#//Load dynamic link library
    hwnd = FindWindow(None, u"tomcat-users.xml - Notepad")#//Get window handle  "XYElementClient Window"
    hpid, pid = win32process.GetWindowThreadProcessId(hwnd)#//Get windowID
    print(hpid, pid)
    hProcess = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)#//Get process handle
    ReadProcessMemory = kernel32.ReadProcessMemory
    addr = ctypes.c_ulong()
    ReadProcessMemory(int(hProcess), address, ctypes.byref(addr), bufflength, None)#//Read memory
    win32api.CloseHandle(hProcess)#//Close handle
    return addr.value

def main():
    addr = GetProcssID(0x2D9C8, 4) #1BA7B1C22D1 0xD0DF1C  0x2CA90
    print(addr)
    ret = addr + 0x1C    
    ret2 = GetProcssID(ret, 4)
    ret3 = ret2 + 0x28
    ret4 = GetProcssID(ret3, 4)
    ret5 = ret4 + 0x288
    ret6 = GetProcssID(ret5, 4) #// Incoming offset address
    print ("Hp:%d" % ret6)


if __name__ == '__main__':
    main()
#————————————————
#版权声明：本文为CSDN博主「Wrpzkb」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/keyb396/article/details/90138778
