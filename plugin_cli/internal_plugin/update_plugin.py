# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree
import os
from plugin_cli.base.result import Err, Ok
from plugin_cli.base.log import Log
from plugin_cli.plugin.plugin import Plugin
from plugin_cli.plugin.plugin_auto_register import AutoRegister
import subprocess

PACKAGE_SOURCE = {
    "tools-box-package": "https://github.com/ZhaoSongGOO/tools-box-package.git"
}
PACKAGE_STORE = os.path.expanduser("~/.tools-box/cache")


@AutoRegister(name="update")
class UpdatePlugin(Plugin):
    def __init__(self):
        super().__init__()

    # 当用户调用此插件时执行的方法
    def accept(self, _):
        # clone
        if not os.path.exists(PACKAGE_STORE):
            os.makedirs(PACKAGE_STORE)
        for source in PACKAGE_SOURCE.keys():
            cmd = f"git clone {PACKAGE_SOURCE[source]} {source}"
            try:
                Log.info(f"Fetching source from {PACKAGE_SOURCE[source]}")
                subprocess.check_call(
                    cmd,
                    shell=True,
                    cwd=PACKAGE_STORE,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            except Exception as e:
                Log.warning(f"Fetching source from {PACKAGE_SOURCE[source]} failed!")
        return Ok()

    # 返回插件的帮助信息
    def help(self):
        return "This is a update plugin."

    # 构建插件特有的命令行参数
    def build_command_args(self, subparser):
        pass
