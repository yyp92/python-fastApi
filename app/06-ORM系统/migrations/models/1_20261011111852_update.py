from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` ADD `addr` VARCHAR(32) NOT NULL COMMENT '教室' DEFAULT '';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` DROP COLUMN `addr`;"""


MODELS_STATE = (
    "eJztmV1vmzAUhv9KxNUmdRP5TneXZq3WdW2lJpomrRMy4BAUYqfGrI26/PfZBmJDIIOmS0"
    "mUm3ycc2zsx+acF/OszbANPf/jwAO+9qn2rCEwg+xHwn5S08B8Lq3cQIHpiUArjjB9SoBF"
    "mW0MPB8ykw19i7hz6mLErCjwPG7EFgt0kSNNAXIfAmhQ7EA6gYQ5fv5iZhfZ8An68d/51B"
    "i70LMTw3Rtfm1hN+hiLmyXiF6IQH4107CwF8yQDJ4v6ASjVbSLKLc6EEECKOTdUxLw4fPR"
    "RbOMZxSOVIaEQ1Ta2HAMAo8q0zUNadMM4+Z2ZAzPR4ahlQBkYcThsqGGi+TwIXxo1FvdVq"
    "/ZafVYiBjmytJdhpeWYMKGAs/NSFsKP6AgjBCMJVTxvYZ1MAEkm2scnyLLhpwmG3PchDY2"
    "SLZyP70crnYfdJvQZp8QdO+Ddkvnv0/HulYM+Qw8GR5EDp2wv83GBr7f+3eDL/27d83Ge9"
    "43ZjdFeKfcRJ6GcC2XfFOPp8oKcIMJrOkjILaR8Mi18WlgQz6otfU5i1peXN1BD4hpr69J"
    "dFsPw16qszyF9/4y3nyxNbr3BE3cwHk4112zxixtAQg4Ykr82vxKcRbEAfFhZn4MPZszpI"
    "w55shjjqx0juyZY8jyItDNauTIE2UfA9smZZDH8btDrmmlgXfa7VOG2gStakCmEFgsvxil"
    "kkay0b+TR2W2eEQf6r2C9F8hq6yV/TX46+QvMIGug67gQizAJRsUQFZWQonq0kj2dBDg88"
    "o+MxPwuCp6qZ3IuDAakIaJoj8c9D+fa8t8mbWlhiii0q4BWoww/yy4kltItTctwBtWTMzM"
    "SCkpZZ6E61doryJCARXCxEQsxRQuFM7Rcq8WKvKG7SInnRAcOBO1lRRmmRuF2Y205Flu1I"
    "nxHDKEojK9fKXoK0FHqXiUipWWiu1TuxmKxGool/ljxubNpxyFVx2yaXVYzezp9WpA9hEu"
    "kSGi6IoLwrbZYYzbzXF3dyJQZcpPUMvpbaVFldnuNANvkNXxEfWWmjo+C98zuEWls7Kp3k"
    "w3q0pvO9ksD+YOWjXLaaZFc+IRJKmaE7o4LZqTknp71Sz4bpbN8cNqhmxWnmPzZbPy2HyU"
    "zXuVtI+y+c0V3VE27+JUtZRspnshm3u6Xg+P8BjpcX3nEvpFr09zBUaZt6cv1xZ7dbb6X1"
    "+p9iFxrUlWyY88Gys+kDHHgn8oBf83JH503xWtRkqTKlek4ogTdajRbhcoRCwqtxIJX+ot"
    "KrupShCOwg+Qbl3XC9BlUbl0hS91loMRjU7wk4S/Dm9vcg5zZJMUZdu1aO1PzXP9ClX+so"
    "+yWXA5DN7zzPcfPJXpu+v+jzTuwbfbMwEH+9QhohfRwVk5DfD6xWz5F0ZLKx8="
)
