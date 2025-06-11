#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plugin_cli.args_parser.args_parser import ArgsParser
from plugin_cli.args_parser.cli_description import CLIDescription
from plugin_cli.plugin.plugin_manager import PluginManager

from base.log import Log
from plugin.json_parser_plugin import JSONParserPlugin


def version():
    return "1.0"


def main():
    plugin_manager = PluginManager()
    plugin_manager.register_plugin(JSONParserPlugin())
    description = CLIDescription("TOOLS-BOX", "Tools box.", version)
    args_parser = ArgsParser(description)
    args_parser.init_subparsers(plugin_manager.plugins)
    args = args_parser.parse_args()

    if args.plugin is not None:
        result = plugin_manager.dispatch_args(args)
        if result.is_ok():
            Log.success("run success")
        else:
            Log.error(result.get_msg())
            exit(result.get_code())
    else:
        args_parser.print_help()


if __name__ == "__main__":
    main()
