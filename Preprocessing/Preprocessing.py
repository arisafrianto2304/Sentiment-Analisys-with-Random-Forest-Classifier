import Library as library

def preprocessing(input_path=None):  # , stopword=stopword, stemmer=stemmer):
    factori = library.StemmerFactory()
    stemmer = factori.create_stemmer()

    factory = library.StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()

    tokenizer = library.RegexpTokenizer(r'\w+')

    arr_praproses = list()
    df = library.pd.read_csv(input_path, encoding='"ISO-8859-1"')

    lobject = df["objek"].values.tolist() #list object
    lulasan = df["ulasan"].values.tolist() #list ulasan
    llabel  = df["label"].values.tolist() #list label

    for ulasan in lulasan:
        lowcase_word = ulasan.lower()  # case folding lowcase data perbaris
        remove_num = library.re.sub(r'\d+', '', lowcase_word)# un comment number
        stopw = stopword.remove(remove_num)  # uncomment jika pakai stopword removal
        stemming = stemmer.stem(stopw)  # uncomment jika pakai stemming
        tokens = tokenizer.tokenize(stemming)  # Tokenisasi Kalimat, tergantung proses terakhirnya, stemming atau stopword atau hanya casefolding
        output = list()
        for kata in tokens:
            output.append(kata)  # proses stemming per-kata dalam 1 kalimat
        # sentence = " ".join(output) + ''
        arr_praproses.append(output)  # tampung kalimat hasil stemm ke arr_praproses

    df = library.pd.DataFrame({"objek":lobject, "ulasan": arr_praproses, "label": llabel})
    return df
