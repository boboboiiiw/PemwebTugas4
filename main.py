# Cara 1: Import seluruh modul
import math_operations as mo

# Cara 2: Import fungsi spesifik
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin, PI

def main():
    print("=== PROGRAM PERHITUNGAN MATEMATIKA ===")
    
    # Menggunakan fungsi dari modul dengan alias 'mo'
    print("\n1. Perhitungan Geometri:")
    print(f"Luas persegi (sisi=5): {mo.luas_persegi(5)}")
    print(f"Keliling persegi panjang (6x4): {mo.keliling_persegi_panjang(6, 4)}")
    print(f"Luas lingkaran (jari-jari=7): {mo.luas_lingkaran(7):.2f}")
    
    # Menggunakan fungsi yang diimport langsung
    print("\n2. Konversi Suhu:")
    print(f"25°C ke Fahrenheit: {celsius_ke_fahrenheit(25):.2f}°F")
    print(f"25°C ke Kelvin: {celsius_ke_kelvin(25):.2f}K")
    
    # Menggunakan konstanta
    print("\n3. Contoh penggunaan konstanta:")
    print(f"Nilai PI: {PI}")
    print(f"Keliling lingkaran (jari-jari=10): {2 * PI * 10:.2f}")
    
    # Contoh tambahan
    print("\n4. Contoh lain:")
    print(f"100°F ke Celsius: {mo.fahrenheit_ke_celsius(100):.2f}°C")
    print(f"Luas persegi panjang (8x3): {mo.luas_persegi_panjang(8, 3)}")

if __name__ == "__main__":
    main()
