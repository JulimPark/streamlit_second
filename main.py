import streamlit as st
import pandas as pd
import os
import numpy as np
import datetime
import ast


st.write("hello!~~bye!!!")
df = pd.DataFrame(pd.read_csv('./exam_data.csv'))

st.title('수학클리닉:blue[🞧]필요와충분')

st.header('정답제출 시스템')

stu_name = st.text_input('*:blue[이름]을 입력하세요: ', '홍길동')
st.write('현재 응시자는 '+stu_name+'입니다')

test_num = st.text_input('*:red[시험지코드]를 입력하세요 ', '0001')
if int(test_num) in list(df['시험고유번호']):
    df1 = df[df['시험고유번호']==int(test_num)].loc[:,]
    test_answer = ast.literal_eval(df1.iat[0,5])
    test_answer = [str(i) for i in test_answer]
    st.write('문항 수:',len(test_answer))
    st.write(test_answer)
    testname = df1.iat[0,1]
    st.write(f'현재 시험지는 *:blue[{testname}] 입니다')
    start = st.button('시험시작')
if start:
    timestamp = datetime.datetime.now()
submit_answer = [num for num in range(len(test_answer))]
lst=('','1','2','3','4','5')

for i in range(len(test_answer)):
    if test_answer[i] in ['1','2','3','4','5']:
        submit_answer[i] = st.radio(str(i+1)+'번 문항의 정답을 입력하세요.',lst,index=0,horizontal=True)
    elif test_answer[i] in ['1,2','1,3','1,4','1,5','2,3','2,4','2,5','3,4','3,5','4,5']:
        st.write(str(i+1)+'번 문항의 정답을 입력하세요.')
#         temp=[]
#         a1 = st.checkbox('1')
#         if a1==True:
#             temp.append('1')
#         else:
#             pass
#         a2 = st.checkbox('2')
#         if a2==True:
#             temp.append('2')
#         else:
#             pass
#         a3 = st.checkbox('3')
#         if a3==True:
#             temp.append('3')
#         else:
#             pass
#         a4 = st.checkbox('4')
#         if a4==True:
#             temp.append('4')
#         else:
#             pass
#         a5 = st.checkbox('5')
#         if a5==True:
#             temp.append('5')
#         else:
#             pass    
        checks = st.columns(5)
        with checks[0]:
            st.checkbox('1')
        with checks[1]:
            st.checkbox('2')
        with checks[2]:
            st.checkbox('3')
        with checks[3]:
            st.checkbox('4')
        with checks[4]:
            st.checkbox('5')
#         submit_answer[i] = ','.join(temp)
    else:
        submit_answer[i] = st.text_input(str(i+1)+'번 문항의 정답을 입력하세요.')
st.write(checks)
end_test = st.button('시험종료')

if end_test:
    st.write(submit_answer)
    

    
# kk = test_code.index[(test_code['시험지코드']==int(test_num))]

# kk2 = test_code.iloc[kk,2]
# question_num = int(kk2)

# st.write(':green[문항 수]는 '+str(question_num)+'문항 입니다')



# no1 = st.radio(
#     '1번 문항의 정답을 입력하세요.',('1','2','3','4','5')
# )
# st.write(no1)


# for i in range(0, question_num):
#     ns = 'no'+str(i)
#     no.append(ns)

# st.write(no)
# for i in range(0, question_num):
#     no[i] = st.radio(str(i+1)+'번 문항의 정답을 입력하세요.',('1','2','3','4','5'))

# submit = [no[i] for i in range(0,question_num)]
# st.write(submit)


csv_file = 'results_option1.csv'
if os.path.exists(csv_file):
    # read from file
    results_option1 = pd.read_csv(csv_file, index_col=False)
else:
    # create empty dataframe with the right columns & dtypes
    results_option1 = pd.DataFrame(
        {'time': np.array([]).astype('datetime64[ns]'),
         'Primary Air Flow Rate': np.array([], dtype=np.float64),
         'Primary Air Temperature': np.array([], dtype=np.float64),
         'Reference Air Temperature': np.array([], dtype=np.float64),
         }
    )

st.write('before')
st.dataframe(results_option1)

with st.form('input_form'):
    qavalue = st.number_input('Primary Air Flow Rate')
    travalue = st.number_input('Primary Air Temperature')
    trvalue = st.number_input('Reference Air Temperature')
    clickSubmit = st.form_submit_button('Submit')

if clickSubmit:
    timestamp = datetime.datetime.now()
    results_option1.loc[len(results_option1)] = [timestamp, qavalue, travalue, trvalue]
    results_option1.to_csv(csv_file, index=False)
    st.write('after')
    st.dataframe(results_option1)
else:
    st.markdown("Please submit to save")
