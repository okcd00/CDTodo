# coding: utf-8
# ==========================================================================
#   Copyright (C) since 2023 All rights reserved.
#
#   filename : settings.py
#   author   : chendian / okcd00@qq.com
#   date     : 2023-04-25
#   desc     : Main entrance of the application
#
# ==========================================================================
import os, sys
PROJECT_PATH = os.path.dirname(__file__)

# auto-setup for PYTHONPATH
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)


if __name__ == "__main__":
    pass
