import streamlit as st
import pandas as pd

df=pd.read_csv("spotify final datasets.csv")

st.title('Song Recommendation App')
st.subheader("Hello User")

st.text('List of the Songs in the App')
df['name'].values


popu = pd.DataFrame(df.groupby('name')['popularity'].mean())
song_matrix = df.pivot_table(index = 'track_number', columns = 'name', values ='popularity')
song_matrix_2 = song_matrix.fillna(0)
popu.sort_values('popularity', ascending = False).head(10)
#abc = song_matrix_2["Tum To Nayan Ki Jyot Ho"]
selected_song_name = st.selectbox('Song Name', df['name'].values)
abc = song_matrix_2[selected_song_name]
similar_to_abc = song_matrix_2.corrwith(abc)
corr_abc = pd.DataFrame(similar_to_abc , columns=['corr'])
corr_abc.dropna(inplace=True)
corr_abc_2 = corr_abc.join(popu['popularity'])
#final_song = corr_abc_2[corr_abc_2['popularity']>30].sort_values(by='corr', ascending = True)
selected_song_popularity = st.selectbox('Popularity', df['popularity'].values)
final_song = corr_abc_2[corr_abc_2['popularity']>selected_song_popularity].sort_values(by='corr', ascending = False)
final = final_song.drop('corr', axis = 1)
final = final.head(50)


st.text('Selected Song Is')
st.write(selected_song_name)

st.text('Recommended Popular Songs based on the selected song with their popularity score : ')
st.write(final)



#if __name__=='__main__':
 #   main()
