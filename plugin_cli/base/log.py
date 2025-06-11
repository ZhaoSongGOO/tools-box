# Copyright 2025 The zhaosonggo@gmail.com, All rights reserved.
# Licensed under the Apache License Version 2.0 that can be found in the
# LICENSE file in the root directory of this source tree

import datetime
import sys


def get_format_time_str():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d %H:%M:%S")
    return formatted_time


class Log:
    green_color_code = "\033[92m"
    red_color_code = "\033[91m"
    yellow_color_code = "\033[93m"
    blue_color_code = "\033[94m"
    reset_color_code = "\033[0m"

    TAG = None

    @staticmethod
    def print(msg):
        print(msg, flush=True)

    @staticmethod
    def get_tag():
        if Log.TAG is None:
            return "CLI"
        return Log.TAG

    @staticmethod
    def info(msg):
        print_msg = f"[{Log.get_tag()}][INFO] {msg}"
        print(
            f"{Log.blue_color_code}[{get_format_time_str()}]{print_msg}{Log.reset_color_code}",
            flush=True,
        )

    @staticmethod
    def success(msg):
        print_msg = f"[{Log.get_tag()}][SUCCESS] {msg}"
        print(
            f"{Log.green_color_code}[{get_format_time_str()}]{print_msg}{Log.reset_color_code}",
            flush=True,
        )

    @staticmethod
    def error(msg):
        print_msg = f"[{Log.get_tag()}][ERROR] {msg}"
        print(
            f"{Log.red_color_code}[{get_format_time_str()}]{print_msg}{Log.reset_color_code}",
            flush=True,
        )

    @staticmethod
    def fatal(msg):
        print_msg = f"[{Log.get_tag()}][FATAL] {msg}"
        print(
            f"{Log.red_color_code}[{get_format_time_str()}]{print_msg}{Log.reset_color_code}",
            flush=True,
        )
        sys.exit(1)

    @staticmethod
    def warning(msg):
        print_msg = f"[{Log.get_tag()}][WARNING] {msg}"
        print(
            f"{Log.yellow_color_code}[{get_format_time_str()}]{print_msg}{Log.reset_color_code}",
            flush=True,
        )
