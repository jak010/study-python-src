import pandas as pd

df = pd.DataFrame([1, 2, 3, 4, 5], columns=["a"])

new_df = pd.DataFrame([], columns=["a"])
for _ in range(1, 20_000):
    insert_row = pd.DataFrame([1], columns=["a"])
    new_df = pd.concat([new_df, insert_row], axis=0, ignore_index=True)

df = pd.concat([df, new_df], axis=0)
df.to_csv("./test.csv", index=False)
