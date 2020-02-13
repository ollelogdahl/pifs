from decimal import Decimal, getcontext

import binascii
import datetime
import threading

import util

#------------------------------------------------------------------------------------------

ABC = "abcdefghijklmnopqrstuvwxyzåäö .,!?"
THREAD_COUNT = 1
SEARCH_SIZE = 5000000
BLOCK_BYTES = 8

#------------------------------------------------------------------------------------------

def print_results(encoded, ec_format, binary,filename, start, block_count):
   print("Encode Format: <8>start_block_1;start_block_2;...")
   
   ec_bin = bin(int.from_bytes(str(encoded).encode(), 'big'))
   ec_len = len(ec_bin)
   
   ecf_bin = bin(int.from_bytes(str(ec_format).encode(), 'big'))
   ecf_len = len(ecf_bin)
   print("Format encoding Ratio: "+str((round(ec_len/ecf_len*100)))+"%")
   print("Total Compression: "+str( (round(len(binary)/ecf_len*100)) )+"%")
   print(str(round(len(binary)/8)) + " [Bytes] > " + str(round(ecf_len/8)) + " [Bytes]")
   print()
   print("Wrote to file: " + filename + ".pifs [" + str(round(ecf_len/8)) + " Bytes]" )
   print()
   
   print("Finished: "+str(datetime.datetime.now())+"")
   delta = datetime.datetime.now() - start
   t = delta.seconds + (delta.microseconds / 1e6)

   print("Process took: "+ str(round(t,2)) + " seconds"
   " to complete.")
   print("[" + str(round(t/block_count, 2)) + " seconds per block]")
   print()

def print_start(starttime):
   print("Started: "+str(starttime))
   print("Threads: "+str(THREAD_COUNT) + " [SINGLE-THREADING]")
   print("Chunk size: " + str(SEARCH_SIZE) + " Characters")
   print("Block size: " + str(BLOCK_BYTES) + " Bytes")
   print()

#------------------------------------------------------------------------------------------

def thread_start():
   pass

#------------------------------------------------------------------------------------------

def compress(data, filename):
   threads = []
   decimal = ""

   start = datetime.datetime.now()
   print_start( start )
   
   for character in data:
      decimal = decimal+str( ABC.find(character) + 10)

   binary = bin(int.from_bytes(decimal.encode(), 'big'))
   bin_len = len(str(binary))
   dec_len = len(decimal)
   
   digit_count = int(dec_len / 2 )
   block_count = int(dec_len / BLOCK_BYTES )
   extra = digit_count%BLOCK_BYTES
   if extra > 0:
      block_count += 1;

   blocks = []
   for i in range(0, block_count):
      s = int(i) * BLOCK_BYTES
      end = int(s) + BLOCK_BYTES
      blocks.append( decimal[s:end] )
      
   print("Compressing "+str(digit_count)+" digits ["+str(round(bin_len/8))+" Bytes]")
   if extra > 0:
      print(
         "(" + str(block_count - 1) + " Full blocks, " +
         str(int(extra)) + " Digits)"
      )
      blank = " "
      for e in range(BLOCK_BYTES - extra):
         decimal = decimal+str( ABC.find(blank) + 10)
      print("[added " + str(BLOCK_BYTES - extra) + " blank bytes]")
   else:
      print("["+str(block_count)+" blocks]")

   print()
   util.cprint([["Block", "Byte", "Decimal", "Thread"]], 16)
   print("--------------------------------------------------------")

   encoded = []
   for block in blocks:
      encoded.append( util.find(0, block, blocks, SEARCH_SIZE) )
      
   print()
   print("All blocks found: "+str(datetime.datetime.now())+"\n")

   ec_format = encoded
   chars = "[]"
   for c in chars:
      ec_format = str(ec_format).replace(c, "")
      
   ec_format = ec_format.replace(", ","A")
   ec_bytes = int(ec_format).to_bytes(ec_format, byteorder='big')
   
   file = open( filename + ".pifs", "wb")
   file.write( ec_bytes)
   file.close()

   print_results(encoded, ec_format, binary, filename, start, block_count)

#------------------------------------------------------------------------------------------

def decompress(filename):
   file = open(filename + ".pifs", 'r')
   data = file.read()
   file.close()

   s = 1
   data = data.split(";")

   decoded = ""
   i = 0
   for addr in data:
      decimal = util.get_chunk(int(addr), BLOCK_BYTES)
      
      n = 2
      ch = [decimal[i:i+n] for i in range(0, len(decimal), n)]
      print("Block-" + str(i) + "   ", end="")
      print(ch)
      for c in ch:
         c = int(c) - 10;
         c = ABC[c:c+1]
         decoded = decoded+str(c)

      i += 1
   print(decoded)
   print()

#------------------------------------------------------------------------------------------
while True:
   i = input("[c]ompress or [d]ecompress? ")
   if i == "c":
      text = input("Input text you want to compress: ")
      print()
      compress(text, "compress")
   elif i == "d":
      decompress("compress")
