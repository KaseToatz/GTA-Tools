from ctypes import Structure, c_ulong, c_long, sizeof, windll, pointer, PYFUNCTYPE
from psutil import process_iter
from time import sleep

class _THREADENTRY32(Structure): 
    _fields_ = [('dwSize', c_ulong), 
                ('cntUsage', c_ulong), 
                ('th32thread_id', c_ulong), 
                ('th32OwnerProcessID', c_ulong),
                ('tpBasePri', c_long),
                ('tpDeltaPri', c_long),
                ('dwFlags', c_ulong)]

def suspend_process(pid):
    thread_class = _THREADENTRY32
    current_thread = thread_class()
    current_thread.dwSize = sizeof(thread_class)
    handle = windll.kernel32.CreateToolhelp32Snapshot(c_ulong(0x00000004), 0)
    threads = []
    more_threads = True
    while more_threads:
        if current_thread.th32OwnerProcessID == c_ulong(pid).value:
            threads.append(current_thread.th32thread_id)
        more_threads = windll.kernel32.Thread32Next(handle, pointer(current_thread))
    windll.kernel32.CloseHandle(handle)
    for thread in threads:
        handle = windll.kernel32.OpenThread(0x0020 | 0x0002 | 0x0040, 0, thread)
        PYFUNCTYPE(c_ulong)(("SuspendThread", windll.kernel32))(handle)
        windll.kernel32.CloseHandle(handle)

def resume_process(pid):
    thread_class = _THREADENTRY32
    current_thread = thread_class()
    current_thread.dwSize = sizeof(thread_class)
    handle = windll.kernel32.CreateToolhelp32Snapshot(c_ulong(0x00000004), 0)
    threads = []
    more_threads = True
    while more_threads:
        if current_thread.th32OwnerProcessID == c_ulong(pid).value:
            threads.append(current_thread.th32thread_id)
        more_threads = windll.kernel32.Thread32Next(handle, pointer(current_thread))
    windll.kernel32.CloseHandle(handle)
    for thread in threads:
        handle = windll.kernel32.OpenThread(0x0020 | 0x0002 | 0x0040, 0, thread)
        windll.kernel32.ResumeThread(handle)
        windll.kernel32.CloseHandle(handle)

def main():
    process_list = [process.pid for process in process_iter() if process.name() == "GTA5.exe"]
    if len(process_list) > 0:
        print("GTA5.exe found.")
        suspend_process(process_list[0])
        print("GTA5.exe suspended. Sleeping for 8 seconds.")
        sleep(8)
        resume_process(process_list[0])

if __name__ == "__main__":
    main()