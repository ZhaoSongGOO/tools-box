# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree


INIT_TEMPLATE = """
# auto generate code
import {module}.{plugin}
"""

PLUGIN_TEMPLATE = """
# -*- coding: utf-8 -*-
from plugin_cli.base.result import Err, Ok
from plugin_cli.plugin.plugin import Plugin
from plugin_cli.plugin.plugin_auto_register import AutoRegister

@AutoRegister(name="{plugin_name}")
class {plugin_class_name}Plugin(Plugin):
    def __init__(self):
        super().__init__()

    def accept(self, args):
        '''
        - Invocation timing
            This method willl be triggered when this plugin is called
            and will be passed the command-line arguments entered by the user.
        - Input
            eg: tools-box your-plugin -name a -version 1.0
                args will be Namespace(plugin='create', name='a', version='1.0'),
                You can use args.name or args.version to get value.
        - Return
            Return value must be of type `Err` or `Ok`.
            eg:
                Err(1, "error message)
                Ok()
        '''
        pass

    def help(self):
        return "your plugin description"

    def build_command_args(self, subparser):
        '''
        The `subparser` is based on the `argparser` library and is used to build
        the user parameter system for the entire CLI. Here, you can construct parameters
        unique to yout own plugin.
        '''
        pass
"""
