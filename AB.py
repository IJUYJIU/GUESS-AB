import streamlit as st
#default_value_goes_here = '1234'
#user_input = st.text_input("label goes here", default_value_goes_here)

import random
import time        # import time 模組
answer = random.sample(range(1, 10), 4)
print(answer)
a = b = n = 0
num = 0            # 新增 num 變數為 0，作為計算次數使用
t = time.time()    # 新增 t 變數為現在的時間

default_value_goes_here = '1234'
#r = st.text_input('輸入四個數字：', default_value_goes_here)
#user = list(r)
#confirm_input = st.button("ok")
while a!=4:
  num += 1         # 每次重複時將 num 增加 1
  a = b = n = 0
  r = st.text_input('輸入四個數字：', default_value_goes_here)
  user = list(r)
  confirm_input = st.button("ok")
  if confirm_input:
    confirm_input=False
    for i in user:
       if int(user[n]) == answer[n]:
        a += 1
       else:
        if int(i) in answer:
         b += 1
       n += 1
  output = ','.join(user).replace(',','')
  print(f'{output}: {a}A{b}B')
#if confirm_input:
#  t = round((time.time() - t), 3)   # 當 a 等於 4 時，計算結束和開始的時間差
#  print(f'答對了！總共猜了 {num} 次，用了 {t} 秒')   # 印出對應的文字
