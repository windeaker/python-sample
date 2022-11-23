import json
import os

# 列出文件夹下所有的文件
rootDirPath = 'E:\\76227904'
rootDir = os.listdir(rootDirPath)
jsonFileName = 'entry.json'
targetRootDir = "E:\\学习视频\\尚硅谷Netty视频教程"
for curDir in rootDir:
    curRootPath = rootDirPath + "\\" + curDir
    jsonFilePath = curRootPath + "\\" + jsonFileName
    fo = open(jsonFilePath, encoding='utf-8')
    jsonData = fo.readline()
    fo.close()
    jsonObject = json.loads(jsonData)
    videoName = jsonObject["page_data"]["part"]
    targetFilePath = targetRootDir + "\\" + videoName+".mp4"

    if os.path.exists(targetFilePath):
        pass
    else:
        print(curRootPath)
        print(targetFilePath)
        print('\n')
