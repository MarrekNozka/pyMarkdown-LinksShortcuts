#!/usr/bin/python
# -*- coding: utf8 -*-


import markdown

text = """
<a href="http://google.cz/search?q=jejda&hl=cz">ahoj</a>

QQQ [[!gg ahoj]](jejda) AAAA

WWW [[!gi obrazky]](robot) AAAA

[[!gg ahoj jojo]](jejda) [[!gg ahoj]]()
[[!dd ahoj
jojo]](jejda) [[!gg ahoj]]()
"""

print text
print markdown.markdown(text, extensions=[ 'linksShortcuts:Shortcuts' ])
