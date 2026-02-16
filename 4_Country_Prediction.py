@st.cache_resource
def train_models():
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    df = pd.read_csv("data/data.csv")
    models = {}
    X = df[["Year"]]

    for country in df.columns[1:]:
        y = df[country]
        model = LinearRegression()
        model.fit(X, y)
        models[country] = model

    return models

models = train_models()
