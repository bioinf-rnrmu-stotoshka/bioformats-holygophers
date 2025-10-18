[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/I6I1ViQv)
# Bioinformatics Cool - FASTA Module

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://python.org)

Универсальный процессор для биологических форматов файлов. Данный репозиторий содержит модуль для работы с FASTA файлами.

## О проекте

Bioinformatics Cool - это набор инструментов для обработки биологических данных, разработанный в рамках учебного проекта.

### Поддерживаемые форматы

-  FASTA - анализ последовательностей
-  FASTQ - анализ чтений
-  SAM - анализ выравниваний
-  VCF - анализ вариантов

## Быстрый старт

### Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/your-username/bioinformatics-toolkit
cd bioinformatics-toolkit

# (Опционально) Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# или
venv\Scripts\activate     # Windows

```
### Демонстрация

```bash
# Запустите демонстрационную программу FASTA
python examples/demo_fasta.py
```

### Тестирование

```bash
# Запустите тесты FASTA модуля
python tests/test_fasta.py
```

## Использование

### Командная строка

```bash
# Быстрый подсчет последовательностей
python -c "from src.formats.fasta import count_sequences_fasta; print(count_sequences_fasta('file.fasta'))"

# Быстрое получение средней длины
python -c "from src.formats.fasta import average_length_fasta; print(average_length_fasta('file.fasta'))"
```

### Python API

```python
from src.formats.fasta import FastaProcessor

# Создание процессора
processor = FastaProcessor("sequences.fasta")

# Основная статистика
stats = processor.get_statistics()
print(f"Количество последовательностей: {stats['sequence_count']}")
print(f"Средняя длина: {stats['average_length']:.2f} bp")
print(f"Общая длина: {stats['total_length']} bp")

# Итерация по последовательностям
for header, sequence in processor.sequence_generator():
    print(f"{header}: {len(sequence)} bp")

# Фильтрация по длине
filtered_sequences = processor.filter_sequences(min_length=100, max_length=1000)
print(f"Найдено {len(filtered_sequences)} последовательностей от 100 до 1000 bp")
```

## Структура проекта

```
bioinformatics-toolkit/
├── src/                    # Исходный код
│   └── formats/
│       ├── fasta.py       # FASTA процессор
│       ├── fastq.py       # FASTQ процессор (в разработке)
│       ├── sam.py         # SAM процессор (в разработке)
│       └── vcf.py         # VCF процессор (в разработке)
├── tests/                  # Тесты
│   └── test_fasta.py      # Тесты FASTA модуля
├── examples/               # Демонстрационные программы
│   └── demo_fasta.py      # Демо FASTA
├── docs/                   # Документация
│   └── source/
│       ├── conf.py        # Настройки Sphinx
│       ├── index.rst      # Главная страница
│       ├── modules.rst    # Документация модулей
│       └── usage.rst      # Инструкции по использованию
├── README.md              # Этот файл
├── requirements.txt       # Зависимости
└── .gitignore            # Игнорируемые файлы Git
```

## Документация

### Генерация документации

```bash
cd docs
sphinx-build -b html source build
```

Откройте `docs/build/index.html` в браузере для просмотра документации.

### Онлайн документация

Документация включает:
- API reference всех классов и методов
- Примеры использования
- Руководство по разработке

## Тестирование

Проект включает комплексные тесты:

```bash
# Запуск всех тестов
python tests/test_fasta.py

# Тестирование отдельных компонентов
python -c "from tests.test_fasta import TestFastaProcessor; t = TestFastaProcessor(); t.test_sequence_count()"
```

## Команда разработки

- Горожанкина П. - разработка FASTQ модуля
- Зубрилина А. - разработка SAM и VCF модуля
- Калион В. - разработка FASTA модуля, документация
