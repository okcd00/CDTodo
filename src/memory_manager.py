# coding: utf-8
# ==========================================================================
#   Copyright (C) since 2023 All rights reserved.
#
#   filename : memory_manager.py
#   author   : chendian / okcd00@qq.com
#   date     : 2023-04-25
#   desc     : record and restore todo from local files
#              for registering and easy-modification
# ==========================================================================
# basic packages
from queue import PriorityQueue
from collections import OrderedDict

# custom packages
from todo_definition import Todo
from src.file_io import *


class MemoryManager(object):
    MEMORY_FORM = 'pkl file'
    MEMORY_FILE = 'compress json'
    MEMORY_PATH = 'memory/todo_memory'

    def __init__(self):
        # list indexing for all memories
        self.data_list = None
        self.tag_mapping = {}  # tag: [index1, index2]
        self.time_mapping = {}  # time: index
        self.load_memory()

    def load_memory(self):
        # load with memory file selection
        if 'pkl' in self.MEMORY_FORM.split():
            self.data_list = load_pkl(self.MEMORY_PATH + '.pkl')
        elif 'kari' in self.MEMORY_FORM.split():
            dic = load_kari(self.MEMORY_PATH + '.kari')
            self.data_list = OrderedDict(dic)
        else:
            ls = load_vocab(self.MEMORY_PATH + '.txt')
            self.data_list = ls

    def dump_memory(self):
        # call it with the 'save' button (or maybe auto-save?)
        if 'pkl' in self.MEMORY_FORM.split():
            save_pkl(self.data_list, self.MEMORY_PATH + '.pkl')

    def insert_new_todo(self):
        pass

    def remove_todo(self):
        pass


if __name__ == "__main__":
    mm = MemoryManager()
    mm.dump_memory()
