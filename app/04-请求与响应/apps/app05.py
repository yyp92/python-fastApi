# form 表单数据
from fastapi import APIRouter, File, UploadFile
from typing import List
import os

app05 = APIRouter()

@app05.post("/file")
async def get_file(file: bytes = File()):
    print("file", file)
    
    return {
        "file": len(file)
    }

@app05.post("/files")
async def get_files(files: List[bytes] = File(...)):
    for file in files:
        print("file", len(file))
    
    return {
        "files": len(files)
    }

@app05.post("/uploadFile")
async def get_uploadFile(file: UploadFile = File(...)):
    print("file", file)

    # __file__ 代表当前app05.py文件的完整路径
    save_dir = os.path.join(os.path.dirname(__file__), "../imgs")
    # 拼接完整保存文件路径：imgs 文件夹 + 上传的原文件名
    path = os.path.join(save_dir, file.filename)
    # 规范化路径，消除 ..
    save_dir = os.path.abspath(save_dir)
    # 创建文件夹，存在不会报错
    os.makedirs(save_dir, exist_ok=True)

    # with：自动管理资源上下文，代码块结束后自动执行清理操作（关闭文件、释放连接），不用手动写 close()，哪怕代码异常也能正常释放资源。
    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)
    
    return {
        "file": file.filename
    }

@app05.post("/uploadFiles")
async def get_uploadFiles(files: List[UploadFile] = File(...)):
    print("files", files)
    
    return {
        # [file.filename for file in files] -> 列表推导式 写法
        "fileNames": [file.filename for file in files]
    }
