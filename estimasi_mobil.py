import pickle
import streamlit as st

model = pickle .load(open('estimasi_mobil.sav','rb'))

st.title('Estimasi Jarak Tempuh Mobil')

Selling_price = st.number_imput('Input Harga Mobil')
Owner = st.number_input('Input Owner Mobil')
Present_Price = st.number('Input Harga Sekarang')
Year = st.number('Input Tahun Mobil')

predict = ''

if st.button('Estimasi Jarak Tempuh'):
    predict = model.predict(
        [[Selling_price,Owner,Present_Price,Year]]
    )
    st.write ('Estimasi Tahun Mobil dalam Ponds :', predict)
