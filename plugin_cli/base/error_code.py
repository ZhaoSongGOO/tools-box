# Copyright 2025 The zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

from enum import Enum, auto


class AutoEnum(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return count


class ErrCode(AutoEnum):
    _ = auto()
    SYSTEM_PLUGIN_NOT_FOUND = auto()
    SYSTEM_VERSION_ILLEGAL = auto()

    SYSTEM_OTHER_ERR = auto()

    PLUGIN_INTERNAL_OTHER_ERR = auto()
