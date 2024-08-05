# Bikesafe


## Set up 
1. If you do not have miniforge install it. You can follow the instructions from [here](https://biapol.github.io/blog/mara_lampert/getting_started_with_mambaforge_and_python/readme.html).
```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh -b -p "${HOME}/conda"
```

2. Change to the directory containing the code and create an environment
```bash
conda create -n bikeshare python=3.9 pip
conda activate bikeshare
pip install -r requirements.txt
``` 

3. Run the app
```
streamlit run BikeSafe.py
```




