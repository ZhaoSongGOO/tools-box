#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

import os
from typing import Type, TypeVar
from plugin_cli.plugin.plugin import Plugin, PluginInfo
from plugin_cli.plugin.plugin_manager import PluginManager
from plugin_cli.env.env import ToolsBoxEnv

T = TypeVar("T", bound="Plugin")


def AutoRegister(name: str = None):
    def decorator(cls: Type[T]) -> Type[T]:
        if not issubclass(cls, Plugin):
            raise TypeError(f"{cls.__name__} is not herient from Plugin!")
        plugin_name = name if name is not None else cls.__name__
        module_path = cls.__module__.split(".")[0]
        plugin_path = os.path.join(ToolsBoxEnv.PLUGINS_PATH, module_path)
        info = PluginInfo(plugin_name, plugin_path, False)
        if module_path == "plugin_cli":
            info.internal = True
        PluginManager.register_plugin(info, cls)

    return decorator
