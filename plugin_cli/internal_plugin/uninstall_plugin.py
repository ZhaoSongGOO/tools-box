# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

from plugin_cli.base.result import Err, Ok
from plugin_cli.plugin.plugin import Plugin
from plugin_cli.plugin.plugin_auto_register import AutoRegister


@AutoRegister(name="uninstall")
class UnInstallPlugin(Plugin):
    def __init__(self):
        super().__init__()

    # 当用户调用此插件时执行的方法
    def accept(self, args):
        print(args)
        # 运行失败，返回Err
        # return Err(1, "run failed")
        # 运行成功，返回 Ok
        return Ok()

    # 返回插件的帮助信息
    def help(self):
        return "This is a uninstall plugin."

    # 构建插件特有的命令行参数
    def build_command_args(self, subparser):
        subparser.add_argument("subcommand", type=str, help="This is a subparser")
