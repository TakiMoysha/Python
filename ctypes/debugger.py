import sys
import time

from ctypes import *
from debugger_defines import *

PROCESS_ALL_ACCESS = 0xFFFF


kernel32 = windll.kernel32

class Debugger():
    def __init__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = False


    def load(self, path_to_exe):
        creation_flags = DEBUG_PROCESS

        startupinfo = STARTUPINFO()
        processinfo = PROCESS_INFORMATION()

        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        startupinfo.cb = sizeof(startupinfo)

        if kernel32.CreateProcessW(path_to_exe, None, None, None, None,
            creation_flags, None, None,
            byref(startupinfo),
            byref(processinfo)
        ):
            print("[*] Process launched")
            print(f"[*] The Process ID I have is: {processinfo.dwProcessId}")
            self.h_process = self.open_process(processinfo.dwProcessId)

        else:
            print(f"[*] Error with error code {kernel32.GetLastError()}.")


    def open_process(salf, pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, pid, False)
        return h_process


    def attach(self, pid):
        self.h_process = self.open_process(pid)

        if kernel32.DebugActiveProcess(pid):
            self.debugger_ctive = True
            self.pid = int(pid)
        else:
            print("[*] Unable to attach to the process.")

    def detach(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print("[*] Finished debugging. Exiting...")
            return True
        else:
            print("There was an error")
            return False