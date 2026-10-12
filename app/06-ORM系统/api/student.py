from fastapi import APIRouter, Request, HTTPException
from models import *
from pydantic import BaseModel, field_validator
from typing import List, Union
from fastapi.templating import Jinja2Templates
# 作用：操作操作系统，文件、路径、环境变量、执行系统命令，跨平台兼容 Mac / Linux / Windows。
import os
# re 是 Python 内置标准库，全称 regular expression，正则表达式模块，专门用来做字符串的复杂匹配、查找、校验、替换。
import re

student_api = APIRouter()

@student_api.get("/")
async def getAllStudent():
    # 1. 查询所有 all 方法 ，返回 QuerySet 对象
    # students = await Student.all()
    # print("students:", students)
    # for student in students:
    #     print(student.name)

    # 2. 过滤查询 filter，返回 QuerySet 对象
    # students = await Student.filter(name = "王五")
    # students = await Student.filter(clas_id = 1)
    # print("students:", students)

    # 3. get 方法，返回 ModelInstance 对象
    # students = await Student.get(id = 1)
    # print("students:", students, students.name)

    # 4. 模糊查询, __gt= 相当于 >
    # students = await Student.filter(sno__gt = 2001)
    # students = await Student.filter(sno__range = [1, 2000])
    # students = await Student.filter(sno__in = [2001, 2002])
    # print("students:", students)

    # 5. values 查询
    # students = await Student.filter(sno__range = [1, 10000])
    # students = await Student.all().values("name", "sno")
    # print("students:", students)

    # 6. 一对多查询 和 多对多查询
    # students = await Student.get(name = "李五")
    # print(students.name)
    # print(students.sno)
    # print(students.clas_id)
    # print(await students.clas.values("name"))
    # students = await Student.all().values("name", "clas__name")
    # print(await students.courses.all().values("name"))
    # print(await students.courses.all().values("name", "teacher__name"))
    students = await Student.all().values("name", "clas__name", "courses__name")

    return {
        "message": "查看的学生",
        "data": students,
    }


class StudentIn(BaseModel):
    name: str
    pwd: str
    sno: int
    clas_id: int
    courses: List[int] = []

    @field_validator("name")
    def name_must_chinese(value):
        # 这个开头的 r，作用：关闭 Python 字符串的转义功能
        # [\u4e00‑\u9fa5·]  => 匹配一个汉字，或者一个间隔号・
        if not re.fullmatch(r"^[\u4e00-\u9fa5·]+$", value):
            raise ValueError("姓名只能是汉字，可包含中间间隔号·")
        return value

    @field_validator("sno")
    def sno_validator(value):
        # assert 是 Python 内置关键字：断言，用来做校验
        # 语法： assert 条件, 错误提示字符串
        assert value > 1000 and value < 10000, "学号要在1000-10000的范围内"
        return value

@student_api.post("/")
async def addStudent(studentIn: StudentIn):
    # 插入到数据库

    # 方式 1
    # student = Student(
    #     name=studentIn.name,
    #     pwd=studentIn.pwd,
    #     sno=studentIn.sno,
    #     clas_id=studentIn.clas_id,
    # )
    # 插入到数据库的操作
    # await student.save()

    # 方式 2
    student = await Student.create(
        name=studentIn.name,
        pwd=studentIn.pwd,
        sno=studentIn.sno,
        clas_id=studentIn.clas_id,
    )

    # 多对多的关系绑定
    chooseCourses = await Course.filter(id__in = studentIn.courses)
    await student.courses.add(*chooseCourses)

    return {
        "message": "添加一个学生",
        "data": student
    }


@student_api.get("/{studentId}")
async def getOneStudent(studentId: int):
    student = await Student.get(id = studentId)

    return {
        # 开头的 f：标记这是 f‑string；告诉 Python：字符串里面大括号 `{}` 里面是变量 / 表达式，不是普通文本
        "message": f"查看 id={studentId} 的学生",
        "data": student,
    }


@student_api.put("/{studentId}")
async def updateStudent(studentId: int, studentIn: StudentIn):
    newData = studentIn.model_dump()
    # newData 删除 courses 字段
    courses = newData.pop("courses")
    await Student.filter(id = studentId).update(**newData)

    # 设置多对多的选修课程
    editStudent = await Student.get(id = studentId)
    chooseCourses = await Course.filter(id__in = courses)
    await editStudent.courses.clear()
    await editStudent.courses.add(*chooseCourses)

    return {
        "message": f"更新 id={studentId} 的学生"
    }


@student_api.delete("/{studentId}")
async def deleteStudent(studentId: int):
    deleteCount = await Student.filter(id = studentId).delete()

    if not deleteCount:
        raise HTTPException(status_code=404, detail=f"主键为{studentId}的学生不存在")

    return {
        "message": f"删除 id={studentId} 的学生"
    }


@student_api.get("/html/index.html")
async def getStudentHtml(request: Request):
    base_dir = os.path.dirname(__file__)
    templates = Jinja2Templates(directory=os.path.join(base_dir, "../", "templates"))

    students = await Student.all()

    return templates.TemplateResponse(
        # 第一个参数必须是 request 对象
        request, 

        # 模板文件
        "index.html",

        # context 上下文对象，一个字典
        {
            "students": students
        }
    )
