# Importing necessary Libraries:

import pandas as pd
import streamlit as st
import pickle


st.markdown("""
<style>

.stButton > button{
    width:100%;
    height:55px;
    font-size:22px;
    font-weight:bold;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)


# Step 2 : Page Configuration ::

st.set_page_config(
    page_title="Amazon Music Clustering",
    page_icon="🎵🎶",
    layout= "wide"
)

# ==========================================
# Custom CSS Styling:
# ==========================================
st.markdown("""
<style>

/* Main App Padding */
.main .block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

/* Rounded Success / Info Boxes */

div[data-testid="stAlert"]{
    border-radius:15px;
    border-left:5px solid #1DB954;
    box-shadow:0 8px 20px rgba(0,0,0,0.25);
}
            
            div[data-testid="stAlert"]{
    transition:0.3s;
}

div[data-testid="stAlert"]:hover{
    transform:translateY(-4px);
    box-shadow:0 12px 28px rgba(0,0,0,0.35);
}
/* Buttons */
.stButton > button{
    border-radius:12px;
    font-weight:600;
}


/* Sidebar */
section[data-testid="stSidebar"]{
    border-right:1px solid #2b2b2b;
    background:linear-gradient(180deg,#161b22,#111827);
}
/* Sidebar Buttons */

section[data-testid="stSidebar"] .stButton>button{
    background:#1f2937;
    border:1px solid #374151;
    color:white;
}

section[data-testid="stSidebar"] .stButton>button:hover{
    background:#16a34a;
}
            
            .stButton > button{
    width:100%;
    height:55px;
    border-radius:14px;
    background:#16a34a;
    color:white;
    font-size:18px;
    font-weight:700;
    border:none;
    transition:0.3s;
}

.stButton > button:hover{
    background:#22c55e;
    transform:scale(1.03);
}

</style>
""", unsafe_allow_html=True)


# Step 3: Title

st.title("🎵 Amazon Music Recommendation System")

st.caption("🎧 ML-Based Music Recommendation System using K-Means Clustering")

st.markdown("---")

# ==========================
# Sidebar
# ==========================

st.sidebar.title("🎵 Amazon Music")

st.sidebar.markdown("---")

st.sidebar.header("Project Details")

st.sidebar.write("**Algorithm :** K-Means Clustering")
st.sidebar.write("**Dataset :** Amazon Music")
st.sidebar.write("**Features :** 18 Audio Features")
st.sidebar.write("**Language :** Python")
st.sidebar.write("**Framework :** Streamlit")

st.sidebar.markdown("---")

st.sidebar.caption("Developed by")

st.sidebar.write("**Mukul Chakravorty**")

st.sidebar.write("Data Science & ML Engineer")

st.sidebar.markdown("---")

st.sidebar.success("ML Portfolio Project")

# ==========================

st.markdown("""
### Project Overview

Predict similar music categories using 18 audio features and the K-Means clustering algorithm.

Adjust the audio features below and click **Predict Cluster**
to identify the most suitable music category.
""")
st.markdown("---")
st.markdown("---")



st.header("🎵 Song Audio Features")

col1, col2 = st.columns(2)

with col1:
    danceability = st.slider("Danceability", 0.0, 1.0, 0.5)

with col2:
    energy = st.slider("Energy", 0.0, 1.0, 0.5)

with col1:
    acousticness = st.slider("Acousticness", 0.0, 1.0, 0.5)

with col2:
    valence = st.slider("Valence", 0.0, 1.0, 0.5)


with col1:
    tempo = st.number_input("Tempo", value=120.0)

with col2:
    popularity_songs = st.number_input("Popularity Songs", 0, 100, 50)


with col1:
    duration_ms = st.number_input("Duration (ms)", value=200000)

with col2:
    explicit = st.selectbox("Explicit", [0, 1])


with col1:
    key = st.slider("Key", 0, 11, 5)

with col2:
    loudness = st.slider("Loudness", -60.0, 5.0, -10.0)


with col1:
    mode = st.selectbox("Mode", [0, 1])

with col2:
    speechiness = st.slider("Speechiness", 0.0, 1.0, 0.05)


with col1:
    instrumentalness = st.slider("Instrumentalness", 0.0, 1.0, 0.0)

with col2:
    liveness = st.slider("Liveness", 0.0, 1.0, 0.2)


with col1:
    followers = st.number_input("Followers", value=100000)

with col2:
    popularity_artists = st.number_input("Popularity Artists", 0, 100, 50)


with col1:
    time_signature = st.slider("Time Signature", 1, 7, 4)

with col2:
    release_year = st.number_input("Release Year", 1900, 2030, 2020)





# Step 4: Loading the Dataset :

df = pd.read_csv("output/Amazon_Music_Clustered.csv")


# Dataset Preview:

st.markdown("---")


#st.subheader("Dataset Preview")

#st.dataframe(df.head())


# Step 5 : Loading the Model:

with open("output/kmeans_music_model.pkl","rb") as file:
    model = pickle.load(file)


# Step 6 : Final check :
#st.success("File Loaded Successfully")

col1, col2 = st.columns(2)

with col1:
    st.info("🎵 **Dataset**\n\nAmazon Music Songs")

with col2:
    st.info(" **Algorithm**\n\nK-Means Clustering")

col3, col4 = st.columns(2)

with col3:
    st.info("🎧 **Features**\n\n18 Audio Features")

with col4:
   st.info("🎯 **Output**\n\n4 Music Categories")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.subheader("🎵 Music Prediction")
        st.caption("Click below to generate your music recommendation.")

        if st.button("🎯 Predict Cluster"):
    
            input_data = [[
                popularity_songs,
                duration_ms,
                explicit,
                danceability,
                energy,
                key,
                loudness,
                mode,
                speechiness,
                acousticness,
                instrumentalness,
                liveness,
                valence,
                tempo,
                time_signature,
                followers,
                popularity_artists,
                release_year
        ]]

            prediction = model.predict(input_data)

            st.markdown("---")
            st.subheader("🎯 Prediction Result")

            st.caption("Your personalized music recommendation based on audio features")

            st.success("✅ Prediction Completed Successfully")

    

            cluster_names = {
                0: "🎵 Acoustic / Calm Songs",
                1: "🔥 High Energy Songs",
                2: "💃 Dance Party Songs",
                3: "🎧 Chill & Relax Songs"
}

            cluster_description = {
            0: "Relaxing, peaceful and acoustic songs ideal for studying, meditation and calm moods.",
            1: "High-energy songs suitable for gym workouts, running and motivation.",
            2: "Dance and party songs with strong rhythm for celebrations and events.",
            3: "Soft chill songs perfect for relaxing, travelling and late-night listening."
}
    

            st.success(f"🎵 Recommended Music Category\n\n{cluster_names[prediction[0]]}"
)

            st.caption(cluster_description[prediction[0]])


            st.markdown("---")

            st.markdown(
"""
<div style='text-align:center;color:#A9A9A9;font-size:14px;'>

Machine Learning Portfolio Project<br>
Python • Streamlit • Scikit-Learn

</div>
""",
unsafe_allow_html=True
)