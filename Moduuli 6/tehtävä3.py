def gallonat_litroiksi(gallonat):
    return gallonat*3.785
while True:
    gallonat = float(input("anna gallonamäärä:"))
    if gallonat < 0:
        break
    litrat = gallonat_litroiksi(gallonat)
    print("litroina", litrat)