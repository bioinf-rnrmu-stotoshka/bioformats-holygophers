from vcf.py import Vcfreader

def demo_vcf():
    vcffile = "example.vcf"
    reader = Vcfreader(vcffile)

    print("=== Заголовки VCF файла ===")
    for _ in reader.read():
        pass
    for line in reader.getheader():
        print(line)

    print("\n=== Варианты с качеством >= 30 ===")
    filtered = reader.filterbyquality(30)
    for var in filtered:
        print(f"{var['#CHROM']}:{var['POS']} {var['REF']}->{var['ALT']} QUAL={var['QUAL']}")

    chrom = 'chr1'
    start, end = 100000, 200000
    print(f"\n=== Варианты на {chrom} в диапазоне {start}-{end} ===")
    in_region = reader.variantsinregion(chrom, start, end)
    for var in in_region:
        print(f"{var['#CHROM']}:{var['POS']} {var['REF']}->{var['ALT']}")
