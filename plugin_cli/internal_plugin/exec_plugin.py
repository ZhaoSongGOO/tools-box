# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

from plugin_cli.base.error_code import ErrCode
from plugin_cli.base.log import Log
from plugin_cli.base.result import Err
from plugin_cli.plugin.plugin import Plugin
from plugin_cli.plugin.plugin_manager import PluginManager
from plugin_cli.plugin.plugin_auto_register import AutoRegister
from plugin_cli.loader.plugin_loader import plugin_loader


import os
import argparse


@AutoRegister(name="exec")
class ExecPlugin(Plugin):
    def __init__(self):
        super().__init__()

    # 当用户调用此插件时执行的方法
    def accept(self, args):
        plugin_name = args.name
        plugin_version = args.version
        plugin_workspace = args.path
        plugin_args = args.args
        # 加载测试插件
        module_path = os.path.join(plugin_workspace, plugin_version)
        plugin_loader(module_path)
        # 获取测试插件实例
        plugin_instance = PluginManager.get_plugin(plugin_name)
        if plugin_instance is None:
            return Err(
                ErrCode.SYSTEM_PLUGIN_NOT_FOUND,
                f"Plugin ({plugin_name}) not found!",
            )
        # 构造测试插件命令行解析器
        parser = argparse.ArgumentParser(
            plugin_name, description=plugin_instance.help()
        )
        plugin_instance.build_command_args(parser)
        Log.info(f"Message from plugin {plugin_name}")
        args = parser.parse_args(plugin_args)
        return plugin_instance.accept(args)

    # 返回插件的帮助信息
    def help(self):
        return "This is an exec plugin."

    # 构建插件特有的命令行参数
    def build_command_args(self, subparser):
        subparser.add_argument("path", type=str, help="Plugin workspace path")
        subparser.add_argument("name", type=str, help="Plugin name")
        subparser.add_argument("version", type=str, help="Plugin version")
        subparser.add_argument(
            "--args", nargs=argparse.REMAINDER, type=str, help="Target plugin args"
        )
