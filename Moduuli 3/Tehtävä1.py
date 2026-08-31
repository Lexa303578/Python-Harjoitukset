kuha = float(input("anna kuhan pituus:"))

if kuha < 37:
    alamitta=37-kuha
    kuha_vastaus=37-alamitta
    print(f"kuha on {alamitta}cm alamittainen, laske veteen")
else :
    print("kuha on hyvänmittainen")