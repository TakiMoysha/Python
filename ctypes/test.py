import debugger


debugger = debugger.Debugger()

# pid = input("Pid: ")
pid = 13084

debugger.attach(int(pid))

debugger.detach()
