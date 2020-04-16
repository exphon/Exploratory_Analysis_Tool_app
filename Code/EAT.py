from ExploratoryAnalysis import ExploratoryAnalysis
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():

    st.title('Exploratory Analysis Tool')

    st.info('''Welcome to the Exploratory Analysis Tool. This is a simple application to getting basic information and quick data visualization for generic csv files. 
                Keep in mind that it is not a complete tool and very large files will reduce application performance.
                If you find a bug or want to help improve this application, the source code is on the link on the left side.''')

    def GetFile():
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file is not None:
            return(pd.read_csv(uploaded_file))

    df = GetFile()
    
    try:

        EA = ExploratoryAnalysis(df)
        st.success('File successfully uploaded!')


        st.sidebar.title('EAT - Menu')

        st.title('Dataframe basic informations')

        st.sidebar.subheader('Basica exploratory analysis options')
        if st.sidebar.checkbox('Basic informations'):

            if st.sidebar.checkbox('Head'):
                st.subheader('Dataframe head:')
                st.write(df.head())

            if st.sidebar.checkbox('Describe'):
                st.subheader('Dataframe description:')
                st.write(df.describe())

            if st.sidebar.checkbox('Info'):
                st.subheader('Dataframe informations:')
                st.text(EA.info())

            if st.sidebar.checkbox('Isnull'):
                st.subheader('Null occurrences')
                st.write(df.isnull().sum())

            if st.sidebar.checkbox('Unique values and frequency'):
                col = st.sidebar.selectbox('Choose a column for see unique values',EA.columns)
                st.subheader('Unique values and frequency')
                st.write(EA.info2(col))


        st.title('Dataframe plots')
        
        st.sidebar.subheader('Data visualization options')
        if st.sidebar.checkbox('Graphics'):

            if st.sidebar.checkbox('Count Plot'):
                st.subheader('Count Plot')
                column_count_plot = st.sidebar.selectbox("Choose a column to plot count",EA.columns)
                hue_opt = st.sidebar.selectbox("Optional categorical variables (countplot hue)",EA.columns.insert(0,None))
                if st.checkbox('Plot Countplot'):
                    fig = EA.CountPlot(column_count_plot, hue_opt)
                    st.pyplot()

            if st.sidebar.checkbox('Distribution Plot'):
                st.subheader('Distribution Plot')
                column_dist_plot = st.sidebar.selectbox("Choose a column to plot distribution (only numerical)",EA.numerical_columns)
                if st.checkbox('Plot Distplot'):
                    fig = EA.DistPlot(column_dist_plot)
                    st.pyplot()
            
            if st.sidebar.checkbox('Heatmap Correlation'):
                st.subheader('Heatmap Correlation Plot')
                fig = EA.HeatMapCorr()
                st.pyplot()

            if st.sidebar.checkbox('Boxplot'):
                st.subheader('Boxplot')
                column_box_plot_X = st.sidebar.selectbox("X (Choose a column):",EA.columns.insert(0,None))
                column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical):",EA.numerical_columns)
                hue_box_opt = st.sidebar.selectbox("Optional categorical variables (boxplot hue)",EA.columns.insert(0,None))
                if st.checkbox('Plot Boxplot'):
                    fig = EA.BoxPlot(column_box_plot_X, column_box_plot_Y, hue_box_opt)
                    st.pyplot()

            if st.sidebar.checkbox('Pairplot'):
                st.subheader('Pairplot')
                hue_pp_opt = st.sidebar.selectbox("Optional categorical variables (pairplot hue)",EA.columns.insert(0,None))
                st.info("This action may take a while.")
                if st.checkbox('Plot Pairplot'):
                    fig = EA.PairPlot(hue_pp_opt)
                    st.pyplot()
    
    
    #except Exception as e:
        #st.write(e)
    except:
        st.error('Upload a csv file to get started.')
        


    st.sidebar.subheader('Brief tutorial about how this application works')
    if st.sidebar.checkbox("Brief tutorial video"):
        st.sidebar.video("https://www.youtube.com/watch?v=Kzd_LCP2m_c")


    st.sidebar.markdown("**Help me to improve this application. See the source code below. Follow me!**")
    st.sidebar.markdown("[Source code](https://github.com/rafaelloni/EAT_app)")
    st.sidebar.markdown("**About the author:**")
    st.sidebar.markdown("[Rafael Loni](https://www.linkedin.com/in/rafael-loni/)")
    st.sidebar.markdown(" ` Version 0.0.1 ` ")

if __name__ == "__main__":
    main()