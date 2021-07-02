import streamlit as st 
from funcitonality import * 

st.title('Simplify my text')
text = st.text_area(label = 'Enter your text here ',height= 600,value= """Over one year after its inception, the coronavirus disease-2019 (COVID-19) pandemic caused by severe acute respiratory syndrome coronavirus-2 (SARS-CoV-2) remains difficult to control despite the availability of several excellent vaccines. \n Progress in controlling the pandemic is slowed by the emergence of variants that appear to be more transmissible and more resistant to antibodies1,2. Here we report on a cohort of 63 COVID-19-convalescent individuals assessed at 1.3, 6.2 and 12 months after infection, 41% of whom also received mRNA vaccines3,4. \n In the absence of vaccination antibody reactivity to the receptor binding domain (RBD) of SARS-CoV-2, neutralizing activity and the number of RBD-specific memory B cells remain relatively stable from 6 to 12 months. \n Vaccination increases all components of the humoral response, and as expected, results in serum neutralizing activities against variants of concern that are comparable to or greater than neutralizing activity against the original Wuhan Hu-1 achieved by vaccination of naive individuals2,5-8.\n The mechanism underlying these broad-based responses involves ongoing antibody somatic mutation, memory B cell clonal turnover, and development of monoclonal antibodies that are exceptionally resistant to SARS-CoV-2 RBD mutations, including those found in variants of concern4,9. In addition, B cell clones expressing broad and potent antibodies are selectively retained in the repertoire over time and expand dramatically after vaccination. The data suggest that immunity in convalescent individuals will be very long lasting and that convalescent individuals who receive available mRNA vaccines will produce antibodies and memory B cells that should be protective against circulating SARS-CoV-2 variants.\n""")


if text != None:  
    array_of_text_scentences, labels = get_prediction(text)
    st.subheader('Your simplified text is')
    arr = list(zip(labels,array_of_text_scentences))
    st.write(arr)
    final = {}

    for i in range(len(arr)):
        x,y = arr[i]
        if x in final.keys(): 
            final[x].append(y)
        else:
            final[x] = [y]

    st.write(final)
    
    for lab,val in final.items():
        print(lab,val)
        st.header(f'# {lab}')
        for v in val:
            v = v.lower().replace('!@#$%^&*:",.<>\n',"")
            st.subheader(f'### {v}')
    # st.text_area(label='asdf',height = 600, value = array_of_text_scentences)
    # st.write(labels)