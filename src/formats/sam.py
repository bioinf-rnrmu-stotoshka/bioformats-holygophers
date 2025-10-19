class Samreader:
    def __init__(self, filename):
        self.filename = filename
        self.header = {}
        self.levels = []

    def read(self):
        with open(self.filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('@'):
                    obj = line[1:3]
                    if obj not in self.header:
                        self.header[obj] = []
                    self.header[obj].append(line)
                else:
                    fields = line.split('\t')
                    if len(fields) < 11:
                        continue
                    level = {
                        'QNAME': fields[0],
                        'FLAG': int(fields[1]),
                        'RNAME': fields[2],
                        'POS': int(fields[3]),
                        'MAPQ': int(fields[4]),
                        'CIGAR': fields[5],
                        'SEQ': fields[9],
                        'QUAL': fields[10]
                    }
                    self.levels.append(level)
                    yield level

    def getheader(self):
        return self.header

    def filterlevels(self, flagmask):
        return (lvl for lvl in self.levels if (lvl['FLAG'] & flagmask) == flagmask)

    def countlevelsperchrom(self):
        counts = {}
        for lvl in self.levels:
            chrom = lvl['RNAME']
            counts[chrom] = counts.get(chrom, 0) + 1
        return counts
