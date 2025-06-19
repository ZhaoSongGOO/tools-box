# Copyright 2025 The zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree
import importlib
import pkgutil
import os
import sys
from plugin_cli.base.log import Log


def plugin_loader(package_path: str):
    module_path = os.path.join(package_path, "plugins")
    if not os.path.exists(module_path):
        os.makedirs(module_path)
        return
    sys.path.append(module_path)
    for _, name, _ in pkgutil.iter_modules([module_path]):
        try:
            importlib.import_module(name)
        except ImportError as e:
            Log.warning(f"Failed to import {name}: {e}")
