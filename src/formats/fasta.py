"""
FASTA format processor.
Integrated with common bioinformatics toolkit.
"""

from typing import Iterator, Tuple, Dict, Union, List
import os
import gzip


class BaseBioProcessor:
    """Abstract base class for all bioinformatics file processors."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.compressed = self._is_compressed(filepath)

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {filepath} not found")

    @staticmethod
    def _is_compressed(filepath: str) -> bool:
        """Check if file is gzip compressed."""
        return filepath.lower().endswith(('.gz', '.gzip'))

    def _open_file(self, mode: str = 'r'):
        """Open file with appropriate mode based on compression."""
        if self.compressed:
            return gzip.open(self.filepath, mode + 't', encoding='utf-8')
        else:
            return open(self.filepath, mode, encoding='utf-8')

    def get_statistics(self) -> dict:
        """Return format-specific statistics."""
        return {}

    def validate_format(self) -> bool:
        """Validate file format."""
        return True


class FastaProcessor(BaseBioProcessor):
    """
    FASTA format processor for sequence analysis.

    Features:
    - Memory-efficient sequence iteration
    - Sequence statistics and filtering
    - Support for compressed files
    - Standardized interface for toolkit integration

    Example:
        >>> processor = FastaProcessor("sequences.fasta")
        >>> count = processor.get_sequence_count()
        >>> print(f"Found {count} sequences")
    """

    def sequence_generator(self) -> Iterator[Tuple[str, str]]:
        """
        Generator yielding sequences from FASTA file.

        Yields:
            Tuple of (header, sequence)

        Example:
            >>> processor = FastaProcessor("test.fasta")
            >>> for header, sequence in processor.sequence_generator():
            ...     print(f"Header: {header}, Length: {len(sequence)}")
        """
        current_header = None
        current_sequence = []

        with self._open_file() as file:
            for line in file:
                line = line.strip()

                if line.startswith('>'):
                    if current_header is not None:
                        yield current_header, ''.join(current_sequence)

                    current_header = line[1:].strip()
                    current_sequence = []
                elif line:
                    current_sequence.append(line)

            if current_header is not None:
                yield current_header, ''.join(current_sequence)

    def get_statistics(self) -> Dict[str, Union[int, float]]:
        """
        Get comprehensive FASTA statistics.

        Returns:
            Dictionary with sequence count, length stats, etc.

        Example:
            >>> processor = FastaProcessor("test.fasta")
            >>> stats = processor.get_statistics()
            >>> print(f"Sequence count: {stats['sequence_count']}")
        """
        lengths = []
        total_length = 0
        sequence_count = 0

        for _, sequence in self.sequence_generator():
            seq_len = len(sequence)
            lengths.append(seq_len)
            total_length += seq_len
            sequence_count += 1

        if not lengths:
            return {
                'format': 'FASTA',
                'sequence_count': 0,
                'total_length': 0,
                'average_length': 0.0,
                'min_length': 0,
                'max_length': 0,
                'file_path': self.filepath
            }

        return {
            'format': 'FASTA',
            'sequence_count': sequence_count,
            'total_length': total_length,
            'average_length': total_length / sequence_count,
            'min_length': min(lengths),
            'max_length': max(lengths),
            'file_path': self.filepath
        }

    def validate_format(self) -> bool:
        """
        Validate FASTA file format.

        Returns:
            True if file appears to be valid FASTA

        Example:
            >>> processor = FastaProcessor("test.fasta")
            >>> is_valid = processor.validate_format()
            >>> print(f"File is valid FASTA: {is_valid}")
        """
        try:
            with self._open_file() as file:
                first_line = file.readline().strip()
                return first_line.startswith('>')
        except:
            return False

    def get_sequence_count(self) -> int:
        """
        Get total number of sequences in FASTA file.

        Returns:
            Number of sequences

        Example:
            >>> processor = FastaProcessor("sequences.fasta")
            >>> count = processor.get_sequence_count()
            >>> print(f"Total sequences: {count}")
        """
        count = 0
        for _, _ in self.sequence_generator():
            count += 1
        return count

    def get_average_length(self) -> float:
        """
        Get average sequence length in FASTA file.

        Returns:
            Average sequence length

        Example:
            >>> processor = FastaProcessor("sequences.fasta")
            >>> avg_len = processor.get_average_length()
            >>> print(f"Average length: {avg_len:.2f}")
        """
        stats = self.get_statistics()
        return stats['average_length']

    def filter_sequences(self, min_length: int = 0,
                         max_length: int = None) -> List[Tuple[str, str]]:
        """
        Filter sequences by length criteria.

        Args:
            min_length: Minimum sequence length (inclusive)
            max_length: Maximum sequence length (inclusive)

        Returns:
            List of (header, sequence) tuples that meet criteria

        Example:
            >>> processor = FastaProcessor("sequences.fasta")
            >>> filtered = processor.filter_sequences(min_length=100)
            >>> print(f"Found {len(filtered)} sequences longer than 100bp")
        """
        filtered = []
        for header, sequence in self.sequence_generator():
            seq_len = len(sequence)
            if seq_len >= min_length and (max_length is None or seq_len <= max_length):
                filtered.append((header, sequence))
        return filtered


# Utility functions for quick operations
def count_sequences_fasta(filepath: str) -> int:
    """
    Quick function to count sequences in FASTA file.

    Args:
        filepath: Path to FASTA file

    Returns:
        Number of sequences

    Example:
        >>> count = count_sequences_fasta("sequences.fasta")
        >>> print(f"Sequence count: {count}")
    """
    processor = FastaProcessor(filepath)
    return processor.get_sequence_count()


def average_length_fasta(filepath: str) -> float:
    """
    Quick function to get average sequence length.

    Args:
        filepath: Path to FASTA file

    Returns:
        Average sequence length

    Example:
        >>> avg_len = average_length_fasta("sequences.fasta")
        >>> print(f"Average length: {avg_len:.2f}")
    """
    processor = FastaProcessor(filepath)
    return processor.get_average_length()


if __name__ == "__main__":
    # Код который выполнится только при прямом запуске файла
    print("🔬 FASTA Processor - Direct Execution")
    
    # Создаем тестовые данные
    test_data = """>test_sequence_1
ATCGATCG
>test_sequence_2
GGGCCCAAA"""
    
    with open('test_direct.fasta', 'w') as f:
        f.write(test_data)
    
    # Тестируем наш класс
    processor = FastaProcessor('test_direct.fasta')
    stats = processor.get_statistics()
    print(f"Результат: {stats}")
