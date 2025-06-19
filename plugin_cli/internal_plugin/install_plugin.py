# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

import os
import yaml
import shutil

from plugin_cli.base.log import Log
from plugin_cli.base.result import Err, Ok
from plugin_cli.plugin.plugin import Plugin
from plugin_cli.plugin.plugin_auto_register import AutoRegister
from plugin_cli.env.env import ToolsBoxEnv, env


def version_key(v):
    return tuple(map(int, v.split(".")))


@AutoRegister(name="install")
class InstallPlugin(Plugin):
    def __init__(self):
        super().__init__()

    # 当用户调用此插件时执行的方法
    def accept(self, args):
        plugin_name = args.name
        version = args.version
        for source in env.config.sources.keys():
            index_path = os.path.join(ToolsBoxEnv.CACHE_PATH, source, "index.yml")
            if not os.path.exists(index_path):
                continue
            with open(index_path, "r") as file:
                data = yaml.safe_load(file)
                packages = data["packages"]
                for package in packages:
                    if package["name"] == plugin_name:
                        versions = package["versions"]
                        if version != "latest" and version not in versions:
                            return Err(
                                4,
                                f"Not found target version ({version}) for {plugin_name}",
                            )
                        best_version = (
                            version
                            if version in versions
                            else max(versions, key=version_key)
                        )
                        plugin_package = os.path.join(
                            ToolsBoxEnv.CACHE_PATH,
                            source,
                            plugin_name,
                            best_version,
                            plugin_name,
                        )
                        target_path = os.path.join(
                            ToolsBoxEnv.PLUGINS_PATH, plugin_name
                        )
                        if os.path.exists(target_path):
                            shutil.rmtree(target_path)
                        shutil.copytree(plugin_package, target_path)
                        return Ok()

        return Err(3, f"Plugin ({plugin_name}) not found")

    # 返回插件的帮助信息
    def help(self):
        return "This is a install plugin."

    # 构建插件特有的命令行参数
    def build_command_args(self, subparser):
        subparser.add_argument("name", type=str, help="plugin name")
        subparser.add_argument(
            "--version", type=str, default="latest", help="plugin version"
        )
