[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/I6I1ViQv)
# Bioinformatics Cool

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://python.org)

Унифицированный процессор для биологических форматов файлов: FASTA, FASTQ, SAM, VCF.

## Возможности

### Модуль FASTA
- Подсчет последовательностей и статистика
- Расчет средней длины последовательностей
- Эффективные генераторы для больших файлов
- Валидация формата и фильтрация
- Поддержка сжатых файлов (.gz)

### Модуль FASTQ
- Анализ качества чтений
- Статистика последовательностей
- Обработка quality scores
- Фильтрация по порогам качества

### Модуль SAM
- Статистика выравниваний
- Анализ маппинга чтений
- Парсинг CIGAR строк
- Поддержка BAM файлов

### Модуль VCF
- Анализ вариантов (variant calling)
- Обработка генотипов
- Фильтрация по метрикам качества
- Поддержка аннотаций

## Установка

```bash
git clone https://github.com/bioinf-rnrmu-stotoshka/bioformats-holygophers
cd bioformats-holygophers
```

## Быстрый старт

### Анализ FASTA
```bash
python examples/demo_fasta.py
python tests/test_fasta.py
```

### Анализ FASTQ
```bash
python examples/demo_fastq.py
python tests/test_fastq.py
```
**Анализ качества чтений:**

![График качества FASTQ чтений](images/fastq-quality.png)

**Содержание нуклеотидов:**

![Содержание нуклеотидов по позициям](images/fastq-content.png)

**Распределение длин последовательностей:**

![Распределение длин ридов](images/fastq-length.png)
```

### Анализ SAM
```bash
python examples/demo_sam.py
python tests/test_sam.py
```

### Анализ VCF
```bash
python examples/demo_vcf.py
python tests/test_vcf.py
```

## Использование

### Python API

#### FASTA
```python
from src.formats.fasta import FastaProcessor
processor = FastaProcessor("sequences.fasta")
stats = processor.get_statistics()
print(f"Количество последовательностей: {stats['sequence_count']}")
```

#### FASTQ
```python
from src.formats.fastq import FastqProcessor
processor = FastqProcessor("reads.fastq")
quality_stats = processor.get_quality_stats()
```

#### SAM
```python
from src.formats.sam import SamProcessor
processor = SamProcessor("alignments.sam")
alignment_stats = processor.get_alignment_stats()
```

#### VCF
```python
from src.formats.vcf import VcfProcessor
processor = VcfProcessor("variants.vcf")
variant_stats = processor.get_variant_stats()
```

## Структура проекта

```
bioformats-holygophers/
├── src/
│   └── formats/
│       ├── fasta.py
│       ├── fastq.py
│       ├── sam.py
│       └── vcf.py
├── tests/
│   ├── test_fasta.py
│   ├── test_fastq.py
│   ├── test_sam.py
│   └── test_vcf.py
├── examples/
│   ├── demo_fasta.py
│   ├── demo_fastq.py
│   ├── demo_sam.py
│   └── demo_vcf.py
├── docs/
│   └── source/
│       ├── conf.py
│       ├── index.rst
│       ├── modules.rst
│       └── usage.rst
├── README.md
├── requirements.txt
└── .gitignore
```

## Документация

Для генерации документации:

```bash
cd docs
sphinx-build -b html source build
```

Откройте `docs/build/index.html` в браузере.

## Тестирование

Запуск всех тестов:

```bash
python -m pytest tests/
```

Или отдельных модулей:

```bash
python tests/test_fasta.py
python tests/test_fastq.py
python tests/test_sam.py
python tests/test_vcf.py
```
---
## Команда разработки

- Горожанкина П. - разработка FASTQ модуля
- Зубрилина А. - разработка SAM и VCF модуля
- Калион В. - разработка FASTA модуля, документация
