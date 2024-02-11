import streamlit as st
import pandas as pd 
import plotly.express as px


df = pd.read_csv("cleaned_data.csv")
df['gdp_country'] = df['gdp_country'].str.strip().str.split('$').str[1].str.replace(',','').astype(float)


st.set_page_config(page_title='billionaires dashboard', layout='wide', page_icon="random")
st.title(":dollar: :rainbow[BILLIONAIRES STATISTICS DASHBOARD] :dollar:")
selected_option = st.sidebar.selectbox("select one", ['Country Wise','Overall Analysis','key Insights'])



if selected_option == 'Country Wise':
    # making bar graph of top 10 billionaires country wise
    st.subheader(":green[Top 10 billionaires country wise]")
    selected_country = st.selectbox("select country", df['countryOfCitizenship'].unique())
    a = df[df['countryOfCitizenship'] == selected_country][['finalWorth','personName']].head(10)
    fig = px.bar(data_frame=a, x='personName', y='finalWorth',
                 color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig, use_container_width=True)
    
    # ploting country on map 
    st.subheader(":green[Countries on map]")
    primary = st.selectbox("select primary parameter", ['population_country','gdp_country'])
    secondary = st.selectbox("select secondary parameter",['total_tax_rate_country','life_expectancy_country'])
    st.text("size represents primary parameter")
    st.text("color represents secondary parameter")
    fig4 = px.scatter_mapbox(df, lat='latitude_country', lon='longitude_country', size=primary, color=secondary,
                             hover_name='countryOfCitizenship',size_max=25, zoom=1, mapbox_style="carto-positron",
                             height=600, width=1000)
    st.plotly_chart(fig4, use_container_width=True)

    # no. of billionaired from each country
    st.subheader(":green[Number of billionaires from top 15 country]")
    fig7 = px.bar(data_frame=df, x=df['countryOfCitizenship'].value_counts().head(15).index,
       y=df['countryOfCitizenship'].value_counts().head(15).values,
       color_discrete_sequence=px.colors.qualitative.Antique)
    st.plotly_chart(fig7, use_container_width=True)
    
elif selected_option == 'Overall Analysis':
    
    # bar graph of no of billionaires industry wise
    st.subheader(":green[Number of billionaires industry wise]")
    fig3 = px.bar(x=df['industries'].value_counts().index, y=df['industries'].value_counts().values,
                  color_discrete_sequence=px.colors.qualitative.Alphabet)
    st.plotly_chart(fig3, use_container_width=True)  
    
    # histogram of age
    st.subheader(':green[Number of billionaires age wise]')
    fig5 = px.histogram(df['age'], nbins=18,color_discrete_sequence=['indianred'])
    st.plotly_chart(fig5)

    # top 10 Male and famale
    st.subheader(":green[Top 10 Male/Female billionaires]")
    selected = st.selectbox("select", ['M','F'])
    temp_df = df[df['gender'] == selected][['finalWorth','personName']].head(10)
    fig6 = px.bar(temp_df, x='personName',y='finalWorth',color_discrete_sequence=px.colors.qualitative.Dark2)
    st.plotly_chart(fig6,use_container_width=True)
    
    col1, col2 = st.columns(2)

    with col1:
        # pie chart of male female
        st.subheader(":green[percent of male female]")
        fig1 = px.pie(names=df['gender'].value_counts().index, values=df['gender'].value_counts().values,
                      hole=0.3, color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # pie chart of self made or family property
        st.subheader(":green[Self made]")
        fig2 = px.pie(names=df['selfMade'].value_counts().index, values=df['selfMade'].value_counts().values,
                       color_discrete_sequence=px.colors.qualitative.Bold)
        st.plotly_chart(fig2,use_container_width=True)    

elif selected_option == 'key Insights':
    st.markdown("Highest number of billionaires are from united states, china and india") 
    st.markdown("Highest number of billionaires are from finance and technology industry")  
    st.markdown("Most of the billionaires have age 55 to 70")  
    st.markdown("there are 87.6 % male and 12.4 % female billionaires")   
    st.markdown("70 % are selfmade billionaires and 30 % have family property") 
    st.markdown("Europian countries have highest life expectancy")