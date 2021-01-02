import sys

# steps for the FPS checking algorithm

# First iterate over all versions in the WOWS folder
# Wows is found (by default) at C:\Games\World_of_Warships_NA\bin
# Next, we need to iterate over all the folders in that folder
#   Select the one with the highest value by either string comparison or date modified, that's the
#   current version of the game
# Once we have that folder selected, navigate to \foldername\res_mods\engine_config.xml
# open the file for editing, find the tag <maxFrameRate>75</maxFrameRate>
# edit the value inside the tag to be 150 or another value the user can supply later
# save the file and close everything down

# TODO: figure out file reading and writing standard library for python
# TODO: figure out the types used for file i/o
# TODO: figure out convention of doing file i/o for plaintext (read in, edit, write out?)
# TODO: add to README.md

someVar = 1
text = "Some string #blahblahblahblah"

print('text')
print(text)
print(someVar)
