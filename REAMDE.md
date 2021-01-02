## WOWS-FPS-Updater

Because the game World of Warships updates frequently, any FPS modifications made to the client are overridden often.

I don't want to keep doing this manually every update, so I've designed a python script 
that I will schedule to run with Windows Task Scheduler every day or so (time interval TBD).

This is also a personal exercise in writing python, so not everything will be perfect.
I am still learning the ropes with this highly abstract language.


#### TODO

1. Core functionality (args checking)
2. Arguments for custom game folder/path
3. Argument for modded/not modded (boolean switch probably, -modded or -m)
4. Argument for custom FPS value (default will be 150)