sphinxcontrib-manpage
=====================

Sphinx role to render html links to online Linux manpages. 

Usage
-----

`:linuxman:ls(1)` will render a link to http://linux.die.net/man/1/ls. 

Config
------

You can configure custom url with a `linux_man_url_regex` directive in `conf.py`, the syntax is as
follows:

`http://linux.die.net/man/$num/$topic`, where `$num` is the man page number and `$topic` is a
string. 


Licence and credits
-------------------

Copyright (c) Dariusz Dwornikowski and Poznan University of Technology. 
Distributed under the Apache Commons 2.0. 
