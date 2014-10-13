#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  shortcut.py
# Datum:   12.10.2014 00:06
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Autor:   Marek Nožka, marek <@t> tlapicka <d.t> net
# Licence: GNU/GPL
# Úloha:
# Popis:
############################################################################
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators

import markdown

__version__ = "0.1"


class LinksShortcuts(markdown.inlinepatterns.Pattern):
    url = {
        'gg': 'http://www.google.com/search?q={0}',
        'gi': '',
        'enwk': '',
        'cswk': '',
        'dd': 'http://duckduckgo.com/?q={}'
    }

    def __init__(self):
        patern = r'\[\[!([^ ]+)\s+([^\]]+)\]\]\(([^\)]*)\)'
        markdown.inlinepatterns.Pattern.__init__(self, patern)

    def handleMatch(self, m):
        el = markdown.util.etree.Element('a')
        el.text = markdown.util.AtomicString( m.group(3) )
        if m.group(4):
            el.attrib['href'] = self.url[m.group(2)].format(m.group(4))
        else:
            el.attrib['href'] = self.url[m.group(2)].format(m.group(4))
        return el


class Shortcuts(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('googleshortcut', LinksShortcuts(), '_begin')


def makeExtension(configs=None):
    return ShortCuts(configs=configs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
