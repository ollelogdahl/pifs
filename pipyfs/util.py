from decimal import Decimal, getcontext
import time

"""
   get_chunk: gå till en plats (seek) och returna allt (buffer_size) steg frammåt
"""
def get_chunk(seek, buffer_size):
   pi = open("pidict.txt", 'r')
   pi.seek(seek)
   chunk = pi.read( int(buffer_size) )
   pi.close()
   return chunk

def find(thread,block, blocks, search_size):
   found = False
   encoded = ""
   while( found == False ):
      i = 0
      while( found == False ):
         chunk = get_chunk(search_size*i, search_size)
         s = search_size*i
         pif = chunk.find(block)
         if pif == -1:
            i += 1
         else:
            found = True
            cprint([[
               str(blocks.index(block)), "["+str(pif + s)+"]",
               block, "Thread-" + str(thread)]], 16
            )
            encoded = pif + s

   return encoded

def cprint(data, w):
   col_width = w
   for row in data:
      print( "".join(word.ljust(col_width) for word in row) )
