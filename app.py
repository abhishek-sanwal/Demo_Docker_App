import io
import pandas as pd
import numpy as np


def main():

    df = pd.DataFrame({"a": [1, 1, 2, 1, 2],
                       "b": [np.nan, 2.0, 3.0, 4.0, 5.0]})

    gb = df.groupby("a")
    print(gb.nth(n=1))


if __name__ == "__main__":
    main()