#! python3
# Dummy Python code to generate OTP (One Time Password)

import random

class OTPMaker:
  # This class uses two functions for OTP. One to create and other to send
  
  def createOTP():
    """ Function to generate OTP """
	  code = []
	  for i in range(6):
		  code.append(random.randint(0,9))
	  return "".join(str(code) for c in code)
  def sendOTP(code):
    """ Function to send OTP. """
    # Modify the code here to change from print to any output 
    print("Your OTP is " + code + ". Kindly do not share it with anyone")
