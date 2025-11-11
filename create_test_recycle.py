import os, struct, time

tmpdir = 'tmp_recycle'
if not os.path.isdir(tmpdir):
    os.makedirs(tmpdir)
# Names: $I123 and $R123
i_name = os.path.join(tmpdir, '$I123')
r_name = os.path.join(tmpdir, '$R123')
# Create $R file with some data
with open(r_name, 'wb') as f:
    f.write(b'Hello-Recycled-File')
# Create $I file version 1: header 3x Q (24 bytes) then 520 bytes pathname utf-16le
version = 1
size = os.path.getsize(r_name)
# Use current time as filetime (convert unix epoch to FILETIME)
WINDOWS_TICK = 10000000
SEC_TO_UNIX_EPOCH = 11644473600
filetime = int((time.time() + SEC_TO_UNIX_EPOCH) * WINDOWS_TICK)
header = struct.pack('<QQQ', version, size, filetime)
# Deleted pathname example: 'C:\Users\me\file.txt' plus trailing NUL, encoded utf-16le
pathname = 'C:\\tmp\\recovered.txt'
# Ensure trailing NUL
pathname_utf16 = (pathname + '\x00').encode('utf-16le')
# Pad to 520 bytes
if len(pathname_utf16) > 520:
    raise SystemExit('pathname too long for test')
pathname_utf16 = pathname_utf16.ljust(520, b'\x00')
with open(i_name, 'wb') as f:
    f.write(header)
    f.write(pathname_utf16)
print('Test files created in', tmpdir)
print('Running recycle_from_bin.py on', tmpdir)
import subprocess, sys
res = subprocess.run([sys.executable, 'recycle_from_bin.py', tmpdir], capture_output=True, text=True)
print('STDOUT:')
print(res.stdout)
print('STDERR:')
print(res.stderr)
print('Exit code:', res.returncode)
