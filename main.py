import os

TEXT = "All afternoon the sun crossed the room, one slow inch at a time, and settled in the corner by the window. The dust hung in it, gold and unhurried. Nothing else moved. The light stayed a while longer, then went on, leaving the wall warm."

def main():
    assert 1 <= len(TEXT) <= 280, "entry must be 1-280 Unicode code points"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
