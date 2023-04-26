import streamlit as st
import pandas as pd
import os
import numpy as np
import datetime
import ast
import fnmatch

st.write("hello!~~bye!!!")
df = pd.DataFrame(pd.read_csv('./exam_data.csv'))
df = df.astype({'정답':'str'})

def test_start():
    st.write('시작')

st.title('수학클리닉:blue[🞧]필요와충분')

st.header('정답제출 시스템')

stu_name = st.text_input('*:blue[이름]을 입력하세요: ', '홍길동')
st.write('현재 응시자는 '+stu_name+'입니다')

test_num = st.text_input('*:red[시험지코드]를 입력하세요 ', '0001')
if int(test_num) in list(df['시험고유번호']):
    df1 = df[df['시험고유번호']==int(test_num)].loc[:,]
    st.write(df1)
    test_answer = ast.literal_eval(df1.iat[0,5])
    st.write('문항 수:',len(test_answer))
    testname = df1.iat[0,1]
    st.write(f'현재 시험지는 *:blue[{testname}] 입니다')
    start = st.button('시험시작')
    if start:
        timestamp = datetime.datetime.now()
        submit_answer = [num for num in range(len(test_answer))]
        for i in range(len(test_answer)):
            if test_answer[i] in ['1','2','3','4','5']:
                submit_answer[i] = st.radio(str(i+1)+'번 문항의 정답을 입력하세요.',('1','2','3','4','5'))
            elif fnmatch.fnmatch(test_answer[i],'*,*'):
                st.write(str(i+1)+'번 문항의 정답을 입력하세요.')
                a1 = st.checkbox('1')
                a2 = st.checkbox('2')
                a3 = st.checkbox('3')
                a4 = st.checkbox('4')
                a5 = st.checkbox('5')
                submit_answer[i] = [a1,a2,a3,a4,a5]
            else:
                submit_answer[i] = st.text_input(str(i+1)+'번 문항의 정답을 입력하세요.')
        
else:
    pass

    
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
