#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import Iterable

path = []


def flatten(items, ignore_types=(str, bytes)):
    global path
    # print(path)
    for x in items:
        # 如果序列是字典类型
        if isinstance(items, dict):
            # 把key的名称加入路径
            path.append(x)
            # 把key的值赋给x
            x = items[x]
        # 如果序列是列表类型
        elif isinstance(items, list):
            # 把索引值加入路径
            path.append(str(items.index(x)))

        # 如果元素值为空
        if not x:
            # 删除当前路径
            path.pop()
            # 跳出当前循环，直接进入下个循环
            continue

        # 如果元素是一个序列，且不是str,bytes类型
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
            path.pop()
        else:
            yield {'.'.join(path): x}
            path.pop()
