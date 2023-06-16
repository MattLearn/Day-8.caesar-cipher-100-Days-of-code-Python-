from static_properties import alphabet, logo

def encrypt(text, shift):
  encryption = ''
  for index in range(len(text)):
    if (alphabet.index(text[index])+shift) >= len(alphabet):
      encryption += (alphabet[alphabet.index(text[index])+shift - len(alphabet)])
    else:
      encryption += (alphabet[alphabet.index(text[index])+shift])
  print(f"The encode is {encryption}")

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def decrypt(text, shift):
  decryption = ''
  for index in range(len(text)):
      decryption += (alphabet[alphabet.index(text[index])-shift])
  print(f"The decode is {decryption}")

print(logo)
inUse = True
while (inUse):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'end' to stop:\n").lower()
  if direction == 'end':
    print("Goodbye!")
    break
    
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if direction == 'encode':
    encrypt(text, shift)
  elif direction == "decode":
    decrypt(text, shift)
