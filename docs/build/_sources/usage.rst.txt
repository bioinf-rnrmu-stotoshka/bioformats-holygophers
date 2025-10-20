Usage Guide
===========

Command Line Interface
----------------------

Basic usage::

    python examples/demo_fasta.py

Python API
----------

FASTA Example
~~~~~~~~~~~~~

.. code-block:: python

    from src.formats.fasta import FastaProcessor
    
    # Create processor
    processor = FastaProcessor("sequences.fasta")
    
    # Get statistics
    stats = processor.get_statistics()
    print(f"Sequence count: {stats['sequence_count']}")
    print(f"Average length: {stats['average_length']:.2f}")
    
    # Iterate through sequences
    for header, sequence in processor.sequence_generator():
        print(f"Header: {header}, Length: {len(sequence)}")

FASTQ Example
~~~~~~~~~~~~~

Базовое использование
^^^^^^^^^^^^^^^^^^^^^

Анализ FASTQ файла и генерация всех графиков качества:

.. code-block:: python

   from src.formats.fastq import FastqProcessor
   
   # Создание анализатора
   analyzer = FastqProcessor("sequencing_data.fastq")
   
   # Получение базовой статистики
   count = analyzer.get_sequence_count()
   avg_length = analyzer.get_average_length()
   
   print(f"Количество последовательностей: {count}")
   print(f"Средняя длина: {avg_length:.2f} bp")
   
   # Генерация всех графиков качества
   analyzer.generate_all_plots()

Работа с большими файлами
^^^^^^^^^^^^^^^^^^^^^^^^^

Использование генераторов для обработки больших FASTQ файлов:

.. code-block:: python

   from src.formats.fastq import FastqProcessor
   
   # Анализатор автоматически использует генераторы
   # для оптимизации памяти (O(1) для статистики)
   analyzer = FastqProcessor("large_sequencing.fastq")
   
   # Статистика рассчитывается потоково
   # без загрузки всего файла в память
   print(f"Общее количество ридов: {analyzer.get_sequence_count():,}")
   
   # Графики строятся с агрегацией данных
   analyzer.plot_per_base_quality("large_file_quality.png")

Индивидуальная генерация графиков
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Создание отдельных графиков качества:

.. code-block:: python

   from fastq_final import FastqReader
   
   analyzer = FastqReader("data.fastq")
   
   # Только график качества по позициям
   analyzer.plot_per_base_quality("my_quality_plot.png")
   
   # Только содержание нуклеотидов
   analyzer.plot_per_base_content("nucleotide_content.png")
   
   # Только распределение длин
   analyzer.plot_sequence_length_distribution("length_dist.png")

Демонстрационный пример
^^^^^^^^^^^^^^^^^^^^^^^

Полный пример с созданием тестовых данных:

.. code-block:: python

   from src.formats.fastq import FastqProcessor
   
   # Создание тестового FASTQ файла
   test_data = '''@read1
   ATCGATCGATCGATCGATCG
   +
   IIIIIIIIIIIIIIIIIIII
   @read2
   GCTAGCTAGCTAGCTAGCTA
   +
   JJJJJJJJJJJJJJJJJJJ'''
   
   with open("test.fastq", "w") as f:
       f.write(test_data)
   
   # Анализ
   analyzer = FastqProcessor("test.fastq")
   analyzer.generate_all_plots()
   
   print("Анализ завершен! Проверьте PNG файлы.")

Интеграция в конвейеры обработки
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Использование в биоинформатических пайплайнах:

.. code-block:: python

   from src.formats.fastq import FastqProcessor
   import pandas as pd
   
   def quality_control_pipeline(fastq_file, output_prefix):
       '''Пайплайн контроля качества'''
       
       # Анализ FASTQ
       analyzer = FastqProcessor(fastq_file)
       
       # Сбор статистики
       stats = {
           'file': fastq_file,
           'total_sequences': analyzer.get_sequence_count(),
           'average_length': analyzer.get_average_length(),
           'total_bp': analyzer.get_sequence_count() * analyzer.get_average_length()
       }
       
       # Генерация отчетов
       analyzer.generate_all_plots()
       
       return stats
   
   # Использование в пайплайне
   results = quality_control_pipeline("experiment.fastq", "qc_report")
   print(f"Результаты QC: {results}")

SAM Example
~~~~~~~~~~~

.. code-block:: python

    from src.formats.sam import SamProcessor
    
    # Create processor
    processor = SamProcessor("alignments.sam")
    
    # Get alignment statistics
    alignment_stats = processor.get_alignment_stats()
    print(f"Mapping rate: {alignment_stats['mapping_rate']:.2%}")
    
    # Parse CIGAR strings
    for read in processor.read_generator():
        print(f"Read: {read['name']}, CIGAR: {read['cigar']}")

VCF Example
~~~~~~~~~~~

.. code-block:: python

    from src.formats.vcf import VcfProcessor
    
    # Create processor
    processor = VcfProcessor("variants.vcf")
    
    # Get variant statistics
    variant_stats = processor.get_variant_stats()
    print(f"Total variants: {variant_stats['variant_count']}")
    
    # Filter by quality
    high_quality_variants = processor.filter_by_quality(min_qual=30)
    print(f"High-quality variants: {len(high_quality_variants)}")