# ambil input dari user
nama = input("Nama: " )
umur = input("Umur: ")
alamat = input("Alamat: ")
# format text
text = "Nama : {}\nUmur: {}\nAlamatn: {}\n".format(nama, umur, alamat)
# buka file untuk ditulis
file_bio = open("biodata.txt", "a")
# tulis text file
file_bio.write(text)
#tutup file
file_bio.close()