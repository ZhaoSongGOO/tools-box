# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree
import os
from plugin_cli.base.result import Err, Ok
from plugin_cli.base.log import Log
from plugin_cli.plugin.plugin import Plugin
from plugin_cli.plugin.plugin_auto_register import AutoRegister
from plugin_cli.env.env import env, ToolsBoxEnv
import subprocess


@AutoRegister(name="update")
class UpdatePlugin(Plugin):
    def __init__(self):
        super().__init__()

    # 当用户调用此插件时执行的方法
    def accept(self, _):
        # clone
        if not os.path.exists(ToolsBoxEnv.CACHE_PATH):
            os.makedirs(ToolsBoxEnv.CACHE_PATH)
        for source in env.config.sources.keys():
            cmd = f"git clone {env.config.sources[source]['src']} {source}"
            try:
                Log.info(f"Fetching source from {env.config.sources[source]}")
                subprocess.check_call(
                    cmd,
                    shell=True,
                    cwd=ToolsBoxEnv.CACHE_PATH,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            except Exception as e:
                Log.warning(
                    f"Fetching source from {env.config.sources[source]} failed!"
                )
        return Ok()

    # 返回插件的帮助信息
    def help(self):
        return "This is a update plugin."

    # 构建插件特有的命令行参数
    def build_command_args(self, subparser):
        pass
