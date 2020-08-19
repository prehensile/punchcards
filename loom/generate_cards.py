##
# Generate a bunch of dummy card text files for testing.
#

import sys, os
import glob 
import subprocess
import random

# expect that first argument will be a path to a folder holding card textfiles
pth_textfiles = sys.argv[1]
pth_textfiles = os.path.realpath( pth_textfiles )

num_cards = int( sys.argv[2] )


card_size = ( 80, 12 )
for i in range( num_cards ):
    card_data = ""
    for y in range( card_size[1] ):
        for x in range( card_size[0] ):
            card_data += "1" if random.random() > 0.5 else "0"
        card_data += "\n" 
    pth_dump = os.path.join( pth_textfiles, "%04d.txt" % i )
    with open( pth_dump, "w" ) as fp:
        fp.write( card_data )
exit()
