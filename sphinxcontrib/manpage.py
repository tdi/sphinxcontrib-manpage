#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2013 Dariusz Dwornikowski.  All rights reserved.
#
"""
  Providing links to manpages with :linuxman: directiv
"""

from docutils import nodes, utils
from docutils.parsers.rst.roles import set_classes
import re

def make_link_node(rawtext, app, name, manpage_num, options):
    """Create a link to a man page.
    """
    ref = "http://linux.die.net/man/%s/%s" % (manpage_num, name)
    set_classes(options)
    node = nodes.reference(rawtext, "%s(%s)" % (name, manpage_num), refuri=ref,
                           **options)
    return node
    

def man_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Link to a online man page issue.
    """
    app = inliner.document.settings.env.app
    p = re.compile("(\w+)\((\d)\)")
    m = p.match(text)

    manpage_num = m.group(2)
    name = m.group(1)
    node = make_link_node(rawtext, app, name, manpage_num, options)
    return [node], []

def setup(app):
    app.info('Initializing manpage plugin')
    app.add_role('linuxman', man_role)
    return

