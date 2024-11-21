"""Prompt: Make something boring."""

import random
import time
import os
import sys

# ASCII art for a boiling water kettle
kettle_ascii = """
   ...::::::..                                 
   .::::...::.            .:-===-:.            
   .:::..:::::::.    .:=##*++++++++*#*=..      
  .::...::::::::.   .**:.           ..:#*.     
  .:::...::::::.   :#=        ..       .*#.    
   ..::::::::::.   =#        *+#+       =#:    
    .::::::::..    :#-     ..*%%-..    .*#.    
     ...::::::.    .-*:  .--=======-. .-%.     
           .:::.    :##.:---=========.-%#.     
            .:==:.  .*#=+*+-------=**+=#=      
             .-==.  .-=-::--========+++=:      
             .-==+-.==-:::-=-----=====+++.     
              .=-=++=-:::----------====++=.    
               :===++-::------------===+++.    
               .:===++=---==------===+++++.    
                 .-=+++==============++++-     
                   ..+++============++++=.     
                     .=++++======++++++-.      
                     :+*#%+**#**+**+%*+=.      
                        .:-=++++++=-..
                    ~ Water is boiling! ~
"""
not_boiling_ascii = """                                 
                          .:-===-:.            
                     .:=##*++++++++*#*=..      
                    .**:.           ..:#*.     
                   :#=        ..       .*#.    
                   =#        *+#+       =#:    
                   :#-     ..*%%-..    .*#.    
                   .-*:  .--=======-. .-%.     
                    :##.:---=========.-%#.     
            .:==:.  .*#=+*+-------=**+=#=      
             .-==.  .-=-::--========+++=:      
             .-==+-.==-:::-=-----=====+++.     
              .=-=++=-:::----------====++=.    
               :===++-::------------===+++.    
               .:===++=---==------===+++++.    
                 .-=+++==============++++-     
                   ..+++============++++=.     
                     .=++++======++++++-.      
                     :+*#%+**#**+**+%*+=.      
                        .:-=++++++=-..
                    ... still not boiling ...
"""
sheep_ascii = r"""
     _ 
  _-(_)-
`(___)
 // \\
"""
sheep_ascii_two = r"""
     _       _  
  _-(_)-  _-(_)-
`(___)  `(___)
// \\   // \\
"""

# Target sum to display the boiling kettle
target_sum = 100
current_sum = 0

print("Waiting for water to boil...\n")

while current_sum < target_sum:
    # Generate a random number
    number = random.randint(-10, 20)
    current_sum += number
    # print(f"Generated: {number} | Current Sum: {current_sum}")

    # Pause for a short duration to simulate real-time generation
    time.sleep(0.5)

    sys.stdout.write(".")
    sys.stdout.flush()
    # Randomly show not boiling kettle
    show_kettle = random.randint(1, 20)
    if show_kettle == 20:
        sys.stdout.write(not_boiling_ascii)
        sys.stdout.flush()


# When target sum is reached, display the ASCII art
sys.stdout.write(kettle_ascii)
