# aie_recsys_cap
AIEdge Recommender System Capstone (June 2023 Cohort)



1. create a virtual env in the /streamlit folder
```
python -m venv .venv
```

2. activate the virtual env
```
source .venv/bin/activate
```

3. In the streamlit folder, pip install tensorflow and tensorflow-recommenders
```
pip install tensorflow
pip install tensorflow-recommenders
```

4. Run the streamlit app file 
app.py is input user_ID, output 10 game recs

app_e.py is input list of game appids, output 10 game recs

```
streamlit run app.py
streamlit run app_e.py
```

# Source of Datasets 
## (final cleaned dataset was a lowercase concatenated game name join between steam.csv and steam-200k.csv)

1. Nik Davis Dataset of 27,000 Steam games and their metadata

https://www.kaggle.com/datasets/nikdavis/steam-store-games


2. Tamber Dataset of 200,000 Steam user interactions (Play, Purchase)

https://www.kaggle.com/datasets/tamber/steam-video-games