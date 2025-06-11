#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plugin_cli.plugin.plugin import Plugin


class JSONParserPlugin(Plugin):
    def __init__(self):
        super().__init__("json-parser")

    def accept(self, args):
        print(args)

    def help(self):
        return "reduce json"

    def build_command_args(self, subparser):
        subparser.add_argument("path", type=str, help="Directory need to be inited")
