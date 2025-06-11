# Copyright 2025 The zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree
import importlib
import pkgutil
import os
import sys


def plugin_loader(package_path: str):
    init_file = os.path.join(package_path, "plugins", "__init__.py")
    module_path = os.path.join(package_path, "plugins")
    if not os.path.exists(module_path):
        os.makedirs(module_path)
        open(init_file, "w").close()
        return

    if not os.path.exists(init_file):
        raise ImportError(
            f"{module_path} is not a Python package (missing __init__.py)"
        )
    sys.path.append(package_path)
    for _, name, _ in pkgutil.iter_modules([module_path]):
        module_full_name = f"plugins.{name}"
        try:
            importlib.import_module(module_full_name)
        except ImportError as e:
            print(f"Failed to import {module_full_name}: {e}")
