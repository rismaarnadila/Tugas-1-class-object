class Segitiga:
    def __init__ (self, T, i):
        self.T=T
        self.i=i
        
    def perhitungan1(self):
        for self.i in range(1, self.T+1):
            print((self.T-self.i)*"*")

    def perhitungan2(self):
        for self.i in range(1, self.T+1):
            print((self.T-self.i)*" "+(self.T)*"*")

Segitiga_terbalik = Segitiga(
    T=6,
    i=0
)
Segitiga_terbalik.perhitungan1()
print("================")
print("")
Segitiga_terbalik.perhitungan2()