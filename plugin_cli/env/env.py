# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

import os


class ToolsBoxConfig:
    def __init__(self, config_file):
        if not os.path.exists(config_file):
            with open(config_file, "w") as f:
                f.write(
                    f"tools-box-package.git;https://github.com/ZhaoSongGOO/tools-box-package.git;f5e1d2f484375a3ccb9b278f69b99ed0e362d79e"
                )
        self.sources = {}
        with open(config_file, "r") as f:
            content = f.readlines()
            for c in content:
                info = c.strip().split(";")
                self.sources[info[0]] = {"src": info[1], "hash": info[2]}


class ToolsBoxEnv:
    HOME_PATH = os.path.expanduser("~/.tools-box/")
    PLUGINS_PATH = os.path.join(HOME_PATH, "plugins")
    CACHE_PATH = os.path.join(HOME_PATH, "cache")
    CONFIG_PATH = os.path.join(HOME_PATH, "config")

    def __init__(self):
        self.config = ToolsBoxConfig(ToolsBoxEnv.CONFIG_PATH)


env = ToolsBoxEnv()
