#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2024 zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree


def is_valid_version(raw_version: str) -> bool:
    version_info = raw_version.split(".")
    if len(version_info) <= 1:
        return False
    for v in version_info:
        try:
            int(v)
        except Exception as e:
            return False
    return True
