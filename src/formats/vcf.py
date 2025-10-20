import pandas as pd

class Vcfreader:
    def __init__(self, filename):
        self.filename = filename
        self.header_lines = []
        self.df = None

    def read(self):
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
            self.df['QUAL'] = pd.to_numeric(self.df['QUAL'], errors='coerce')  # . заменяем на NaN

    def get_header(self):
        return self.header_lines

    def filter_by_quality(self, min_qual):
        return self.df[self.df['QUAL'] >= min_qual]

    def variants_in_region(self, chrom, start, end):
        region_df = self.df[(self.df[self.df.columns[0]] == chrom) & (self.df['POS'] >= start) & (self.df['POS'] <= end)]
        return region_df
