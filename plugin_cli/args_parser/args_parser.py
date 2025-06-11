# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

import argparse

from plugin_cli.args_parser.cli_description import CLIDescription
from plugin_cli.plugin.plugin_manager import PluginManager


class ArgsParser:
    def __init__(self, description: CLIDescription):
        self.parser = argparse.ArgumentParser(description=description.description)
        self.subparsers = self.parser.add_subparsers(
            dest="plugin", help="Available plugins"
        )
        self.parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"{description.name} version {description.version()}",
            help=f"print the {description.name} version number and exit (also --version)",
        )

    def init_subparsers(self):
        for name in PluginManager.plugins_instances.keys():
            plugin_instance = PluginManager.plugins_instances[name]
            subparser = self.subparsers.add_parser(name, help=plugin_instance.help())
            plugin_instance.build_command_args(subparser)

    def parse_args(self):
        return self.parser.parse_args()

    def print_help(self):
        self.parser.print_help()
