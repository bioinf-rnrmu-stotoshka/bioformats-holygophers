Bioinformatics Toolkit Documentation
====================================

Добро пожаловать в документацию нашего проекта!

.. toctree::
   :maxdepth: 2
   :caption: Содержание:
   
   modules
   usage

Быстрый старт
-------------

Установка::

    pip install -e .

Использование::

    from src.formats.fasta import FastaProcessor
    processor = FastaProcessor("sequences.fasta")
    print(processor.get_sequence_count())

Форматы
-------

Наш тулкит поддерживает:

- FASTA
- FASTQ
- SAM
- VCF

Команда разработки
------------------

- Виктория - FASTA модуль
- Полина - FASTQ модуль
- Анна - SAM модуль
- Анна - VCF модуль