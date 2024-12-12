
import pickle
import streamlit as st
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)
def predict(温度, 饱和点, 高度):
    input = [[x1, x2, x3]] 
    pred = model.predict(input)
    return pred[0]
x1 = st.slider('温度', 0.0, 60.0, 5.0)
x2 = st.slider('饱和点', 0.0, 60.0, 5.0)  
x3 = st.slider('高度', 0.0, 60.0, 5.0)

if st.button('预测'):
    pred = predict(x1, x2, x3)
    st.write('预测结果:', pred)
