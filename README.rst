python-kolors
=============

Simple and lightweight shell color output function.

It also checks if terminal supports color before vomitting ANSI codes.

Usage
-----

.. code-block:: python

    from kolors import c

    print c('Some <red>Red</end> and <blue>blue</end> text')
    print c('<green bg>Some green background</end>')
    print c('Some <cyan bold bg>{}</end>').format('interpolation')


.. note:: The keyword in the closing tag isn't really relevant, but I like to use "</end>" everywhere for shortness and consistency.  Simple shell color output function.


Colors
------

* grey (alias: gray)
* red
* green
* yellow
* blue
* magenta (alias: purple)
* cyan
* white


Styles
------

* bold
* bg


Roadmap
-------

Not sure where this project will go, but suggestions and pull requests are welcome.

The features bellow were suggested, I'm seriously considering them for the next iterations.


Use curses
**********

.. code-block:: python

    import curses

    curses.setupterm()

    if curses.tigetstr('setf') is not None:
        # Red foreground, if supported.
        print (curses.tparm(curses.tigetstr('setf'), curses.COLOR_RED).decode('utf-8'))

From man 5 terminfo:

> To  change  the  current  foreground  or background color on a Tek‐
> tronix-type terminal, use setaf (set  ANSI  foreground)  and  setab
> (set  ANSI background) or setf (set foreground) and setb (set back‐
> ground).  These take one parameter, the  color  number.   The  SVr4
> documentation  describes only setaf/setab; the XPG4 draft says that
> "If the terminal supports ANSI escape sequences to  set  background
> and  foreground,  they  should be coded as setaf and setab, respec‐
> tively.

Note: thanks u/awegge!


Cleaner, nestable syntax
************************

.. code-block:: xml

    <fg red>Red text<b>Red bold text <bg blue>Red bold tect on Blue background</bg>red bold again</b>Just red again </fg>


Wrapping around other libraries
*******************************

Like colorama & click.style
