from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clas` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '班级名称'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '姓名',
    `pwd` VARCHAR(32) NOT NULL COMMENT '密码',
    `sno` INT NOT NULL COMMENT '学号',
    `clas_id` INT NOT NULL,
    CONSTRAINT `fk_student_clas_4be9b492` FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '姓名',
    `pwd` VARCHAR(32) NOT NULL COMMENT '密码',
    `tno` INT NOT NULL COMMENT '老师编号'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '课程名称',
    `teacher_id` INT NOT NULL COMMENT '课程教师',
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztmV1vmzAUhv9KxNUmdRP5IEl3l2at1nVtpSaaJq0TMuAQFGKnYNZGXf77bAOxIZBB06"
    "Uk4iYfx8fGfnw458U8K3NsQdf/OHSBr3xqPCsIzCH9kbCfNBSwWAgrMxBguNzRjD0Mn3jA"
    "JNQ2Aa4PqcmCvuk5C+JgRK0ocF1mxCZ1dJAtTAFyHgKoE2xDMoUebfj5i5odZMEn6Md/Fz"
    "N94kDXSkzTsdi1uV0nywW3XSJywR3Z1QzdxG4wR8J5sSRTjNbeDiLMakMEPUAgG554AZs+"
    "m120ynhF4UyFSzhFqY8FJyBwibRcQxc2Rddvbsf66Hys60oJQCZGDC6darhJNpvCh1az0+"
    "v0291On7rwaa4tvVV4aQEm7Mjx3IyVFW8HBIQenLGAyr83sA6nwMvmGvunyNIpp8nGHLeh"
    "jQ2CrYinl8NV7oNeG1r0E4LefaB1VPb7dKIqxZDPwZPuQmSTKf3bbm3h+31wN/wyuHvXbr"
    "1nY2N6U4R3yk3U0uJNqxUL6slM2gFmMIA5ewSepSdaxN74JLAgm9TG/pxFPS+u7qAL+LI3"
    "9yS6rUfhKNXZnsKxv4qDL7ZG9x6niVs4D+dm07w1T1sAAjZfErs2u1KcBXHg+TAzP4Yt2z"
    "Ok8KlzZJ0jK50j+8YE0rwIVKMaOfJEimMCgUlDXy8Vz8lO/47rytDvatop3QOo9gvSf4WA"
    "36hIG/A3yV9gDzo2uoJLvgGXdFIAmVmxHqXMsRjpKMDnVSRq9sDjOh+nIpFyoTQgCdPGYD"
    "QcfD5XVvkKYMfyVkRAXAO0HGP2WXAnd1ARb1obtuwYX5meKvLSOj0mraC19ghrewgTe3wr"
    "ZnApcY62e71RUWvYL2okUw8H9lTuJTRDZqBQu56uxqutEiZeQ4aGkZaXL2J8yalWMbWKqb"
    "SK0U6tdqhfqqFcFo8ZwZtPOXKvOmTD7NKa2Veb1YDsI1wiQ0TeFReEmtGljLX2pLc/ESgz"
    "ZYd75fS21KPKbPeagbfI6vj0dEdNHR/THhjcotJZCqo3082y0ttNNoszo6NWzWKZadGceA"
    "RJquaELk6L5qSk3l01c77bZXP8sJohm6Xn2HzZLD0217L5oJJ2LZvfXNHVsnkfp6qlZDM5"
    "CNncV9VmeIRHSU+ae5fQL3qzlyswyrzYe7m2OKiz1f/6tm8APcecZpX8qGVrxQfCpy74x1"
    "Lwf0PPj+67otVI6lLlilQccaIOtTStQCGiXrmViLclSxG7qUoQjtyPkG5TVQvQpV65dHlb"
    "6iwHIxKd4CcJfx3d3uQc5oguKcqWY5LGn4br+BWq/GUfZbPgMhhs5LnvP7gy03fXgx9p3M"
    "Nvt2ccDvaJ7fFR+ABn5TTA6xez1V+cMLwY"
)
