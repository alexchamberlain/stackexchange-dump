# stackexchange-dump.py

A simple script to dump the contents of a Stack Exchange question.

## Usage
First, install [Py-StackExchange][1], then it is as simple as

    $ python2 stackexchange-dump.py 11881795 > 11881795.html

## Producing `.epub` files
`.epub` files can be easily generated by using [`pandoc`][2].

    $ pandoc 11881795.html -o 11881795.epub

  [1]: https://github.com/lucjon/Py-StackExchange
  [2]: http://johnmacfarlane.net/pandoc/
