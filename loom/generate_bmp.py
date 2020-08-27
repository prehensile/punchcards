##
# Generate a bmp file for weaving from a directory full of text files.
#

import sys, os
import glob

from PIL import Image


# define a function that rotates a 2d array by 90°
# see https://stackoverflow.com/questions/41290350/inplace-rotation-of-a-matrix
# we'll use this to rotate the card data before outputting to an image line
def rotate_matrix( m ):
    return [list(row[::-1]) for row in zip(*m)]


# expect that first command line argument will be a path to a folder holding punchcard textfiles
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

# sort filenames into order
all_textfiles = sorted( all_textfiles )

# generate a new empty image
image_width = 960
image_height = len( all_textfiles )  # i.e one textfile == one row in the image
image_out = Image.new( "1", (image_width,image_height) )

# step through all textfiles in the given path
num_textfiles = len( all_textfiles )
for row, fn_textfile in enumerate(all_textfiles):

    print( "Processing file: {} ({:d} of {:d}, {:0.0f}%)".format(
        fn_textfile,
        row+1,
        num_textfiles,
        (row/num_textfiles) * 100
    ))
    
    # construct path to textfile
    pth_textfile = os.path.join( pth_textfiles, fn_textfile )
    
    # read contents of textfile
    rows = None
    with open(pth_textfile) as fp:
        rows = fp.read()
    
    # rotate hole data through 90°
    # print( rows )
    rows = [ list(row) for row in rows.splitlines() ]
    rows = rotate_matrix( rows )
    #print( "\n".join([ "".join(row) for row in rows]) )
    
    # write rows to image
    # TODO: there is almost certainly a more efficient way to do this ¯\_(ツ)_/¯
    for y, row in enumerate(rows):
        for x, hole in enumerate(row):

            # convert "1" or "0" to 1 or 0
            pixel = int(hole)  

            # invert hole data so that a 1 in the data (hole) gives us 0 in the image (black pixel)
            pixel = 1 if pixel == 0 else 0 

            image_out.putpixel( (x,y), pixel )

image_out.save( fn_bmp )