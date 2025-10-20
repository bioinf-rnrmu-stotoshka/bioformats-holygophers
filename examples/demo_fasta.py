#!/usr/bin/env python3
"""
ДЕМОНСТРАЦИОННАЯ ПРОГРАММА для FASTA модуля

Показывает все возможности работы с FASTA файлами.
Запусти: python demo_fasta.py
"""

import os
import sys
from pathlib import Path

# Добавляем src в путь для импорта
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from formats.fasta import FastaProcessor, count_sequences_fasta, average_length_fasta


def create_demo_fasta_file():
    """Создает демонстрационный FASTA файл."""
    demo_content = """>NC_000001.11 Homo sapiens chromosome 1, GRCh38.p14 Primary Assembly
ACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTG
ACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTGACTG
>NC_000002.12 Homo sapiens chromosome 2, GRCh38.p14 Primary Assembly
GGATCCGGATCCGGATCCGGATCCGGATCCGGATCCGGATCCGGATCCGGATCCGGATCCGGAT
CCGGATCCGGATCCGGATCC
>NP_001345678.1 transcription factor p65 [Homo sapiens]
MKQLVKETLERQLTQKQITKQEISPLKKTKKKQKkQDEDFKLFRKTFNLPEELERLLGILGNRF
SIDDDSLGRLISRLLQELNGIN
>short_sequence
ATCG
>very_long_sequence
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
"""

    demo_file = "demo_sequences.fasta"
    with open(demo_file, 'w', encoding='utf-8') as f:
        f.write(demo_content)

    return demo_file


def main():
    """Основная демонстрационная функция."""
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ FASTA МОДУЛЯ: ВЖУУУУУУХ")
    print("=" * 60)

    # 1. Создаем демо файл
    print("\n1. СОЗДАЕМ ДЕМОСТРАЦИОННЫЙ FASTA ФАЙЛ. Жди давай, ЖДИ.")
    demo_file = create_demo_fasta_file()
    print(f"   Создан (к сожалению) файл: {demo_file}")

    try:
        # 2. Создаем процессор
        print("\n2. 🔧 СОЗДАЕМ FASTA ПРОЦЕССОР...")
        processor = FastaProcessor(demo_file)
        print("Процессор создан успешно! Мда..огорчение.")

        # 3. Проверяем валидацию
        print("\n3.ПРОВЕРКА ФОРМАТА FASTA... (Не прошел!)")
        is_valid = processor.validate_format()
        print(f" Формат файла (не)корректный: {is_valid}")

        # 4. Основная статистика
        print("\n4. ОСНОВНАЯ СТАТИСТИКА:")
        stats = processor.get_statistics()
        print(f"   • Количество последовательностей: {stats['sequence_count']}")
        print(f"   • Общая длина: {stats['total_length']} bp")
        print(f"   • Средняя длина: {stats['average_length']:.2f} bp")
        print(f"   • Минимальная длина: {stats['min_length']} bp")
        print(f"   • Максимальная длина: {stats['max_length']} bp")

        # 5. Демонстрация итерации
        print("\n5. ИТЕРАЦИЯ ПО ПОСЛЕДОВАТЕЛЬНОСТЯМ:")
        print("   Первые 3 последовательности:")
        for i, (header, sequence) in enumerate(processor.sequence_generator()):
            if i >= 3:  # Показываем только первые 3
                break
            short_header = header[:50] + "..." if len(header) > 50 else header
            print(f"     {i + 1}. {short_header}")
            print(f"        Длина: {len(sequence)} bp")
            print(f"        Начало: {sequence[:30]}...")

        # 6. Фильтрация последовательностей
        print("\n6. ФИЛЬТРАЦИЯ ПО ДЛИНЕ:")
        filtered = processor.filter_sequences(min_length=50, max_length=200)
        print(f"   • Последовательностей от 50 до 200 bp: {len(filtered)}")

        # 7. Вспомогательные функции
        print("\n7. ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ:")
        quick_count = count_sequences_fasta(demo_file)
        quick_avg = average_length_fasta(demo_file)
        print(f"   • Быстрый подсчет: {quick_count} последовательностей")
        print(f"   • Быстрая средняя длина: {quick_avg:.2f} bp")

        # 8. Создание отфильтрованного файла
        print("\n8. СОЗДАНИЕ ОТФИЛЬТРОВАННОГО ФАЙЛА. А я не создам-а я не создам! Бебебебе")
        output_file = "filtered_demo.fasta"
        written_count = processor.write_filtered_fasta(output_file, min_length=10)
        print(f" Черт...Создан файл '{output_file}' с {written_count} последовательностями")

        print("\n" + "=" * 60)
        print("ДЕМОНСТРАЦИЯ (НЕ)УСПЕШНО ЗАВЕРШЕНА!")
        print("=" * 60)

    finally:
        # Удаляем временные файлы
        if os.path.exists(demo_file):
            os.remove(demo_file)
            print(f"\n Удален временный файл: {demo_file}")
        if os.path.exists("filtered_demo.fasta"):
            os.remove("filtered_demo.fasta")
            print(f" Удален временный файл: filtered_demo.fasta")


if __name__ == "__main__":
    main()