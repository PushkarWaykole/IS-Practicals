# -*- coding: utf-8 -*-
"""Final Practicals IS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EnXhDadN-qUkZOXD-phDAHyl7XNK0CGn

FINAL LIST OF EXPERIMENTS For Information Security Practical Exam
--------------------------------------------------------------------------------------------------------------------------------------------

 

1.To implement Caesar Cipher 
 


	
Plaintext will be provided 
	
Obtain Ciphertext

 
--------------------------------------------------------------------------------------------------------------------------------------------

 

2. To implement Vignere Cipher (26 Caesar Ciphers)
 



	
Plaintext will be provided 
	
Obtain Ciphertext


 
--------------------------------------------------------------------------------------------------------------------------------------------

 


3. To implement Columnar / Double Columnar Transposition
 



	
Plaintext will be provided
	
Keys will be provided
	
Obtain Ciphertext



__________________________________________________________________________________________________________________________________________
 

4. To implement Playfair Cipher
 



	
Plaintext will be provided 
	
Obtain Ciphertext


 
--------------------------------------------------------------------------------------------------------------------------------------------

 
5. To implement Electronic Code Book
 



	
Plaintext will be provided 
	
Obtain Ciphertext


--------------------------------------------------------------------------------------------------------------------------------------------

 

6. To implement simplified DES
 



	
Plaintext will be provided 
	
Obtain Ciphertext


 
--------------------------------------------------------------------------------------------------------------------------------------------

 

7. To implement RSA algorithm



	
Follow RSA Algorithm, 
	
Take inputs from the user(integer or character, will be prompted in the question)
	
	
Obtain the Ciphertext and Retrieve the Plaintext back.

 
--------------------------------------------------------------------------------------------------------------------------------------------

 

8. To Implement Diffie Hellman Algorithm



	
Follow DH Algorithm.
	
Take inputs from the user.
	
Obtain the Shared Secret Key


 
--------------------------------------------------------------------------------------------------------------------------------------------

9. To implement Merkel Tree

 
--------------------------------------------------------------------------------------------------------------------------------------------
 

10. To demonstrate Packet sniffing using wireshark.



	
Sniff Passwords
	
Sniff traffic from a particular protocol
	
application, etc

 
--------------------------------------------------------------------------------------------------------------------------------------------

 

11.To implement your own Substitution/Transposition Cipher



	
Plaintext will be provided.
	
Obtain the Ciphertext.

#Ceaser Cipher
"""

def encrypt(pt,key):
  ans=""
  # print(pt,key)
  for i in pt:
    if(i==" "):
      ans+=" "
    else:

      temp=((ord(i)+key-97)%26)
      
      ans+=chr(temp+97)
  # print(ans)  
  return ans

def decrypt(ct,key):
  ans=""
  # print(ct,key)
  # print(ct)
  for i in ct:
    if i==" ":
      ans+=" " 
    else:

      temp=((ord(i)-key-97+26)%26)
      
      ans+=chr(temp+97)
  # print(ans)
  return ans

pt="abc"
key=3
ct=encrypt(pt,key)
print(ct)
print(decrypt(ct,key))

"""#Vignere Cipher"""

# Python code to implement
# Vigenere Cipher

# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
	
# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) + ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
	
# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) -
			ord(key[i]) + 26) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))
	
# Driver code
if __name__ == "__main__":
	string = "GEEKSFORGEEKS"
	keyword = "AYUSH"
	key = generateKey(string, keyword)
	cipher_text = cipherText(string,key)
	print("Ciphertext :", cipher_text)
	print("Original/Decrypted Text :",
		originalText(cipher_text, key))

"""#Columnar transposition Cipher"""

def printMat(mat):
  for i in mat:
    print(i)


def encrypt(pt,key):
  matrix=[]
  # print(matrix)
  n=len(key)
  temp=pt
  completed=False
 
  while(len(temp)!=0):
    level=[]
    if(not completed):

      for j in range(n):
        if(len(temp)!=0):
          level.append(temp[0])
          temp=temp[1:]
        else:
          level.append('x')
          completed=True
      # print(level)
      
      
      matrix.append(level)
  
  printMat(matrix)
  # print(key)
  original_map=[]
  for i,alpha in enumerate(key):
    original_map.append([alpha,i])
  # print(original_map)

  key=list(key)
  temp=list(sorted(key))
  # print(temp)
  map=[]
  for i,alpha in enumerate(temp):
    map.append([alpha,i])

  n=len(matrix)
  # print(n)
  transpose=[]
  for i in range(len(key)):
    level=[]
    for j in range(n):
      # print(matrix[j][i])
      level.append(matrix[j][i])
    transpose.append(level)
  printMat(transpose)

  ans=""
  visited=[]
  for i in map:
    alpha=i[0]
    index=0
    for y in original_map:
      if(y[0]==alpha and y[1] not in visited):
        index=y[1]
        visited.append(index)
        break
    # print(index)
    temp=transpose[index]
    for j in temp:
      ans+=j
  # print(ans)

  return (ans,original_map,map)
  
  
encrypt("columnartransposition","heaven")


import math
def decrypt(map,o_map,key,ct):
  n_rows=math.ceil(len(ct)/len(key))
  # print(n_rows)
  text=[ct[i:i+n_rows] for i in range(0, len(ct), n_rows)]
  print(text)
  indexes=[]
  visited=[]
  for i in map:
    alpha=i[0]
    index=0
    for y in o_map:
      if(y[0]==alpha and y[1] not in visited):
        index=y[1]
        # print(index)
        visited.append(index)
        break
    indexes.append(index)
  
  # print(indexes)
  mat=[]
  for i in indexes:
    mat.append(text[i])
  # print(mat)
  
  ans=[]
  for i in range(n_rows):
    first=([word[i] for word in mat])
   
    ans.append(first)

  fans=""
  for word in ans:
    x="".join([str(i) for i in word])
    fans+=x
  # print(ans)
  # print(fans)
  index=fans.find('x')
  if index!=-1:
    fans=fans[:index]
  return fans
  




pt="columnartransposition"
key="heaven"

cipher_text,o_map,map=encrypt(pt,key)
print("Cipher text is: ",cipher_text)
plain_text=decrypt(o_map,map,key,cipher_text)
print("Plain text is: ",plain_text)

"""#Playfair Cipher"""

def createTable(key):
    k=[]
    for i in key:
        if i not in k:
            if i=="J":
                k.append("I")
            else:
                k.append(i)
    for i in range(65,91):
        if i==74:
            continue
        if chr(i) not in k:
            k.append(chr(i))
    table=[]
    for i in range(5):
        table.append(k[:5])
        k=k[5:]
    return table

def group2(s):
    l=len(s)
    group = []
    i=0
    while i<l-1:
        if s[i]!=s[i+1]:
            group.append(s[i]+s[i+1])
            i+=2
        else:
            if s[i]=="X":
                t="Y"
            else:
                t="X"
            group.append(s[i]+t)
            i+=1
    if i==l-1:
        if s[i]=="X":
                t="Y"
        else:
            t="X"
        group.append(s[i]+t)
    return group

def search(table,e):
    for i in range(5):
        for j in range(5):
            if table[i][j]==e:
                return i,j


# Encryption

s = input("Enter plain text : ").upper()
k = input("Enter key : ").upper()

def encrypt(s,k):
    group = group2(s)
    table = createTable(k)
    ans=""
    for g in group:
        c1,c2=g[0],g[1]
        i1,j1=search(table,c1)
        i2,j2=search(table,c2)
        if i1==i2:
            ans+=table[i1][(j1+1)%5]+table[i2][(j2+1)%5]
        elif j1==j2:
            ans+=table[(i1+1)%5][j1]+table[(i2+1)%5][j2]
        else:
            ans+=table[i1][j2]+table[i2][j1]
    return ans

print("Encrypted text is :",encrypt(s,k))


# Decryption

s = input("Enter cipher text : ").upper()
k = input("Enter key : ").upper()

def decrypt(s,k):
    group = group2(s)
    table = createTable(k)
    ans=""
    for g in group:
        c1,c2=g[0],g[1]
        i1,j1=search(table,c1)
        i2,j2=search(table,c2)
        if i1==i2:
            ans+=table[i1][(j1+4)%5]+table[i2][(j2+4)%5]
        elif j1==j2:
            ans+=table[(i1+4)%5][j1]+table[(i2+4)%5][j2]
        else:
            ans+=table[i1][j2]+table[i2][j1]
    return ans

print("Decrypted text is :",decrypt(s,k))

"""#ECB"""

pt="abcdefghijklmnopqrstert"
key="fd^jkh8gfd5jk3$3"
def split_n(text,n):
  blocks=[]
  while(len(text)!=0):
      blocks.append(text[:n])
      text=text[n:]
  l=len(blocks[-1])
  if(l!=n):
      while(l!=n):
          blocks[-1]+="x"
          l+=1
  return blocks
def convert_to_binary(char):
  n=ord(char)
  binary=""
  while(n>=1):
      if(n%2==1):
          binary+="1"
      else:
          binary+="0"
      n=n//2
  l=len(binary)
  while(l!=8):
      binary+="0"
      l+=1
  binary=binary[::-1]
  return binary
    
convert_to_binary('a')


def find_xor(a,b):
    xor=""
    for i in range(len(a)):
        xor+=str(int(a[i])^int(b[i]))
    return xor

find_xor("101","111")

def binaryToDecimal(binary):
  binary=int(binary)
  decimal, i = 0, 0
  while(binary != 0):
      dec = binary % 10
      decimal = decimal + dec * pow(2, i)
      binary = binary//10
      i += 1
  return decimal

def encrypt(pt,key):
    print(pt,key)
    print("First split the pt into blocks of size 16 each")
    blocks=split_n(pt,16)
    print(blocks)
    
    print("Now we need to convert the key to binary")
    key_binary=""
    for c in key:
        key_binary+=convert_to_binary(c)
    print("The key in binary: ",key_binary)
    print("Now convert the blocks into binary")
    binary_blocks=[]
    for block in blocks:
        temp=""
        for c in block:
            temp+=convert_to_binary(c)
        binary_blocks.append(temp) 
    print("The binary blocks are: ",binary_blocks) 
    
    
    
    print("Now doing xor with the key")
    cipher_blocks=[]
    for block in binary_blocks:
        xored=find_xor(key_binary,block)
        cipher_blocks.append(xored)
    print("The ciphered blocks are:",cipher_blocks)
    
    print("Now shifting the blocks by one to the left")
    shifted_binary_blocks=[] 
    for block in cipher_blocks:
        first=block[0]
        block=block[1:]
        block+=first
        shifted_binary_blocks.append(block)
    print("The shifted binary blocks are: ",shifted_binary_blocks)
    
    print("Generating the cipher text")
    ct=""
    for block in cipher_blocks:
        temp=split_n(block,8)
        for c in temp:
            asci=binaryToDecimal(c)
            asci=asci%128
            print(asci)
            ch=chr(asci)
            ct+=ch
    return ct
        
        
     
ct=encrypt(pt,key)
print(ct)

"""#Simplified DES"""

def blocksof4(text):
  blocks = []
  while(text!=''):
      blocks.append(text[:4])
      text = text[4:]

  return blocks

def expansionPermutation(RPT, KEY):
  blocksRPT = blocksof4(RPT)
  n = len(blocksRPT)
  # print(blocksRPT)
  expandedRPT = []
  for inx, word in enumerate(blocksRPT):
      if inx==0:
          temp = blocksRPT[-1][-1] + word + blocksRPT[1][0]
      elif inx==(n-1):
          temp = blocksRPT[-2][-1] + word + blocksRPT[0][0]
      else:
          temp = blocksRPT[inx-1][-1] + word + blocksRPT[inx+1][0]
      
      expandedRPT.append(temp)
  # print(expandedRPT)
  expandedRPT_str = ''.join(expandedRPT)
  
  
  
  XORed = ''
  for pt, k in zip(expandedRPT_str, KEY):
      XORed += str(int(pt)^int(k))
  
  blocksof6 = []
  while XORed!='':
      blocksof6.append(XORed[:6])
      XORed = XORed[6:]
  
  
  sbox = []
  for i in blocksof6:
      temp = i[1:5]
      sbox.append(temp)
  

  
  sbox_str = ''.join(sbox)

  return sbox_str

def encryption(PT, KEY1, KEY2):
  n = len(PT)
  n = n//2
  lpt = pt[:n]
  rpt = pt[n:]
  
  for i in range(2):
      print('\n\nLPT :', lpt)
      print('RPT :', rpt)
      if(i==0):
          sbox = expansionPermutation(rpt, KEY1)
      else:
          sbox = expansionPermutation(rpt, KEY2)

      xor = ''
      for l, k in zip(lpt, sbox):
        
          xor += str(int(l)^int(k))
      
      lpt = xor
      lpt, rpt = rpt, lpt

  
  return lpt + rpt

pt = '0100110010100001101101001100111000000110010111110100010001010010'
key1 = '001111111010110111000011111100010110110011110100'
key2 = '110000000101001000111100000011101001001100001011'
print("\nPLAIN TEXT:", pt)
ct = encryption(pt, key1, key2)
print("\n\nCIPHERED TEXT:", ct)

"""#RSA Algorithm"""

N=1000000
primes=[True]*N
for i in range(2,N):
  if primes[i]:
    for j in range(i*i,N,i):
      primes[j]=False

print(primes[24])

def find_nearest_prime(n):
  if primes[n]:
    return n
  
  for i in range(n,N):
    if primes[i]:
      return i
  
  return -1

import math
def find_e(phi,p,q):
  for e in range(2,N):
    if math.gcd(phi,e)==1 and e is not q and e is not p:
      return e

def RSA():

  
  p=input("Enter the p string: ")
  q=input("Enter the q string: ")

  n1=len(p)
  n2=len(q)
  print(n1,n2)

  p=find_nearest_prime(n1)
  q=find_nearest_prime(n2)

  if p==q:
    q=find_nearest_prime(q+1)
  
  print("The values of p and q are: ",p,q)
  # print(p,q)

  n=(p)*(q)
  print("The value of n is: ",n)

  phi=(p-1)*(q-1)
  print("The value of phi(n) is: ",phi)

  #Calculate d
  # (d*e)mod phi=1
  
  # to find e that is the number which is co prime with phi(n)

  e=find_e(phi,p,q)
  # print("The value o "e)

  d=0
  index=-1
  for k in range(2,N):
    if k is not e:
      if ((k*e) % phi)==1:
        print("In the loop ",k)
        d=k
        break
  
  print(d)

  PT=int(input("Enter the plain text number: "))

  #the value of PT should be less than phi(n)
  PT=PT%phi

  print("The original Plain text is: PT%phi(n)",PT)
  CT=pow(PT,e)%n
  print("The cipher text number is: ",CT)
  PT=pow(CT,d)%n
  print("The plain text number is: ",PT) 




RSA()

"""#Diffie hellman key exchange

"""

def diffie(g,a,b,p):
  a_generated=pow(g,a)%p
  b_generated=pow(g,b)%p

  shared_key_a=pow(b_generated,a)%p
  shared_key_b=pow(a_generated,b)%p

  if(shared_key_a==shared_key_b):
    print("Authentication successfull")
  else:
    print("Authentication Failed")


#P = 23, G = 9 ,a = 4, b = 3
diffie(9,4,3,23)

"""#Merkel tree"""

input="1,2,3,4,5".split(',')
print(input)

import hashlib
def hash(val):
  return hashlib.sha256(val.encode('utf-8')).hexdigest()

def merkel_root(input):
  while(len(input) & (len(input)-1)!=0):
    input.append('$')
  print("After inserting dummy values input is :",input)
  level=0
  while(len(input)!=1):
    temp=[]
    for i in range(0,len(input)-1,2):
      val=hash(input[i])+hash(input[i+1])
      temp.append(val)
    print("At level ",level)
    for i in temp:
      print(i)
    level+=1
    input=temp
  
  root=input[0]
  print("The final root is: ",root)
  

merkel_root(input)