#!/usr/bin/python3
# SPDX-FileCopyringhtText: 2022 Takato Tanimoto

import sys

ans = 0
for line in sys.stdin:
    try:
        ans += int(line)
    except:
        ans += float(line)

print(ans)
