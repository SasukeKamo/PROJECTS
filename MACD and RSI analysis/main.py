import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def strategia_rsi(data, okres_rsi=14, gorna_granica_rsi=70, dolna_granica_rsi=30):

    data['zmiana'] = data['Zamkniecie'].diff()  # obliczenie zmian cen
    data['zysk'] = data['zmiana'].apply(lambda x: x if x > 0 else 0)  # obliczenie zysków
    data['strata'] = -data['zmiana'].apply(lambda x: x if x < 0 else 0)  # obliczenie strat
    data['sredni_zysk'] = data['zysk'].rolling(window=okres_rsi).mean()  # obliczenie średniego zysku
    data['srednia_strata'] = data['strata'].rolling(window=okres_rsi).mean()  # obliczenie średniej straty
    data['rs'] = data['sredni_zysk'] / data['srednia_strata']  # obliczenie względnej siły
    data['rsi'] = 100 - (100 / (1 + data['rs']))  # obliczenie RSI


    kapital = 1000
    akcje = 0
    zysk_najlepszej = 0
    strata_najgorszej = 0

    for i in range(1, len(data)):
        if data['rsi'][i] > gorna_granica_rsi and data['rsi'][i - 1] <= gorna_granica_rsi:
            # sell
            if akcje > 0:
                kapital += akcje * data['Zamkniecie'][i]
                zysk_strata = ((data['Zamkniecie'][i] - data['Zamkniecie'][i - 1]) / data['Zamkniecie'][i - 1]) * 100
                if zysk_strata > zysk_najlepszej:
                    zysk_najlepszej = zysk_strata
                if zysk_strata < strata_najgorszej:
                    strata_najgorszej = zysk_strata
                akcje = 0
        elif data['rsi'][i] < dolna_granica_rsi and data['rsi'][i - 1] >= dolna_granica_rsi:
            # buy
            if kapital > 0:
                doKupna = kapital / data['Zamkniecie'][i]
                akcje += doKupna
                kapital -= doKupna * data['Zamkniecie'][i]

                
    print(f"Zysk najlepszej transakcji: {zysk_najlepszej:.2f}%")
    print(f"Strata najgorszej transakcji: {strata_najgorszej:.2f}%")
    if kapital > 1000:
        print(f"Udaloby sie zarobic! Kapital koncowy to: {kapital:.2f}")
    elif kapital > 0 and kapital < 1000:
        print(f"Przynajmniej bys nie zbankrutowal. Kapital koncowy to: {kapital:.2f}")
    else:
        print(f"Czy warto bylo szalec tak? Kapital koncowy to: {kapital:.2f}")


# Wczytanie danych z pliku CSV (Stooq.pl)
dane = pd.read_csv('dnp_d.csv')

dane['Data'] = pd.to_datetime(dane['Data'])

krotkaSredniaKroczaca = dane['Zamkniecie'].ewm(span=12, adjust=False).mean()
dlugaSredniaKroczaca = dane['Zamkniecie'].ewm(span=26, adjust=False).mean()

macd = krotkaSredniaKroczaca - dlugaSredniaKroczaca

signal = macd.ewm(span=9, adjust=False).mean()


histogram = macd - signal

kapital = 1000  # kapital poczatkowy
akcje = 0      

poprawne_przewidywania = 0
wszystkie_przewidywania = 0
zysk_najlepszej = 0
strata_najgorszej = 0

for i in range(1, len(dane)):
    # MACD przecina signal w gore, kupujemy akcje
    if macd[i] > signal[i] and macd[i-1] <= signal[i-1]:
        # doKupna = kapital / zamkniecia[i] -> jeśli wersja z liczeniem macd i signal bez zewnętrznych bibliotek
        doKupna = kapital / dane['Zamkniecie'][i]
        akcje += doKupna
        kapital -= doKupna * dane['Zamkniecie'][i]
        if dane['Zamkniecie'][i] > dane['Zamkniecie'][i-1]:
            poprawne_przewidywania += 1
        wszystkie_przewidywania += 1
    # MACD przecina signal w dol, sprzedajemy akcje
    elif macd[i] < signal[i] and macd[i-1] >= signal[i-1]:
        kapital += akcje * dane['Zamkniecie'][i]
        zysk_strata = ((dane['Zamkniecie'][i] - dane['Zamkniecie'][i-1])/dane['Zamkniecie'][i-1]) * 100
        if zysk_strata > zysk_najlepszej:
            zysk_najlepszej = zysk_strata
        if zysk_strata < strata_najgorszej:
            strata_najgorszej = zysk_strata
        akcje = 0
        if dane['Zamkniecie'][i] < dane['Zamkniecie'][i-1]:
            poprawne_przewidywania += 1
        wszystkie_przewidywania += 1

print("Strategia MACD: ")
print(f"Poprawne przewidywania: {poprawne_przewidywania}")
print(f"Wszystkie przewidywania: {wszystkie_przewidywania}")
print("Skutecznosc przewidywan: {:.2%}".format(poprawne_przewidywania / wszystkie_przewidywania))
print(f"Zysk najlepszej transakcji: {zysk_najlepszej:.2f}%")
print(f"Strata najgorszej transakcji: {strata_najgorszej:.2f}%")
if kapital > 1000:
    print(f"Udaloby sie zarobic! Kapital koncowy to: {kapital:.2f}")
elif kapital > 0 and kapital < 1000:
    print(f"Przynajmniej bys nie zbankrutowal. Kapital koncowy to: {kapital:.2f}")
else:
    print(f"Czy warto bylo szalec tak? Kapital koncowy to: {kapital:.2f}")

wartosc_kapitalu = (kapital*100)/1000
if wartosc_kapitalu > 100:
    wartosc_kapitalu = wartosc_kapitalu - 100
    wartosc_kapitalu = str(f"+{wartosc_kapitalu:.2f}")
else:
    wartosc_kapitalu = 100 - wartosc_kapitalu
    wartosc_kapitalu = str(f"-{wartosc_kapitalu:.2f}")
print(f"Procentowy zysk/strata: {wartosc_kapitalu}%")


obszar, poziom = plt.subplots(2, sharex=True, figsize=(12, 8))

# Wykres danych wejściowych
poziom[0].plot(dane['Data'], dane['Zamkniecie'], label='Close')
poziom[0].set_title('Cena akcji')
poziom[0].set_ylabel('PLN')
poziom[0].grid()

# Wykres MACD
poziom[1].plot(dane['Data'], macd, label='MACD')
poziom[1].plot(dane['Data'], signal, label='Signal')
poziom[1].set_title('Wykres MACD dla akcji Dino Polska SA')
poziom[1].set_ylabel('Wartosc MACD')
poziom[1].legend(loc='upper left')
poziom[1].grid()


#plt.savefig('MACD_DINOPL.png')
plt.show()

plt.figure(figsize=(12,8))
plt.plot(dane['Data'], macd, label='MACD')
plt.plot(dane['Data'], signal, label='Signal')
plt.bar(dane['Data'],histogram, color='green', label='Histogram')
plt.title('Wykres MACD z histogramem dla akcji Dino Polska SA')
plt.ylabel('Wartosc MACD')
plt.legend(loc='upper left')
#plt.savefig('DINOPL_HISTOGRAM.png')
plt.show()

# dodatkowa strategia
print("\n")
print("STRATEGIA RSI: ")
strategia_rsi(dane)

