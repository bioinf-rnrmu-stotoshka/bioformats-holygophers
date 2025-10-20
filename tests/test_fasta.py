"""
Tests for FASTA module.
Simple tests that don't require external files.
"""

import os
import sys
import tempfile

# Добавляем src в путь чтобы импортировать твои модули
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

from formats.fasta import FastaProcessor, count_sequences_fasta, average_length_fasta

def create_test_fasta(content: str) -> str:
    """Создает временный FASTA файл для тестов."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.fasta', delete=False) as f:
        f.write(content)
        return f.name


class TestFastaProcessor:
    """Тесты для FastaProcessor."""

    def test_sequence_count(self):
        """Тест подсчета последовательностей."""
        fasta_content = """>seq1
ATCG
>seq2
GGGCCC
>seq3
AAA"""

        test_file = create_test_fasta(fasta_content)
        try:
            processor = FastaProcessor(test_file)
            assert processor.get_sequence_count() == 3, "Должно быть 3 последовательности"
            print("test_sequence_count: Ты прошел мою проверку!")
        finally:
            os.unlink(test_file)

    def test_average_length(self):
        """Тест расчета средней длины."""
        fasta_content = """>seq1
ATCG
>seq2
GGGCCC
>seq3
AAA"""

        test_file = create_test_fasta(fasta_content)
        try:
            processor = FastaProcessor(test_file)
            # (4 + 6 + 3) / 3 = 4.33
            avg_len = processor.get_average_length()
            assert abs(avg_len - 4.33) < 0.1, f"Средняя длина должна быть ~4.33, получилось {avg_len}"
            print("test_average_length: Ты прошел мою проверку!")
        finally:
            os.unlink(test_file)

    def test_validate_format(self):
        """Тест валидации FASTA формата."""
        # Правильный FASTA
        good_fasta = """>seq1
ATCG"""
        good_file = create_test_fasta(good_fasta)

        # Неправильный FASTA
        bad_fasta = """NOT_A_HEADER
ATCG"""
        bad_file = create_test_fasta(bad_fasta)

        try:
            processor_good = FastaProcessor(good_file)
            processor_bad = FastaProcessor(bad_file)

            assert processor_good.validate_format() == True, "Правильный FASTA должен валидироваться"
            assert processor_bad.validate_format() == False, "Неправильный FASTA не должен валидироваться"
            print("test_validate_format: Неплохо, ты справился!")
        finally:
            os.unlink(good_file)
            os.unlink(bad_file)


def test_utility_functions():
    """Тест вспомогательных функций."""
    fasta_content = """>seq1
ATCG
>seq2
GGGCCC"""

    test_file = create_test_fasta(fasta_content)
    try:
        count = count_sequences_fasta(test_file)
        avg_len = average_length_fasta(test_file)

        assert count == 2, "count_sequences_fasta должен вернуть 2"
        assert avg_len == 5.0, "average_length_fasta должен вернуть 5.0"
        print("test_utility_functions: А ты не такой уж и дурень!")
    finally:
        os.unlink(test_file)


def run_all_tests():
    """Запускает все тесты."""
    print("ЗАПУСК ТЕСТОВ FASTA МОДУЛЯ: ПОЛЕТЕЛИ!")
    print("=" * 40)

    tester = TestFastaProcessor()
    tester.test_sequence_count()
    tester.test_average_length()
    tester.test_validate_format()
    test_utility_functions()

    print("=" * 40)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ! (На наше общее удивление, ха)")


if __name__ == "__main__":
    run_all_tests()