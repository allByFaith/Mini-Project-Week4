# This is the mini-project week4 ------------------------------------------------------------------------------
# File Name     : writeDictToCSV.py
# Date          : 12 Nov 2022
# Developer     : Samuel KO
# Description   : This function receives three parameters.  The function will base
#               : on the pass in file name (e.g. fileProduct.csv) and the file
#                 type (e.g. PRODUCT_HEADER) to write the pass in dictionary to the
#                 data file.
# Input         : Pass in parameters 1) dictionary 2) file name 3) file header
# Output        : STATUS : OK or NOT_OK
# -------------------------------------------------------------------------------------------------------------

import os
import csv
import traceback

def funWriteDICTtoCSV(inDict, inWriteFile, inWriteHeader):

   try:
      STATUS = 'NOT_OK'

      # fields = ['customer_name','customer_address','customer_phone','couriers','status']
      # fields = ['prodName','price']
      # fields = ['name','phone']
      fields=inWriteHeader.split(',') # Convert str to list
      with open(inWriteFile, 'a+') as csvFile:
            # creating a csv dict writer object 
            writer = csv.DictWriter(csvFile, fieldnames = fields) 
            if (os.stat(inWriteFile).st_size == 0):
               # writing headers (field names) 
               writer.writeheader()  
            # writing data rows 
            writer.writerows(inDict)
      STATUS = 'OK'
   except:
      traceback.print_exc()

   return STATUS
 