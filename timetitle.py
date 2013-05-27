import win32gui
import time
import win32api
import win32con
import win32process

def getForegroundWindowProcessInfo(foregroundHWND):
    t, pid = win32process.GetWindowThreadProcessId(foregroundHWND)
    #print 'pid:' + str(pid)
    handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION|win32con.PROCESS_VM_READ, 0, pid)
    #print 'Handle:' + str(handle)
    path = win32process.GetModuleFileNameEx(handle, 0)
    win32api.CloseHandle(handle)
    #print path
    return path, pid

def getForegroundWindowTitle():
    foregroundHWND = win32gui.GetForegroundWindow()
    #print foregroundHWND
    title = win32gui.GetWindowText(foregroundHWND)
    #print title
    return title, foregroundHWND

if __name__ == '__main__':
    lastTitle = ''
    lastPid = 0
    while 1:
        try:
            title, foregroundHWND = getForegroundWindowTitle()
            path, pid = getForegroundWindowProcessInfo(foregroundHWND)
            if title != lastTitle or pid != lastPid:
                print '['+time.ctime() + '] , Title= [' +  title + ' ], Path="'+path +'" , pid=['+str(pid)+']'
                lastTitle = title
                lastPid = pid
        except Exception as e:
            print time.ctime() + 'Error: ' + str(e)

	time.sleep(2)

