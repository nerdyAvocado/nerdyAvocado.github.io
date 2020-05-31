#!/usr/bin/env python3

import os
import sys
import re

current_dir = os.getcwd()
tags_dir = os.path.join(current_dir, 'blog/tags')
posts_dir = os.path.join(current_dir, '_posts')
tags_pattern = r"tags: ([\w\-]+(?: +[\w\-]+)*)"
tag_file_template = """---
layout: tagpage
tag: %s
title: Amy Boslam's Blog
permalink: /blog/tags/%s/
---
"""

tags = []

try:
    for root, dirs, files in os.walk(posts_dir, topdown=True):
        for filename in files:
            with open(os.path.join(root,filename), 'r') as f:
                data = f.read()
                for m in re.finditer(tags_pattern, data):
                    tags.extend(m[1].split(' '))
except FileNotFoundError:
    print("Could not find posts directory.")

unique_tags = set(tags)
tags_list = list(unique_tags)
print(tags_list)

rc = 0

try:
    for tag in tags_list:
        tag_filename = os.path.join(tags_dir, "%s.md" % tag.lower())
        if not os.path.isfile(tag_filename):
            rc = 1
            print(tag_filename)
            with open(tag_filename, 'w') as f:
                f.write(tag_file_template % (tag,tag.lower()))
except FileNotFoundError:
    print("Could not find tags directory.")

sys.exit(rc)