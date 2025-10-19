class Vcfreader:
    def __init__(self, filename):
        self.filename = filename
        self.header = []
        self.columns = []
        self.variants = []

    def read(self):
        with open(self.filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('##'):
                    self.header.append(line)
                elif line.startswith('#CHROM'):
                    self.columns = line.lstrip('#').split('\t')
                else:
                    fields = line.split('\t')
                    variant = dict(zip(self.columns, fields))
                    variant['POS'] = int(variant['POS'])
                    variant['QUAL'] = float(variant['QUAL']) if variant['QUAL'] != '.' else 0.0
                    self.variants.append(variant)
                    yield variant

    def get_header(self):
        return self.header

    def filter_by_quality(self, minqual):
        return (v for v in self.variants if v['QUAL'] >= minqual)

    def variants_in_region(self, chrom, start, end):
        return (v for v in self.variants if v['#CHROM'] == chrom and start <= v['POS'] <= end)
