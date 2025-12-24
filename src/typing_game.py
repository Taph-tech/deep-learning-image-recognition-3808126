import time


'''
target_text = "The quick brown fox jumps over the lazy dog."
print("Type the following text as quickly as you can:")
print(target_text)

input("Press Enter when you're ready to start...")
start_time= time.time()

user_input = input("Start typing here: ")
end_time = time.time()

if user_input == target_text:
    elasped_time = end_time - start_time
    print(f'You typed the text in: {elasped_time:.2f} seconds.')
else:
    print("Try again.")
    
    
    
# password cracker

import time
import itertools

password = input("Enter a password to be cracked: ")
start_time = time.time()
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
guess = []
for length in range(1, 9):  # Limiting to passwords of length 1 to 8
    for attempt in itertools.product(characters, repeat=length):
        guess = ''.join(attempt)
        if guess == password:
            end_time = time.time()
            print(f'Password "{password}" cracked in {end_time - start_time:.2f} seconds!')
            break
    else:
        continue
    break
'''
  
 
password = input("Enter a password to be cracked: ")
start_time = time.time()
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
guess = []
for val in range(password.__len__()):
  a = [i for i in characters]
  for y in range(val):
    a = [x + i for i in characters for x in a]
    guess = guess + a
    if password in guess:
      break
    end_time = time.time()
    clock = str(end_time - start_time)
    
print("Your password is: "+ password)
print("It took "+ clock + " seconds to crack your password.")






     