#!/usr/bin/env python3
import sys
import emoji

input_filename  = sys.argv[1]
result_filename = sys.argv[2]
copy_filename   = sys.argv[3]

with open(input_filename, "r") as in_file, open(result_filename, "w") as result_file, open(copy_filename, "w") as copy_file:
     # make a backup
     copy_file.write(in_file.read())

     # reset fp on in_file
     in_file.seek(0)

     # process txt
     result_file.write(
         emoji.emojize(in_file.read(), use_aliases=True)
     )
