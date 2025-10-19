# -*- coding: utf-8 -*-
from fastq_final import FastqReader
import matplotlib.pyplot as plt

def main():
    print(" ДЕМОНСТРАЦИЯ FASTQ АНАЛИЗАТОРА")
    print("=" * 50)
    
    # Создаем тестовые данные
    print("\n1.  СОЗДАЕМ ТЕСТОВЫЙ FASTQ ФАЙЛ...")
    test_data = """@read1
GGGTGATGGCCGCTGCCGATGGCGTCAAATCCCACC
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIII9IG9IC
@read2
GTTCAGGGATACGACGTTTGTATTTTAAGAATCTGA
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII6IBI
@read3
GTTTCTGCAGCTGGTGGTGAATGGGAAGAGGTTCAA
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII8
@read4
ATGGTAGTTGGGTTGGCAGACTTTGGTGACTGCAGG
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII6II
@read5
CAGCTCGTATGCCGTCTTCTGCTTGAAAAAAAAAAA
+
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII5II
"""
    
    with open("demo.fastq", "w", encoding='utf-8') as f:
        f.write(test_data)
    print("    Файл 'demo.fastq' создан!")
    
    # Инициализируем анализатор
    print("\n2.  ИНИЦИАЛИЗИРУЕМ FASTQ АНАЛИЗАТОР...")
    analyzer = FastqReader("demo.fastq")
    print("    Анализатор готов!")
    
    # Показываем статистику
    print("\n3.  СТАТИСТИКА ДАННЫХ:")
    count = analyzer.get_sequence_count()
    avg_len = analyzer.get_average_length()
    print(f"   • Количество последовательностей: {count}")
    print(f"   • Средняя длина: {avg_len:.2f} bp")
    print(f"   • Общий объем данных: {count * avg_len:.0f} bp")
    
    # Демонстрируем отдельные методы
    print("\n4.  ДЕТАЛЬНЫЙ АНАЛИЗ:")
    sequences = analyzer._read_fastq_chunks()
    first_read = next(sequences)
    print(f"   • Первая последовательность: {first_read[1][:20]}...")
    print(f"   • ID первого рида: {first_read[0]}")
    print(f"   • Длина первого рида: {len(first_read[1])} bp")
    
    # Генерируем графики
    print("\n5.  ГЕНЕРАЦИЯ ГРАФИКОВ КАЧЕСТВА:")
    print("   • Per Base Sequence Quality...")
    analyzer.plot_per_base_quality("demo_quality.png")
    
    print("   • Per Base Sequence Content...")
    analyzer.plot_per_base_content("demo_content.png")
    
    print("   • Sequence Length Distribution...")
    analyzer.plot_sequence_length_distribution("demo_length.png")
    
    # Или все сразу:
    # analyzer.generate_all_plots()
    
    print("\n6. ВОЗМОЖНОСТИ АНАЛИЗАТОРА:")
    print("    Оптимизация памяти через генераторы")
    print("    Статистика по последовательностям") 
    print("    3 типа графиков качества")
    print("    Работа с большими файлами")
    print("    Поддержка русского языка")
    
    print("\n" + "=" * 50)
    print(" ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА!")
    print(" Проверь созданные файлы:")
    print("   • demo_quality.png")
    print("   • demo_content.png")
    print("   • demo_length.png")
    print("\n Для анализа своих данных:")
    print("   analyzer = FastqReader('ваш_файл.fastq')")
    print("   analyzer.generate_all_plots()")

if __name__ == "__main__":
    main()