import ctypes
import psutil
import time

class _THREADENTRY32(ctypes.Structure): 
    _fields_ = [('dwSize', ctypes.c_ulong), 
                ('cntUsage', ctypes.c_ulong), 
                ('th32thread_id', ctypes.c_ulong), 
                ('th32OwnerProcessID', ctypes.c_ulong),
                ('tpBasePri', ctypes.c_long),
                ('tpDeltaPri', ctypes.c_long),
                ('dwFlags', ctypes.c_ulong)]

def suspend_process(pid):
    thread_class = _THREADENTRY32
    current_thread = thread_class()
    current_thread.dwSize = ctypes.sizeof(thread_class)
    handle = ctypes.windll.kernel32.CreateToolhelp32Snapshot(ctypes.c_ulong(0x00000004), 0)
    threads = []
    more_threads = True
    while more_threads:
        if current_thread.th32OwnerProcessID == ctypes.c_ulong(pid).value:
            threads.append(current_thread.th32thread_id)
        more_threads = ctypes.windll.kernel32.Thread32Next(handle, ctypes.pointer(current_thread))
    ctypes.windll.kernel32.CloseHandle(handle)
    for thread in threads:
        handle = ctypes.windll.kernel32.OpenThread(0x0020 | 0x0002 | 0x0040, 0, thread)
        ctypes.PYFUNCTYPE(ctypes.c_ulong)(("SuspendThread", ctypes.windll.kernel32))(handle)
        ctypes.windll.kernel32.CloseHandle(handle)

def resume_process(pid):
    thread_class = _THREADENTRY32
    current_thread = thread_class()
    current_thread.dwSize = ctypes.sizeof(thread_class)
    handle = ctypes.windll.kernel32.CreateToolhelp32Snapshot(ctypes.c_ulong(0x00000004), 0)
    threads = []
    more_threads = True
    while more_threads:
        if current_thread.th32OwnerProcessID == ctypes.c_ulong(pid).value:
            threads.append(current_thread.th32thread_id)
        more_threads = ctypes.windll.kernel32.Thread32Next(handle, ctypes.pointer(current_thread))
    ctypes.windll.kernel32.CloseHandle(handle)
    for thread in threads:
        handle = ctypes.windll.kernel32.OpenThread(0x0020 | 0x0002 | 0x0040, 0, thread)
        ctypes.windll.kernel32.ResumeThread(handle)
        ctypes.windll.kernel32.CloseHandle(handle)

def main():
    process_list = [process.pid for process in psutil.process_iter() if process.name() == "GTA5.exe"]
    if len(process_list) > 0:
        print("GTA5.exe found.")
        suspend_process(process_list[0])
        print("GTA5.exe suspended. Sleeping for 8 seconds.")
        time.sleep(8)
        resume_process(process_list[0])

if __name__ == "__main__":
    main()