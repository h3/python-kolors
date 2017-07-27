python-kolors
=============

Simple and lightweight shell color output function.

It also checks if terminal supports color before vomitting ANSI codes.

Usage
-----

.. code:: python

    from kolors import c

    print c('Some <red>Red</end> and <blue>blue</end> text')
    print c('<green bg>Some green background</end>')
    print c('Some <cyan bold bg>{}</end>').format('interpolation')

**Note**: the keyword in the closing tag isn't really relevant, but I
like to use "" everywhere for shortness and consistency. Simple shell
color output function.

Colors
------

-  grey (alias: gray)
-  red
-  green
-  yellow
-  blue
-  magenta (alias: purple)
-  cyan
-  white

Styles
======

-  bold
-  bg
