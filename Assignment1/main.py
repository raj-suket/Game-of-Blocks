from Crypto.Hash import SHA256 #installed pycrypto library through pip
import time

h=SHA256.new()
s=input("Enter the string: ")
begin=time.time()
res = bytes(s, 'utf-8')
i=1
while True:
    news=res
    hn=SHA256.new()
    hn.update(res)
    x=str(i)
    res1=bytes(x, 'utf-8')
    hn.update(res1)
    ans=hn.hexdigest()
    ans=int(ans, 16)
    if ans<0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF :
        time.sleep(1)
        end=time.time()
        print(f'\nThe required positive number is : {i}')
        break
    
    i=i+1

print(f"\nExecuted with total time {end - begin} seconds")