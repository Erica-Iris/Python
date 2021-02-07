
__all__ = ["remove", "move", "mkdir", "join", "size", "ls_ext",
           "read_int", "write_int"]

import os

join = os.path.join

def remove(f):
    try:
        os.remove(f)
    except:
        pass

def move(src, dst):
    try:
        os.rename(src, dst)
    except:
        pass

def mkdir(d):
    if os.path.exists(d):
        return
    try:
        os.mkdir(d)
    except:
        pass

def size(f):
    if os.path.exists(f):
        return os.path.getsize(f)
    return 0

def ls_ext(d, ext):
    """
    return a list of files with specific extension in a folder
    """
    for f in os.listdir(d):
        if os.path.splitext(f)[-1].lower() != ext:
            continue
        p = join(d, f)
        if os.path.isfile(p):
            yield f

def read_int(p):
    """
    read an integer from a file
    """
    if os.path.exists(p):
        try:
            f = None
            f = open(p, "rb")
            i = f.readline().strip()
            f.close()
            if i.isdigit():
                return max(0, int(i))
        except:
            if f:
                f.close()
    return 0

def write_int(p, i):
    """
    write an integer to a file
    """
    try:
        f = None
        f = open(p, "wb")
        f.write("%s\n" % i)
        f.close()
    except:
        if f:
            f.close()

