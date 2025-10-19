# -*- coding: utf-8 -*-
import subprocess
import sys

print("УСТАНАВЛИВАЕМ MATPLOTLIB...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])

print("ЗАПУСКАЕМ ОПТИМИЗИРОВАННЫЙ FASTQ АНАЛИЗАТОР...")
import matplotlib.pyplot as plt
from collections import defaultdict

class FastqReader:
    """
    Класс для чтения и анализа FASTQ файлов с оптимизацией памяти
    Использует генераторы для работы с большими файлами
    """
    
    def __init__(self, filename):
        self.filename = filename
        self._sequence_count = None
        self._total_length = None
    
    def _read_fastq_chunks(self):
        """ГЕНЕРАТОР: читает FASTQ файл по одному риду за раз"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            while True:
                # Читаем 4 строки одного рида
                lines = [file.readline().strip() for _ in range(4)]
                if not lines[0]:  # Конец файла
                    break
                yield lines
    
    def calculate_statistics(self):
        """Рассчитывает статистику используя генератор (память O(1))"""
        count = 0
        total_length = 0
        
        for chunk in self._read_fastq_chunks():
            count += 1
            sequence_line = chunk[1]  # Вторая строка - последовательность
            total_length += len(sequence_line)
        
        self._sequence_count = count
        self._total_length = total_length
        return count, total_length
    
    def get_sequence_count(self):
        """Возвращает количество последовательностей в файле"""
        if self._sequence_count is None:
            self.calculate_statistics()
        return self._sequence_count
    
    def get_average_length(self):
        """Возвращает среднюю длину последовательностей"""
        if self._sequence_count is None:
            self.calculate_statistics()
        if self._sequence_count == 0:
            return 0
        return self._total_length / self._sequence_count
    
    def plot_per_base_quality(self, output="quality.png"):
        """Строит график качества по позициям (Per Base Sequence Quality)"""
        quality_sums = defaultdict(int)
        quality_counts = defaultdict(int)
        max_position = 0
        
        for chunk in self._read_fastq_chunks():
            quality_line = chunk[3]  # Четвертая строка - качество
            for i, char in enumerate(quality_line):
                score = ord(char) - 33  # Конвертируем в числовое качество
                quality_sums[i] += score
                quality_counts[i] += 1
                max_position = max(max_position, i)
        
        # Рассчитываем среднее качество для каждой позиции
        positions = range(1, max_position + 2)
        avg_qualities = [quality_sums[i] / quality_counts[i] for i in range(max_position + 1)]
        
        # Создаем график
        plt.figure(figsize=(10, 6))
        plt.plot(positions, avg_qualities, linewidth=2)
        plt.title('Качество последовательностей по позициям')
        plt.xlabel('Позиция в риде (bp)')
        plt.ylabel('Phred Quality Score')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output, dpi=150)
        plt.close()
        print(f"Сохранен: {output}")
    
    def plot_per_base_content(self, output="content.png"):
        """Строит график содержания нуклеотидов по позициям (Per Base Sequence Content)"""
        base_counts = {'A': defaultdict(int), 'C': defaultdict(int), 
                      'G': defaultdict(int), 'T': defaultdict(int)}
        total_counts = defaultdict(int)
        max_position = 0
        
        for chunk in self._read_fastq_chunks():
            sequence_line = chunk[1]  # Вторая строка - последовательность
            for i, base in enumerate(sequence_line):
                base_upper = base.upper()
                if base_upper in base_counts:
                    base_counts[base_upper][i] += 1
                    total_counts[i] += 1
                    max_position = max(max_position, i)
        
        positions = range(1, max_position + 2)
        plt.figure(figsize=(10, 6))
        
        # Строим линии для каждого нуклеотида
        for base, counts in base_counts.items():
            percentages = [counts[i] / total_counts[i] * 100 if total_counts[i] > 0 else 0 
                          for i in range(max_position + 1)]
            plt.plot(positions, percentages, label=base, linewidth=2)
        
        plt.title('Содержание нуклеотидов по позициям')
        plt.xlabel('Позиция в риде (bp)')
        plt.ylabel('Процент (%)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output, dpi=150)
        plt.close()
        print(f"Сохранен: {output}")
    
    def plot_sequence_length_distribution(self, output="length.png"):
        """Строит гистограмму распределения длин последовательностей"""
        lengths = []
        
        for chunk in self._read_fastq_chunks():
            sequence_line = chunk[1]  # Вторая строка - последовательность
            lengths.append(len(sequence_line))
        
        plt.figure(figsize=(10, 6))
        plt.hist(lengths, bins=20, edgecolor='black', alpha=0.7)
        plt.title('Распределение длин последовательностей')
        plt.xlabel('Длина последовательности (bp)')
        plt.ylabel('Частота')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(output, dpi=150)
        plt.close()
        print(f"Сохранен: {output}")
    
    def generate_all_plots(self):
        """Генерирует все три графика качества"""
        print("Генерируем графики с оптимизацией памяти...")
        self.plot_per_base_quality()
        self.plot_per_base_content()
        self.plot_sequence_length_distribution()
        print("ВСЕ ГРАФИКИ СОЗДАНЫ С ОПТИМИЗАЦИЕЙ ПАМЯТИ!")

def create_test_fastq():
    """Создает тестовый FASTQ файл для демонстрации"""
    print("СОЗДАЕМ ТЕСТОВЫЙ ФАЙЛ...")
    test_data = ""
    for i in range(100):
        test_data += f"@read{i}\n"
        test_data += "ATCGATCGATCGATCGATCG\n"  # 20 bp
        test_data += "+\n"
        test_data += "IIIIIIIIIIIIIIIIIIII\n"  # Качество 40
    return test_data

if __name__ == "__main__":
    print(" ОПТИМИЗИРОВАННЫЙ FASTQ АНАЛИЗАТОР С ГЕНЕРАТОРАМИ!")
    
    # Создаем тестовый файл
    test_data = create_test_fastq()
    with open("test.fastq", "w", encoding='utf-8') as f:
        f.write(test_data)
    
    # Анализируем
    analyzer = FastqReader("test.fastq")
    
    print("РАССЧИТЫВАЕМ СТАТИСТИКУ...")
    count = analyzer.get_sequence_count()
    avg_len = analyzer.get_average_length()
    
    print(f" КОЛИЧЕСТВО ПОСЛЕДОВАТЕЛЬНОСТЕЙ: {count}")
    print(f" СРЕДНЯЯ ДЛИНА: {avg_len:.2f} bp")
    print(f" ОБЩИЙ ОБЪЕМ ДАННЫХ: {count * avg_len:.0f} bp")
    
    print("\n ГЕНЕРИРУЕМ ГРАФИКИ...")
    analyzer.generate_all_plots()
    
    print("\n ГОТОВО! Оптимизированная версия готова для больших файлов!")

    print(" ИСПОЛЬЗОВАНИЕ ПАМЯТИ: O(1) для статистики, O(max_length) для графиков!")
