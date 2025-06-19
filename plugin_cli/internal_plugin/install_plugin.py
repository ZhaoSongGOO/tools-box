# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

import os
import yaml
import shutil

from plugin_cli.base.result import Err, Ok
from plugin_cli.plugin.plugin import Plugin
from plugin_cli.plugin.plugin_auto_register import AutoRegister

PACKAGE_SOURCE = {
    "tools-box-package": "https://github.com/ZhaoSongGOO/tools-box-package.git"
}
PACKAGE_STORE = os.path.expanduser("~/.tools-box/cache")

PLUGIN_PATH = os.path.expanduser("~/.tools-box/plugins")


@AutoRegister(name="install")
class InstallPlugin(Plugin):
    def __init__(self):
        super().__init__()

    # 当用户调用此插件时执行的方法
    def accept(self, args):
        plugin_name = args.name
        for source in PACKAGE_SOURCE.keys():
            index_path = os.path.join(PACKAGE_STORE, source, "index.yml")
            if not os.path.exists(index_path):
                continue
            with open(index_path, "r") as file:
                data = yaml.safe_load(file)
                packages = data["packages"]
                for package in packages:
                    print(package["name"], plugin_name)
                    if package["name"] == plugin_name:
                        plugin_file = os.path.join(
                            PACKAGE_STORE,
                            source,
                            plugin_name,
                            "0.1",
                            f"{plugin_name}.py",
                        )
                        target_file = os.path.join(PLUGIN_PATH, f"{plugin_name}.py")
                        shutil.copyfile(plugin_file, target_file)
                        return Ok()

        return Err(3, f"Plugin ({plugin_name}) not found")

    # 返回插件的帮助信息
    def help(self):
        return "This is a install plugin."

    # 构建插件特有的命令行参数
    def build_command_args(self, subparser):
        subparser.add_argument("name", type=str, help="This is a subparser")
