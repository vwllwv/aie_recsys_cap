# aie_recsys_cap
AIEdge Recommender System Capstone (June 2023 Cohort)



1. create a virtual env in the /streamlit folder
```
python -m venv .venv
```

OR

```
conda create -n tf_recsys
```

2. activate the virtual env
```
source .venv/bin/activate
```

OR

```
conda activate tf_recsys
```

3. In the streamlit folder, pip install streamlit version 1.22, tensorflow and tensorflow-recommenders
```
pip install streamlit==1.22
pip install tensorflow==2.11.1
pip install tensorflow-recommenders
```

4. Test streamlit installation
```
streamlit hello
```
Quit the streamlit application if it runs OK.

5. Run the streamlit app file 
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


# requirements.txt
altair==4.2.2
protobuf==3.19.6
python==3.10.12
scann==1.2.9
streamlit==1.22.0
tensorflow==2.11.1
tensorflow-recommenders==0.7.3

## for running the notebooks
jupyter==1.0.0


