# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

from plugin_cli.base.error_code import ErrCode
from plugin_cli.base.result import Err, Ok
from plugin_cli.plugin.plugin import Plugin
from plugin_cli.plugin.plugin_auto_register import AutoRegister
from plugin_cli.utils.version import is_valid_version
from plugin_cli.plugin.plugin_template import INIT_TEMPLATE, PLUGIN_TEMPLATE

import os


@AutoRegister(name="create")
class CreatePlugin(Plugin):
    def __init__(self):
        super().__init__()

    # 当用户调用此插件时执行的方法
    def accept(self, args):
        project_name = args.name
        version = args.version
        if not is_valid_version(version):
            return Err(
                ErrCode.SYSTEM_VERSION_ILLEGAL,
                f"version ({version}) is illeagle!",
            )
        if os.path.exists(project_name):
            return Err(
                ErrCode.SYSTEM_OTHER_ERR,
                f"workspace ({project_name}) has existed!",
            )

        workspace = os.path.join(project_name, version, project_name)
        os.makedirs(workspace)
        init_file = os.path.join(workspace, "__init__.py")
        with open(init_file, "w") as f:
            content = INIT_TEMPLATE.replace("{module}", project_name).replace(
                "{plugin}", project_name
            )
            f.write(content)
        plugin_file = os.path.join(workspace, f"{project_name}.py")
        with open(plugin_file, "w") as f:
            best_plugin_name = project_name.strip().replace("_", "-")
            plugin_class_name_values = best_plugin_name.split("-")
            best_plugin_class_name = ""
            for v in plugin_class_name_values:
                lv = v.lower()
                lv = lv[0].upper() + lv[1:]
                best_plugin_class_name += lv
            content = PLUGIN_TEMPLATE.replace(
                "{plugin_name}", best_plugin_name
            ).replace("{plugin_class_name}", best_plugin_class_name)
            f.write(content)
        return Ok()

    # 返回插件的帮助信息
    def help(self):
        return "This is a create plugin."

    # 构建插件特有的命令行参数
    def build_command_args(self, subparser):
        subparser.add_argument("name", type=str, help="Plugin name")
        subparser.add_argument("version", type=str, help="Plugin version")
