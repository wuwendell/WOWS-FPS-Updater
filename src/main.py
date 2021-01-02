import os

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

# TODO: add to README.md

tagNameConstant = "<maxFrameRate>"
tagNameCloseConstant = "</maxFrameRate>"

# only run the logic in the script if this was called as an argument using interpreter
if __name__ == "__main__":
    # find the latest file based on numbering system
    os.chdir(r"C:\Games\World_of_Warships_NA\bin")
    dirName = max(os.listdir())
    engineConfigFileName = 'C:\\Games\\World_of_Warships_NA\\bin\\' + dirName + r"\res_mods\engine_config.xml"
    print("Now opening file:", engineConfigFileName)
    with open(engineConfigFileName, 'r+') as f:
        contents = f.read()
        indexOfFrameRateTag = contents.index(tagNameConstant)
        indexOfFrameRateTag += len(tagNameConstant)
        indexOfFrameTagClose = contents.index(tagNameCloseConstant)
        final = contents[:indexOfFrameRateTag] + '175' + contents[indexOfFrameTagClose:]
        f.seek(0)
        f.write(final)
        f.truncate()
        print("successfully wrote to file")
