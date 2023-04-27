import streamlit as st
import pandas as pd
import os
import numpy as np
from datetime import datetime
import ast



@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')


st.write("hello!~~bye!!!")
df = pd.DataFrame(pd.read_csv('./exam_data.csv'))

st.title('수학클리닉:blue[+]필요와충분')

st.header('정답제출 시스템')

stu_name = st.text_input('*:blue[이름]을 입력하세요: ', '홍길동')
st.write('현재 응시자는 '+stu_name+'입니다')

test_num = st.text_input('*:red[시험지코드]를 입력하세요 ','0001')
try:
    if int(test_num) in list(df['시험고유번호']):
        df1 = df[df['시험고유번호']==int(test_num)].loc[:,]
        test_answer = ast.literal_eval(df1.iat[0,5])
        jumsu = ast.literal_eval(df1.iat[0,6])
        test_answer = [str(i) for i in test_answer]
        st.subheader(f'본 시험의 문항 수는 :green[{len(test_answer)}]문항 입니다.')
        testname = df1.iat[0,1]
        st.subheader(f'현재 시험지는 :blue[{testname}] 입니다')
        st.subheader(f':red[시험시작 버튼을 눌러야 풀이시간 측정이 가능합니다.]')
        start = st.button('시험시작')
    else:
        st.write('시험지에 기록된 시험지코드를 정확히 입력하세요.')
    # try:
    if start:
        aaa = datetime.now()
        timestamp1 = aaa.timestamp()
        temp_dict = {'시작시간':timestamp1}
        df11 = pd.DataFrame(temp_dict, index=[0])
        df11.to_csv('temp_csv.csv',index=False,mode='w')
    submit_answer = [num for num in range(len(test_answer))]
    lst=('','1','2','3','4','5')

    for i in range(len(test_answer)):
        if test_answer[i] in ['1','2','3','4','5']:
            submit_answer[i] = st.radio(f':red[{str(i+1)}]번 문항의 정답을 입력하세요.',lst,index=0,horizontal=True)
        elif test_answer[i] in ['1,2','1,3','1,4','1,5','2,3','2,4','2,5','3,4','3,5','4,5']:
            st.write(f':red[{str(i+1)}]번 문항의 정답을 입력하세요.')
            temp=[]

            checks = st.columns(5,gap="small")
            with checks[0]:
                a1 = st.checkbox('1')
                if a1==True:
                    temp.append('1')
                else:
                    pass
            with checks[1]:
                a2 = st.checkbox('2')
                if a2==True:
                    temp.append('2')
                else:
                    pass
            with checks[2]:
                a3 = st.checkbox('3')
                if a3==True:
                    temp.append('3')
                else:
                    pass
            with checks[3]:
                a4 = st.checkbox('4')
                if a4==True:
                    temp.append('4')
                else:
                    pass
            with checks[4]:
                a5 = st.checkbox('5')
                if a5==True:    
                    temp.append('5')
                else:
                    pass    
            submit_answer[i] = ','.join(temp)
        else:
            submit_answer[i] = st.text_input(f':red[{str(i+1)}]번 문항의 정답을 입력하세요.')
        st.divider()

    end_test = st.button('시험종료')

    if end_test:
        bbb = datetime.now()
        timestamp2 = bbb.timestamp()
        df12 = pd.DataFrame(pd.read_csv('temp_csv.csv'))
        timestamp11 = df12.iat[0,0]
        df12 = df12.drop(0)
        df12.to_csv('temp_csv.csv',mode='w',index=False)
        correct = []
        incorrect = []
        sum1= 0
        remaintime = round((timestamp2-timestamp11)/len(test_answer),2)
        timelist = [remaintime for i in range(len(test_answer))]
        take_day = f"{bbb.year}/{format(bbb.month,'02')}/{format(bbb.day,'02')}"
        for i in range(len(test_answer)):
            if submit_answer[i] == test_answer[i]:
                correct.append(i+1)
                sum1 = sum1+jumsu[i]
            else:
                incorrect.append(i+1)
        if sum(jumsu)==sum1:
            st.header(f'참 잘 했습니다. 시험고유번호 :blue[{test_num}]의 점수는 :red[{sum1}점] 입니다.')
        else:
            st.header(f'시험고유번호 :blue[{test_num}]의 점수는 :red[{sum1}점] 입니다.')
            st.header(f'틀린 문항의 번호는 :green[{incorrect}]입니다.')
            st.header(f'풀이 소요시간은 :orange[{round(timestamp2-timestamp11,2)}]초 입니다.')

        csv_file = 'take_exam_online.csv'
        if os.path.exists(csv_file):
            # read from file
            ddf = pd.read_csv(csv_file, index_col=False)
        else:
            # create empty dataframe with the right columns & dtypes
            data_dict2={'학생이름':[],'학생HP':[],'시험고유번호':[],'시험명':[],'점수':[],'학생답':[],'맞은문항':[],'틀린문항':[],'문항별응시시간(초)':[],'총응시시간(초)':[],'응시일':[],'응시번호':[]}
            ddf = pd.DataFrame(data_dict2)

        ddf.loc[len(ddf['학생이름'])] = [stu_name,0,test_num,testname,sum1,str(submit_answer),str(correct),str(incorrect),str(timelist),sum(timelist),take_day,0]
        st.dataframe(ddf)
        ddf.to_csv(csv_file, index=False)
        csv = convert_df(ddf)
       
except:
    pass
try:
    through_pass = st.text_input('*:blue[download password]를 입력하세요')
    
    if through_pass == 'asdffdsa':
        st.write(through_pass == 'asdffdsa')
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='take_exam_online.csv',
            mime='text/csv')
    else:
        pass
except:
    pass
#     st.write("???")
# ddf = pd.DataFrame(
#     {'time': np.array([]).astype('datetime64[ns]'),
#      'Primary Air Flow Rate': np.array([], dtype=np.float64),
#      'Primary Air Temperature': np.array([], dtype=np.float64),
#      'Reference Air Temperature': np.array([], dtype=np.float64),
#      }
# )

# st.write('before')
# st.dataframe(results_option1)

# with st.form('input_form'):
#     qavalue = st.number_input('Primary Air Flow Rate')
#     travalue = st.number_input('Primary Air Temperature')
#     trvalue = st.number_input('Reference Air Temperature')
#     clickSubmit = st.form_submit_button('Submit')

# if clickSubmit:
#     timestamp = datetime.datetime.now()
#     results_option1.loc[len(results_option1)] = [timestamp, qavalue, travalue, trvalue]
#     results_option1.to_csv(csv_file, index=False)
#     st.write('after')
#     st.dataframe(results_option1)
# else:
#     st.markdown("Please submit to save")
