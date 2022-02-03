import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
	   """Returns True if there is enough free disk space, false otherwise."""
	   du = shutil.disk_usage(disk)
	   #calcute the percentage of free space
	   percent_free = 100 * du.free / du.total
	   #Calculate how many free gigabytes
	   gigabytes_free = 100 * du.free /2**30
	   if percent_free < min_percent or gigabytes_free < min_absolute:
	   	return False
	   return True
  # Check for at least 20 GB and 10% free
if not check_disk_usage("/", 20, 10):
 	print("ERROR: Not enough disk space")
 	sys.exit(1)

print ("Everyrhing ok")
sys.exit(0) 
