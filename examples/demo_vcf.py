from vcf.py import Vcfreader

def demo_vcf_pandas():
    vcf_path = "C:/Users/Asus/Desktop/test_vcf.vcf"
    reader = Vcfreader(vcf_path)
    reader.read()

    print("VCF Заголовки:")
    for line in reader.get_header():
        print(line)

    print("\nВсе варианты:")
    print(reader.df[[reader.df.columns[0], 'POS', 'REF', 'ALT', 'QUAL', 'FILTER']])

    print("\nФильтрация по качеству (QUAL >= 0):")
    filtered = reader.filter_by_quality(0)
    print(filtered[[reader.df.columns[0], 'POS', 'REF', 'ALT', 'QUAL']])

    chrom = "20"
    start, end = 1000000, 2000000
    print(f"\nВарианты на хромосоме {chrom} в диапазоне {start}-{end}:")
    region = reader.variants_in_region(chrom, start, end)
    print(region[[region.columns[0], 'POS', 'REF', 'ALT', 'QUAL']])


if __name__ == "__main__":
    demo_vcf_pandas()
