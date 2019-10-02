import Library as library

def combine_data(filename=None, ulasan=None, output_path=None):
    df = library.pd.read_csv(filename, encoding="ISO-8859-1")

    du = library.pd.DataFrame(data=ulasan, columns=["ulasan"])
    df = df[["objek", "ulasan", "label"]]

    df[["ulasan"]] = du
    # untuk save dataframe ke file
    df.to_csv(output_path)

    return df