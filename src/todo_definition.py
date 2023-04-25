# coding: utf-8
# ==========================================================================
#   Copyright (C) since 2023 All rights reserved.
#
#   filename : todo_definition.py
#   author   : chendian / okcd00@qq.com
#   date     : 2023-04-25
#   desc     : the basic structure for a todo item
#              with neccessary info
# ==========================================================================
import time


class Todo():
    def __init__(self, title, endtime=None):
        self.title = title
        self.description = []
        self.start_time = int(time.time())  # int
        self.end_time = self.analysis_endtime(endtime)

    def analysis_endtime(et):
        return -1
    

if __name__ == "__main__":
    pass
