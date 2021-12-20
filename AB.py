import streamlit as st

import random
import time       
answer = random.sample(range(1, 10), 4)
a = b = n = 0
num = 0            
t = time.time()    
while a!=4:
  num += 1         
  a = b = n = 0
  user = st.number_input('輸入四個數字')
confirm_input = st.button("ok")
if confirm_input:
  for i in user:
    if int(user[n]) == answer[n]:
      a += 1
    else:
      if int(i) in answer:
        b += 1
    n += 1
  st.number_output = ','.join(user).replace(',','')
  st.write(f'{output}: {a}A{b}B')
t = round((time.time() - t), 3)   
st.write(f'答對了！總共猜了 {num} 次，用了 {t} 秒')   
st.write(answer)
