from collections import OrderedDict, defaultdict
from file_io import *


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
    if self.data_list is None:
        print("Fresh new start! (I can not find my memory file.)")
        self.data_list = []
    for index, item in enumerate(self.data_list):
        self.tag_mapping[item.tag or 'notag'].append(index)
        self.time_mapping[item.end_time or -1].append(index)
    self.log(f"Memory Loaded, {len(self.data_list)} todos are collected.")


def dump_memory(self):
    # call it with the 'save' button (or maybe auto-save?)
    if 'pkl' in self.MEMORY_FORM.split():
        save_pkl(self.data_list, self.MEMORY_PATH + '.pkl')
    elif 'kari' in self.MEMORY_FORM.split():
        dic = save_kari(self.MEMORY_PATH + '.kari')
        self.data_list = OrderedDict(dic)
    else:
        ls = dump_vocab(self.MEMORY_PATH + '.txt')
        self.data_list = ls
    self.log(f"Memory Saved, {len(self.data_list)} todos are collected.")