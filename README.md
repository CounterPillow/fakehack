# fakehack
Silly l33t script for entertainment purposes.

## Why
Because.

## Dependencies
[click](http://click.pocoo.org/5/), python3

## Usage
    ./fakehack.py [user] [host]

to launch a "fake shell" of *user@host*, then you may type:

    h4xx0rz [target]

to see the fruits of an uneventful afternoon.

To exit, use

    exit

## This code is pretty bad
This was supposed to be like, a 10 line thing, but I just kept adding stuff 
including gross misuse of click's command line parsing and wrangling with 
the stone-age technology of terminals.

### Why don't you use readline?
Because it breaks shit in weird ways and I have no clue why.

### Why don't you use (n)curses?
It's surprisingly hard to emulate typical shell behaviour using curses, 
and python's curses bindings kinda suck. If this was bigger than a one-file 
thing, I'd probably have used curses or similar, but if this was bigger than 
a one-file thing I'd also be asking myself what I was doing with my life.