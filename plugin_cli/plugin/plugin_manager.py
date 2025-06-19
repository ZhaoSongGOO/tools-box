#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

from typing import Type
from plugin_cli.base.result import Result
from plugin_cli.plugin.plugin import Plugin, PluginInfo


class PluginManager:
    plugins_class = {}
    plugins_instances = {}

    @staticmethod
    def register_plugin(info: PluginInfo, plugin: Type[Plugin]):
        name = info.name
        PluginManager.plugins_class[name] = plugin
        plugin_instance = plugin()
        plugin_instance.name = name
        PluginManager.plugins_instances[name] = {
            "info": info,
            "instance": plugin_instance,
        }

    @staticmethod
    def dispatch_args(args) -> Result:
        plugin = PluginManager.plugins_instances[args.plugin]["instance"]
        return plugin.accept(args)

    @staticmethod
    def get_plugin_info(plugin_name) -> PluginInfo:
        if plugin_name in PluginManager.plugins_instances.keys():
            return PluginManager.plugins_instances[plugin_name]["info"]
        else:
            return None
