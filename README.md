# recycle_from_bin.py: restore files from Windows Recycle Bin directory

recycle_from_bin.py is a command-line tool Python script which restores all
files (by moving and renaming them) from a Windows Recycle Bin directory. It
works with and 3 (>= 3.0) and Python 2 (>= 2.4), and it works on Linux,
macOS (and other Unix-like systems) and Windows.

By default it restores files into the original sourc directories.
Verbose mode included so you can see what's happening.

It doesn't overwrite files in the restore target directory, but it appends a
number to the filename to disambiguate.

It works for filenames contaning any characters (even non-ASCII).

Example usage on Linux:

```
  ./recycle_from_bin.py /media/foo/bar/'$Recycle.Bin'
```

Example usage on Windows (verbose mode):

```
  python recycle_from_bin.py -v "C:\$Recycle.Bin"
```

The license of recycle_from_bin.py is GNU GPL 2.0 or newer.
