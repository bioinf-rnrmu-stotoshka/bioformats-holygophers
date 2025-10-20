class Samreader:
    """
    Класс для чтения и анализа SAM-файлов (формат выравнивания последовательностей).

    Атрибуты:
        filename (str): Путь к SAM-файлу.
        header (dict): Заголовок SAM-файла в виде словаря, где ключ — двухбуквенный идентификатор,
                       значение — список строк заголовка.
        levels (list): Список выравниваний, каждое представлено словарём с ключами:
            'QNAME' (str): Имя прочтения.
            'FLAG' (int): Флаг выравнивания.
            'RNAME' (str): Имя ссылочного последовательности (хромосомы).
            'POS' (int): Позиция выравнивания.
            'MAPQ' (int): Качество сопоставления.
            'CIGAR' (str): CIGAR-строка (описание выравнивания).
            'SEQ' (str): Последовательность нуклеотидов.
            'QUAL' (str): Качество прочтения.

    Методы:
        __init__(filename):
            Инициализирует объект с именем файла и пустыми структурами для заголовка и выравниваний.

        read():
            Читает SAM-файл построчно.
            - Заголовки начинаются с '@' и группируются по двухсимвольному коду после '@'.
            - Выравнивания парсятся в словари и добавляются в атрибут levels.
            Возвращает генератор словарей для каждого выравнивания.

        getheader():
            Возвращает словарь заголовка SAM-файла.

        filterlevels(flagmask):
            Фильтрует выравнивания по битовой маске флага FLAG.
            Принимает целочисленную маску flagmask и возвращает генератор выравниваний,
            у которых (FLAG & flagmask) == flagmask.

        countlevelsperchrom():
            Подсчитывает количество выравниваний для каждой последовательности RNAME.
            Возвращает словарь {название_хромосомы: количество_выравниваний}.
    """
    def __init__(self, filename):
        self.filename = filename
        self.header = {}
        self.levels = []

    def read(self):
        with open(self.filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('@'):
                    obj = line[1:3]
                    if obj not in self.header:
                        self.header[obj] = []
                    self.header[obj].append(line)
                else:
                    fields = line.split('\t')
                    if len(fields) < 11:
                        continue
                    level = {
                        'QNAME': fields[0],
                        'FLAG': int(fields[1]),
                        'RNAME': fields[2],
                        'POS': int(fields[3]),
                        'MAPQ': int(fields[4]),
                        'CIGAR': fields[5],
                        'SEQ': fields[9],
                        'QUAL': fields[10]
                    }
                    self.levels.append(level)
                    yield level

    def getheader(self):
        return self.header

    def filterlevels(self, flagmask):
        return (lvl for lvl in self.levels if (lvl['FLAG'] & flagmask) == flagmask)

    def countlevelsperchrom(self):
        counts = {}
        for lvl in self.levels:
            chrom = lvl['RNAME']
            counts[chrom] = counts.get(chrom, 0) + 1
        return counts
    

'''ДЕМОНСТРАЦИЯ'''

def demosam():
    samfile = "C:/Users/Asus/Desktop/test_sam.sam"
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
