import os

dirs = os.listdir("E:\Music\HighQuality")
print("dirs: %s" % dirs)
dirs = os.listdir()
print("dirs: %s" % dirs)

musicFiles = dict()

print("dirs: %s" % musicFiles)

print("abs path: %s" % os.path.abspath("."))

print(os.walk(os.path.abspath(".")))


def get_filelist(dir):
    Filelist = []
    newDir = dir
    if os.path.isfile(dir):
        Filelist.append(dir)
        # # 若只是要返回文件文，使用这个
        # Filelist.append(os.path.basename(dir))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if s == "xxx":
            # continue
            newDir = os.path.join(dir, s)
            merge(Filelist, get_filelist(newDir))
    return Filelist


def merge(target, source):
    for item in source:
        target.append(item)


files = get_filelist("E:\Music\HighQuality")
for file in files:
    print(file)
