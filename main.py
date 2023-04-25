import streamlit as st
import pandas as pd
st.write("hello!~~bye!!!")
df = pd.DataFrame(pd.read_csv('./exam_data.csv'))
df1 = df['정답']

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
