#!/usr/bin/env python3.5

import os

if __name__ == "__main__":
    if not os.path_exists("newdir"):
        os.makedirs("newdir")
