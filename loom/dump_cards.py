##
# Dump a directory full of punch card images to text files.
#

import sys, os
import glob 
import subprocess


# details for punchcard.py script
pth_punchcard_script = "../punchcards/punchcard.py"
pth_punchcard_script = os.path.realpath( pth_punchcard_script )
script_args = [ "-u", "-b", "127", "--row-height", "0.255"]
script_args = [ "python", pth_punchcard_script ] + script_args

# expect that first argument will be a path to a folder holding punchcard image files
pth_images = sys.argv[1]

# construct a path to the textfiles
pth_images = os.path.realpath( pth_images )
pth_images = os.path.join( pth_images, "*.*")

# acceptable image files
image_types = [ ".png", ".gif" ]

# step through all files in the given path
for fn_image in glob.glob( pth_images ):

    # if file isn't one of our acceptable types, skip it
    if not (fn_image[-4:] in image_types):
        continue
    
    # construct path to image
    pth_image = os.path.join( pth_images, fn_image )

    # construct punchcard script arguments for this image
    # use a copy of script_args so we don't accumulate file names with each run
    this_args = list(script_args) 
    this_args.append( pth_image )
    
    # run the script and hold the output in card_dump
    card_dump = subprocess.check_output( this_args )

    # write card_dump to a textfile
    fn_dump = fn_image[:-4] + ".txt"
    pth_dump = os.path.join( pth_images, fn_dump )
    with open( fn_dump, "wb" ) as fp:
        fp.write( card_dump )
    
    
