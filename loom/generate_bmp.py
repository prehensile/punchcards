##
# Generate a bmp file for weaving from a directory full of text files.
#

import sys, os
import glob

from PIL import Image


# expect that first argument will be a path to a folder holding punchcard textfiles
pth_textfiles = sys.argv[1]

# get output filename from arguments if it's there
fn_bmp = "loom.bmp"
if len(sys.argv) > 1:
    fn_bmp = sys.argv[2]

# construct a path to the textfiles
pth_textfiles = os.path.realpath( pth_textfiles )
pth_textfiles = os.path.join( pth_textfiles, "*.txt")

# get all filenames for textfiles
all_textfiles = glob.glob( pth_textfiles )

# generate a new empty image
image_width = 960
image_height = len( all_textfiles )  # i.e one textfile == one row in the image
image_out = Image.new( "1", (image_width,image_height) )

# step through all textfiles in the given path
for row, fn_textfile in enumerate(all_textfiles):
    
    # construct path to textfile
    pth_textfile = os.path.join( pth_textfiles, fn_textfile )
    
    # read contents of textfile
    holes = None
    with open(pth_textfile) as fp:
        holes = fp.read()
    
    # remove newlines from textfile, giving us all the holes on one line
    holes = holes.replace( "\n", "" )

    # write holes to image
    # TODO: there is almost certainly a more efficient way to do this ¯\_(ツ)_/¯
    for column, h in enumerate(holes):
        
        # convert "1" or "0" to 1 or 0
        pixel = int(h)  

        # invert hole data so that a 1 in the data (hole) gives us 0 in the image (black pixel)
        pixel = 1 if pixel == 0 else 0 

        image_out.putpixel( (column,row), pixel )

image_out.save( fn_bmp )