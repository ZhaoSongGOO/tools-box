# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

# ==============================================
# plugin_cli 库使用说明
# ==============================================
# 本示例展示如何使用 plugin_cli 库创建一个支持插件化的命令行工具

# 1. 首先导入必要的模块
from plugin_cli.args_parser.args_parser import ArgsParser
from plugin_cli.args_parser.args_parser import CLIDescription
from plugin_cli.plugin.plugin import Plugin
from plugin_cli.plugin.plugin_manager import PluginManager
from plugin_cli.base.log import Log
from plugin_cli.base.result import Ok, Err
from plugin_cli.plugin.plugin_auto_register import AutoRegister


# 2. 创建自定义插件
# 使用 @AutoRegister 装饰器自动注册插件
# name 参数指定插件名称（可选）: 如果不指定name，将会使用类名作为插件名称
@AutoRegister(name="Custom-Plugin")
class CustomPlugin(Plugin):
    def __init__(self):
        super().__init__()

    # 当用户调用此插件时执行的方法
    def accept(self, args):
        print(args)
        # 运行成功，返回 Ok
        # return Ok()
        # 运行失败，返回Err
        return Err(1, "run failed")

    # 返回插件的帮助信息
    def help(self):
        return "This is a demo plugin."

    # 构建插件特有的命令行参数
    def build_command_args(self, subparser):
        subparser.add_argument("subcommand", type=str, help="This is a subparser")


# 3. 定义版本回调函数
def version_callback():
    """返回CLI工具的版本信息"""
    return "0.0.1"


def main():
    # 4.1 初始化日志系统
    Log.TAG = "Example"  # 设置日志标签
    Log.info("Welcome use Plugin-CLI")
    # 4.2 创建CLI描述对象
    # 参数说明:
    # - 第一个参数: 程序名称
    # - 第二个参数: 程序描述
    # - version_callback: 版本信息回调函数
    description = CLIDescription("demo-cli", "This is a demo cli!", version_callback)

    # 4.3 初始化参数解析器
    args_parser = ArgsParser(description)
    args_parser.init_subparsers()

    # 4.4 解析命令行参数
    args = args_parser.parse_args()

    # 4.5 处理插件命令或显示帮助信息
    if args.plugin is not None:
        # 如果指定了插件，则分发参数给对应插件处理
        result = PluginManager.dispatch_args(args)
        if result is None:
            Log.warning(f"Plugin ({args.plugin}) should return an result, not None")
        else:
            if result.is_ok():
                Log.success(f"Plugin ({args.plugin}) run success")
            else:
                Log.error(
                    f"Plugin ({args.plugin}) run failed! with code {result.get_code()} : {result.get_msg()}"
                )
    else:
        # 否则显示帮助信息
        args_parser.print_help()


if __name__ == "__main__":
    main()
