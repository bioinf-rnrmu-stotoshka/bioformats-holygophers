from sam.py import Samreader

def demosam():
    samfile = "test_sam.sam"
    reader = Samreader(samfile)

    print("=== Заголовки SAM файла ===")
    for _ in reader.read():
        pass
    headers = reader.getheader()
    for htype, lines in headers.items():
        print(f"{htype}:")
        for line in lines:
            print("  ", line)

    print("\n=== Количество выравниваний по хромосомам ===")
    counts = reader.countlevelsperchrom()
    for chrom, count in counts.items():
        print(f"{chrom}: {count}")

    print("\n=== Выравнивания с флагом 0x4 (не выровнены) ===")
    unaligned = reader.filterlevels(0x4)
    for lvl in unaligned:
        print(f"{lvl['QNAME']} на {lvl['RNAME']} с флагом {lvl['FLAG']}")


if __name__ == "__main__":
    demosam()

