class Segitiga:
    def _init_(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def luas_segitiga(self):
        print((self.alas*self.tinggi)/2)

class Balok:
    def _init_(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume_balok(self):
        print(self.panjang*self.lebar*self.tinggi)

Segitiga = Segitiga(
    alas = 10,
    tinggi = 5
)

Balok = Balok(
    panjang = 10,
    lebar = 5,
    tinggi = 2
)

Segitiga.luas_segitiga()
Balok.volume_balok()