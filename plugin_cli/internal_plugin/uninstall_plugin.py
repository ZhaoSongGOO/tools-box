# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

from plugin_cli.base.result import Err, Ok
from plugin_cli.plugin.plugin import Plugin, PluginInfo
from plugin_cli.plugin.plugin_manager import PluginManager
from plugin_cli.plugin.plugin_auto_register import AutoRegister
from plugin_cli.env.env import ToolsBoxEnv

import os
import shutil


@AutoRegister(name="uninstall")
class UnInstallPlugin(Plugin):
    def __init__(self):
        super().__init__()

    # 当用户调用此插件时执行的方法
    def accept(self, args):
        plugin_name = args.name
        info = PluginManager.get_plugin_info(plugin_name)
        if info is None:
            return Ok()
        plugin_path = info.path
        if os.path.exists(plugin_path):
            shutil.rmtree(plugin_path)
        return Ok()

    # 返回插件的帮助信息
    def help(self):
        return "This is a uninstall plugin."

    # 构建插件特有的命令行参数
    def build_command_args(self, subparser):
        subparser.add_argument("name", type=str, help="Plugin name")
