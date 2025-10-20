import pandas as pd

class Vcfreader:
    """
    Класс для чтения и фильтрации данных из VCF файла.

    Атрибуты:
        filename (str): Имя файла VCF.
        header_lines (list): Список строк заголовка файла (начинается с '##').
        df (pandas.DataFrame): Таблица данных вариантов из VCF.

    Методы:
        read(): Считывает VCF файл, загружает заголовок и данные в DataFrame.
        get_header(): Возвращает список строк заголовка VCF файла.
        filter_by_quality(min_qual): Фильтрует варианты по минимальному значению качества.
        variants_in_region(chrom, start, end): Возвращает варианты из указанного регионa.
    """

    def __init__(self, filename):
        """
        Инициализирует объект с именем файла.

        Args:
            filename (str): Путь к VCF файлу.
        """
        self.filename = filename
        self.header_lines = []
        self.df = None

    def read(self):
        """
        Считывает VCF файл.

        Загружает строки заголовка, начинающиеся с '##', 
        и затем считывает данные вариаций после строки с колонками '#CHROM'.
        Преобразует 'POS' в int, 'QUAL' в числовой тип с заменой ошибок на NaN.
        """
        with open(self.filename, 'r') as f:
            header = []
            for line in f:
                if line.startswith('##'):
                    header.append(line.strip())
                elif line.startswith('#CHROM'):
                    columns = line.strip()[1:].split('\t')
                    break
            self.df = pd.read_csv(
                self.filename,
                comment='#',
                sep='\t',
                names=columns,
                dtype={columns[0]: str}
            )
            self.header_lines = header

            self.df['POS'] = self.df['POS'].astype(int)
            self.df['QUAL'] = pd.to_numeric(self.df['QUAL'], errors='coerce')

    def get_header(self):
        """
        Возвращает список строк заголовка VCF файла.

        Returns:
            list: Заголовочные строки (начинающиеся с '##').
        """
        return self.header_lines

    def filter_by_quality(self, min_qual):
        """
        Фильтрует варианты по минимальному значению качества (QUAL).

        Args:
            min_qual (float): Минимальное значение качества для фильтрации.

        Returns:
            pandas.DataFrame: Отфильтрованные варианты с QUAL >= min_qual.
        """
        return self.df[self.df['QUAL'] >= min_qual]

    def variants_in_region(self, chrom, start, end):
        """
        Возвращает варианты, находящиеся в указанном хромосоме и диапазоне позиций.

        Args:
            chrom (str): Имя хромосомы.
            start (int): Начальная позиция региона (включительно).
            end (int): Конечная позиция региона (включительно).

        Returns:
            pandas.DataFrame: Варианты, расположенные в указанном регионе.
        """
        region_df = self.df[
            (self.df[self.df.columns[0]] == chrom) &
            (self.df['POS'] >= start) &
            (self.df['POS'] <= end)
        ]
        return region_df
    

'''ДЕМОНСТРАЦИЯ'''

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
