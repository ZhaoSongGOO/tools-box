# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

# ==============================================
# plugin_cli 库使用说明
# ==============================================
# 本示例展示如何使用 plugin_cli 库创建一个支持插件化的命令行工具

# 1. 首先导入必要的模块
import os
from plugin_cli.app.app import App
from plugin_cli.base.log import Log
from plugin_cli.loader.plugin_loader import installed_plugins_loader
from plugin_cli.internal_plugin import *


installed_plugins_loader()


# 3. 定义版本回调函数
def version_callback():
    """返回CLI工具的版本信息"""
    return "0.0.1"


class ToolsBox(App):
    def __init__(self):
        super().__init__("tools-box", "tools-box, manager your python tools!")

    def version(self):
        return version_callback()

    def on_result(self, result):
        if result is None:
            Log.warning(
                f"Plugin ({self.active_plugin}) should return an result, not None"
            )
        else:
            if result.is_ok():
                Log.success(f"Plugin ({self.active_plugin}) run success")
                exit(0)
            else:
                Log.error(
                    f"Plugin ({self.active_plugin}) run failed! with code {result.get_code()} : {result.get_msg()}"
                )
                exit(result.get_code())


def main():
    ToolsBox().run()


if __name__ == "__main__":
    main()
