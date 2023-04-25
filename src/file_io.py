# coding: utf-8
# ==========================================================================
#   Copyright (C) since 2023 All rights reserved.
#
#   filename : file_io.py
#   author   : chendian / okcd00@qq.com
#   date     : 2021-01-21
#   desc     : univeral file resolving script.
# ==========================================================================

import os
import sys
import json
import time
import pickle
from typing import (
    IO, Any, Callable, Dict, List, 
    Optional, Union)


def get_cache_dir(cache_dir: Optional[str] = None) -> str:
    """
    Returns a default directory to cache static files
    (usually downloaded from Internet), if None is provided.
    Args:
        cache_dir (None or str): if not None, will be returned as is.
            If None, returns the default cache directory as:
        1) $DLCORE_CACHE, if set
        2) otherwise ~/.torch/dlcore_cache
    """
    if cache_dir is None:
        cache_dir = os.path.expanduser(
            os.getenv("DLCORE_CACHE", "~/.torch/dlcore_cache")
        )
    return cache_dir


def load_json(fp, show_time=False):
    if not os.path.exists(fp):
        print(f"Failed loading {fp} for file-not-existed.")
        return dict()

    with open(fp, 'r', encoding='utf8') as f:
        if show_time:
            start_time = time.time()
            print(f"Loading {fp.split('/')[-1]} ({get_filesize(fp)}MB)", end=' ')
            sys.stdout.flush()
        ret = json.load(f)
        if show_time:
            print(f"cost {round(time.time() - start_time, 3)} seconds.")
        return ret


def dump_json(obj, fp, debug=False, compress=True):
    try:
        fp = os.path.abspath(fp)
        if not os.path.exists(os.path.dirname(fp)):
            os.makedirs(os.path.dirname(fp))
        with open(fp, 'w', encoding='utf8') as f:
            if compress:
                json.dump(obj, f, ensure_ascii=False, 
                          separators=(',', ':'))
            else:
                json.dump(obj, f, ensure_ascii=False, 
                        indent=4, separators=(', ', ': '))
        if debug:
            print(f'json文件保存成功，{fp}')
        return True
    except Exception as e:
        if debug:
            print(f'json文件{obj}保存失败, {e}')
        return False


def load_vocab(fp, show_time=False):
    if not os.path.exists(fp):
        print(f"Failed loading {fp} for file-not-existed.")
        return []
    
    if show_time:
        start_time = time.time()
        print(f"Loading {fp.split('/')[-1]} ({get_filesize(fp)}MB)", end=' ')
        sys.stdout.flush()
    ret = [line.strip() for line in open(fp, 'r')]
    if show_time:
        print(f"cost {round(time.time() - start_time, 3)} seconds.")
    return ret


def save_kari(obj, fp, show_time=False):
    # save key-array-items
    if show_time:
        start_time = time.time()
    if not os.path.exists(os.path.dirname(fp)):
        os.makedirs(os.path.dirname(fp))
    with open(fp, 'w') as f:
        for k, v in sorted(obj.keys()):
            f.write(f"{k}\t{' '.join(v)}\n")
    if show_time:
        print(f"cost {round(time.time() - start_time, 3)} seconds.")
        print(f"Saved {fp.split('/')[-1]} ({get_filesize(fp)}MB)", end=' ')


def load_kari(fp, show_time=False):
    # load key-array-items
    if show_time:
        start_time = time.time()
        print(f"Loading {fp.split('/')[-1]} ({get_filesize(fp)}MB)", end=' ')
        sys.stdout.flush()
    if not os.path.exists(fp):
        print("Failed for file-not-existed.")
        return None
    ret = {line.strip().split('\t')[0]: line.strip().split('\t')[1].split(' ') 
           for line in open(fp, 'r')}
    if show_time:
        print(f"cost {round(time.time() - start_time, 3)} seconds.")
    return ret


def save_pkl(obj, fp, show_time=False):
    if show_time:
        start_time = time.time()
    if not os.path.exists(os.path.dirname(fp)):
        os.makedirs(os.path.dirname(fp))
    pickle.dump(obj, open(fp, 'wb'))
    if show_time:
        print(f"cost {round(time.time() - start_time, 3)} seconds.")
        print(f"Saved {fp.split('/')[-1]} ({get_filesize(fp)}MB)", end=' ')


def load_pkl(fp, show_time=False):
    if show_time:
        start_time = time.time()
        print(f"Loading {fp.split('/')[-1]} ({get_filesize(fp)}MB)", end=' ')
        sys.stdout.flush()
    if not os.path.exists(fp):
        print("Failed for file-not-existed.")
        return None
    ret = pickle.load(open(fp, 'rb'))
    if show_time:
        print(f"cost {round(time.time() - start_time, 3)} seconds.")
    return ret


def get_main_dir():
    # 如果是使用pyinstaller打包后的执行文件，则定位到执行文件所在目录
    if hasattr(sys, 'frozen'):
        return os.path.join(os.path.dirname(sys.executable))
    # 其他情况则定位至项目根目录
    return os.path.join(os.path.dirname(__file__), '..', '..')


def get_abs_path(*name):
    fn = os.path.join(*name)
    if os.path.isabs(fn):
        return fn
    return os.path.abspath(os.path.join(get_main_dir(), fn))


def timestamp2time(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_file_modified_time(fp):
    # '''获取文件的修改时间'''
    # fp = unicode(filePath, 'utf8')
    t = os.path.getmtime(fp)
    return timestamp2time(t)


def get_filesize(fp):
    # '''获取文件的大小,结果保留两位小数，单位为MB'''
    # fp = unicode(fp,'utf8')
    fsize = os.path.getsize(fp)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)


def flatten(nested_list, unique=False):
    ret = [elem for sub_list in nested_list for elem in sub_list]
    if unique:
        return list(set(ret))
    return ret


if __name__ == "__main__":
    print(get_main_dir())
