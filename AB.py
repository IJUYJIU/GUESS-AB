import streamlit as st
#title = st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)

import random
import time       
w = random.sample(range(1, 10), 4)
a = b = n = 0
num = 0            
t = time.time()    
while a!=4:
  num += 1         
  a = b = n = 0
  title = st.text_input('Movie title', 'Life of Brian')
  st.write('The current movie title is', title)
  
  h = list(title)
confirm_input = st.button("ok")
if confirm_input:
    for i in user:
      if int(user[n]) == w[n]:
        a += 1
      else:
        if int(i) in w:
          b += 1
      n += 1
    output = ','.join(h).replace(',','')
    st.write(f'{output}: {a}A{b}B')
t = round((time.time() - t), 3)   
st.write(f'答對了！總共猜了 {num} 次，用了 {t} 秒')   
st.write(w)
