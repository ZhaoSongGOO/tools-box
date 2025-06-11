#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2024 The DSM Authors, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

from plugin_cli.args_parser.args_parser import ArgsParser
from plugin_cli.args_parser.cli_description import CLIDescription
from plugin_cli.plugin.plugin_manager import PluginManager
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
        plugin_manager.dispatch_args(args)
    else:
        args_parser.print_help()


if __name__ == "__main__":
    main()
