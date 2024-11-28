data_panen = {
    'lokasi1':{
        'nama_lokasi':'Kebun A',
        'hasil_panen':{
            'padi':1200,
            'jagung':800,
            'kedelai':500
        }
    },
    'lokasi2':{
        'nama_lokasi':'Kebun B',
        'hasil_panen':{
            'padi':1500,
            'jagung':900,
            'kedelai':450
        }
    },
    'lokasi3':{
        'nama_lokasi':'Kebun C',
        'hasil_panen':{
            'padi':1100,
            'jagung':750,
            'kedelai':600
        }
    },
    'lokasi4':{
        'nama_lokasi':'Kebun D',
        'hasil_panen':{
            'padi':1300,
            'jagung':850,
            'kedelai':550
        }
    },
    'lokasi5':{
        'nama_lokasi':'Kebun E',
        'hasil_panen':{
            'padi':1400,
            'jagung':950,
            'kedelai':480
        }
    }
}

# jawaban soal 1
# outputkan semua data yang ada
print('Jawaban Soal 1')
for key, value in data_panen.items():
    print(f'tempat = {key}')
    print(f'nama lokasi = {value["nama_lokasi"]}')
    print(f'Berikut adalah hasil Panen di {value["nama_lokasi"]}\n')

# jawaban soal 2
# outputkan hasil panen jagung di lokasi 2
print('Jawaban Soal 2')
print(f'hasil panen jagung di lokasi 2 adalah {data_panen["lokasi2"]["hasil_panen"]["jagung"]}\n')

# jawaban soal 3
# tampilkan nama lokasi dari lokasi 3
print('Jawaban Soal 3')
print(f'nama lokasi dari lokasi 3 adalah {data_panen["lokasi3"]["nama_lokasi"]}\n')