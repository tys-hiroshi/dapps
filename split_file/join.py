#!/usr/bin/python
# coding: UTF-8

## https://qiita.com/5zm/items/49118188d76e61ca5113
import os

# 指定されたデータサイズでファイルを分割する
def divide_file(filePath, chunkSize):

    def read():
        with open(filePath, 'rb') as f:
            while True:
                data = f.read(chunkSize)
                if len(data) == 0:
                    return
                yield data

    def write(filePath, data):
        with open(filePath, 'wb') as f:
            f.write(data)

    def divide():
        for i, data in enumerate(read()):
            saveFilePath = '%s.%s' % (filePath, i)
            write(saveFilePath, data)
            yield saveFilePath

    return list(divide())

# 渡されたファイルリストの順序で１つのファイルに結合する
def join_file(fileList, filePath):

    with open(filePath, 'wb') as saveFile:
        for f in fileList:
            data = open(f, "rb").read()
            saveFile.write(data)
            saveFile.flush()

# 指定された部分データをファイルから取得する
def partial_content(filePath, start, end):

    partialSize = end - start + 1
    f = open(filePath, "rb")
    f.seek(start)
    data = f.read(partialSize)
    print(type(data))
    return data


# main
if __name__ == "__main__":
    fileList = ["upload20200708130502_ad2abea311d6412dbb47e0f9f4a9507c_000000.txt",
     "upload20200708130502_ad2abea311d6412dbb47e0f9f4a9507c_000001.txt"]
    target = "teststring.txt"
    # 分割したファイルを結合
    join_file(fileList, 'join_' + target)

    # 0-9999 の 10000 Byte を取り出す
    data01 = partial_content(target, 0, 9999)
    # 10000-残り全て を取り出す
    data02 = partial_content(target, 10000, os.path.getsize(target))
    # 結合して確かめる
    with open('partial_' + target, 'wb') as filePartial:
        filePartial.write(data01)
        filePartial.write(data02)