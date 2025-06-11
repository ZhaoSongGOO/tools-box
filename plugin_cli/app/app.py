# Copyright 2025 The zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

from plugin_cli.args_parser.args_parser import ArgsParser
from plugin_cli.args_parser.args_parser import CLIDescription
from plugin_cli.base.result import Result
from plugin_cli.plugin.plugin_manager import PluginManager
from plugin_cli.base.log import Log


class App:
    def __init__(self, name, description):
        Log.TAG = name

        def version_callback():
            return self.version()

        self.args_parser = ArgsParser(
            CLIDescription(name, description, version_callback)
        )
        self.args_parser.init_subparsers()
        self.active_plugin = None

    def run(self):
        args = self.args_parser.parse_args()
        if args.plugin is not None:
            self.active_plugin = args.plugin
            result = PluginManager.dispatch_args(args)
            self.on_result(result)
        else:
            self.args_parser.print_help()

    def on_result(self, result: Result):
        pass

    def version(self):
        pass
