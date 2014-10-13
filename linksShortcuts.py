#!/usr/bin/python
# -*- coding: utf8 -*-
"""
# Date:    12.10.2014 00:06
# Author:  Marek Nožka, marek <@t> tlapicka <d.t> net
# Licence: GNU/GPL

"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import generators

import markdown

__version__ = "0.2"


class LinksShortcuts(markdown.inlinepatterns.Pattern):
    url = {
        'gg': 'http://www.google.com/search?q={0}',
        'gi': 'http://google.com/search?q={0}&tbm=isch',
        'dd': 'http://duckduckgo.com/?q={0}',
        'enwk': 'http://en.wikipedia.com/wiki/{0}',
        'cswk': 'http://cs.wikipedia.com/wiki/{0}',
        'ipynb': 'http://nbviewer.ipython.org/urls/raw.github.com/tlapicka/'
                 'IPythonNotebooks/master/{0}.ipynb',
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
            el.attrib['href'] = self.url[m.group(2)].format(m.group(3))
        return el


class Shortcuts(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.add('googleshortcut', LinksShortcuts(), '_begin')


def makeExtension(configs=None):
    return Shortcuts(configs=configs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
