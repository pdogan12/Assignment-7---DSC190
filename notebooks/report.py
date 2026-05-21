import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, pd, plt


@app.cell
def __(pd):
    df = pd.read_csv("data/features/events.csv")
    df.head()
    return (df,)


@app.cell
def __(df, plt):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(df["duration_minutes"], bins=20, edgecolor="white", color="#378ADD")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of event durations")
    plt.tight_layout()
    fig
    return (fig, ax)
