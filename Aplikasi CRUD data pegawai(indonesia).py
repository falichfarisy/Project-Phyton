#list pegawai
id_pegawai = [123, 234, 345, 456, 567]
nama_pegawai = ['arif', 'alvian', 'irvan', 'peo', 'paiz banget']
nomor_hp = [74839, 3275, 982130, 32019, 493021]
pegawai= [id_pegawai, nama_pegawai, nomor_hp]

def create():
    try:
        print (f"Masukkan id, nama, dan nomor HP anda(contoh): , {id_pegawai[0], nama_pegawai[0], nomor_hp[0]}")
        id_pegawai_baru = int(input("Masukkan ID pegawai baru: "))
        nama_pegawai_baru = (input("Masukkan Nama pegawai baru: "))
        nomor_hp_baru = int(input("Masukkan Nomor Telepon Pegawai baru: "))
        
        id_pegawai.append(id_pegawai_baru)
        nama_pegawai.append(nama_pegawai_baru)
        nomor_hp.append(nomor_hp_baru)
        print (f"Pegawai baru telah ditambahkan: {id_pegawai_baru, nama_pegawai_baru, nomor_hp_baru}")
    except ValueError:
        print ("Input tidak valid, pastikan ID dan Nomor telepon berupa angka.")

def read():
    cari_id_pegawai = int(input ("Cari pegawai berdasarkan ID: "))
    if cari_id_pegawai in id_pegawai:
        posisi = id_pegawai.index(cari_id_pegawai)
        print (f"ID {cari_id_pegawai} anda terletak pada urutan ke-{posisi + 1}.")
        print ({id_pegawai[posisi], nama_pegawai[posisi], nomor_hp[posisi]})
    else:
        print (f"Id {cari_id_pegawai} tidak ditemukan dalam list.")

def update():
    cari_id_pegawai = int(input ("Cari pegawai berdasarkan id: "))
    if cari_id_pegawai in id_pegawai:
        posisi = id_pegawai.index(cari_id_pegawai)
        print({id_pegawai [posisi], nama_pegawai [posisi], nomor_hp [posisi]})
        if input ("Apakah anda ingin mengubah data (y/t): ").lower() == "y":
            id_pegawai_baru = int(input("ID pegawai baru: "))
            nama_pegawai_baru = input ("nama pegawai baru: ")
            nomor_hp_baru = int(input ("Nomor Telepon baru: "))

            id_pegawai[posisi] = id_pegawai_baru
            nama_pegawai[posisi] = nama_pegawai_baru
            nomor_hp[posisi] = nomor_hp_baru
            print (f"data telah diubah menjadi {id_pegawai, nama_pegawai, nomor_hp}")
        else:
            print ("Data tidak diubah")
    else:
        print (f"Id {cari_id_pegawai} tidak ditemukan dalam list.")

    
def delete():
    cari_id_pegawai = int(input ("Cari pegawai berdasarkan id: "))
    if cari_id_pegawai in id_pegawai:
        posisi = id_pegawai.index(cari_id_pegawai)
        print({id_pegawai[posisi], nama_pegawai[posisi], nomor_hp[posisi]})
        if input("Apakah anda ingin menghapus data?(y/t): ").lower() == "y":
            del (id_pegawai[posisi], nama_pegawai[posisi], nomor_hp[posisi])
            print(f"Data telah diubah menjadi {id_pegawai, nama_pegawai, nomor_hp}")
        else:
            print("Data tidak diubah")
    else: 
        print (f"ID {cari_id_pegawai} tidak ditemukan dalam list.")

print("1. Create")
print("2. Read")
print("3. Update")
print("4. Delete")

try:
    pilihan = int(input("Pilih opsi berikut [1/2/3/4]: "))
    if pilihan == 1:
        print (create())
    elif pilihan == 2:
        print (read())
    elif pilihan == 3:
        print (update())
    elif pilihan == 4:
        print (delete())
    else:
        print ("pilihan tidak valid")
except ValueError:
    print ("Pesan tidak dikenal")