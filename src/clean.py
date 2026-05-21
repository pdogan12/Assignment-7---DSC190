import pandas as pd
from pathlib import Path

VALID_EVENT_TYPES = {"click", "view", "scroll", "purchase"}

INPUT = Path("data/raw/events.csv")
OUTPUT = Path("data/clean/events.csv")

def main():
    df = pd.read_csv(INPUT)

    df = df.dropna()

    df["event_type"] = df["event_type"].str.lower()
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
    df = df.dropna(subset=["duration_seconds"])
    df = df[df["duration_seconds"] > 0]

    df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed")
    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    print(f"clean: {len(df)} rows written to {OUTPUT}")

if __name__ == "__main__":
    main()
