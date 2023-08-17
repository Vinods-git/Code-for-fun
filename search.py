# importing the module
import pywhatkit
 
# using Exception Handling for
# handling unprecedented errors
try:
   
  # it will perform google search
  pywhatkit.info("Microsoft", lines = 4)
  print("\nSuccessfully Searched")
 
except:
     
  # printing error message
  print("An Unknown Error Occurred")