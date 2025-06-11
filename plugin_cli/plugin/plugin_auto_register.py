#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

from typing import Type, TypeVar
from plugin_cli.plugin.plugin import Plugin
from plugin_cli.plugin.plugin_manager import PluginManager

T = TypeVar("T", bound="Plugin")


def AutoRegister(name: str = None):
    def decorator(cls: Type[T]) -> Type[T]:
        if not issubclass(cls, Plugin):
            raise TypeError(f"{cls.__name__} is not herient from Plugin!")
        print(cls.__name__)
        plugin_name = name if name is not None else cls.__name__
        PluginManager.register_plugin(plugin_name, cls)

    return decorator
