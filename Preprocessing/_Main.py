import Library as library

fileall = 'Data/dataset.csv'
data = library.pr.preprocessing(input_path=fileall)
#clean_data  = library.load_data.combine_data(filename=fileall, ulasan=list_ulasan, output_path='Data/clean_data.csv')

# Print("Hasil Preprocessing")
# save clean data to csv
data.to_csv('Data/clean_data kecil.csv', index=False) # ini yaa kalo mau di save ke csv, tinggal run lagi aja
print(data)
