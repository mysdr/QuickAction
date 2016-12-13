from SysTrayIcon import SysTrayIcon 
 
import os
import sys
import subprocess
import threading
import time

def fun(cmd):
    t = threading.Thread(target=fun1, args=(cmd,))
    t.start()
def fun1(cmd):
    cmd = '"'+cmd+'"'
    print(cmd)
    if(cmd.split('\\')[-1][3]=='-'):
        os.system(cmd)
    else: subprocess.call(cmd, shell=True)

def reboot():
    fun('quickAction.pyw')
    time.sleep(0.5)
    os._exit(0)
    
def getItem(d, f):
    if f[3] != '_' and f[3] != '-':
        return (f, None, lambda cmd = d + f:fun(cmd))
    if f[4:9] == '-----':
        return ('', None, 'separator')
    return (f[4:], None, lambda cmd = d + f:fun(cmd))
    


d = 'actions\\002_autorun\\'
files = os.listdir(d)
for f in files:
    if not os.path.isdir(d + f):
        fun(d + f)


res = [('重启程序', None, lambda: reboot())]
d = 'actions\\'
files = os.listdir(d)
for f in files:
    if os.path.isdir(d + f):
        dd = d + f + '\\'
        ffiles = os.listdir(dd)
        rres = []
        for ff in ffiles:
            if not os.path.isdir(dd + ff):
                rres.append(getItem(dd, ff))
        if len(rres) == 0: pass
        elif f[3] == '_':
            res.append((f[4:], None,tuple(rres)))
        else: res.append((f, None,tuple(rres)))
    else:
        res.append(getItem(d, f))         
menu_options = tuple(res)

SysTrayIcon('icon.ico', "QuickAction", menu_options, passClass = False)

