#!/usr/bin/python
# -*- coding: utf8 -*-


import markdown

text = """
<a href="http://google.cz/search?q=jejda&hl=cz">ahoj</a>
QQQ [[!gg ah&oj]](jejda) AAAA

WWW [[!gg ahoj]]() AAAA

[[!gg ahoj jojo]](jejda) [[!gg ahoj]]()
[[!dd ahoj
jojo]](jejda) [[!gg ahoj]]()
"""

print text
print markdown.markdown(text, extensions=[ 'linksShortcuts:Shortcuts' ])
