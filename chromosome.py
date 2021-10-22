from array import array


class Chromosome:
    def __init__(self, location, start, end):
        self.location = int(location)
        self.indexes = (start, end)

    def __init__(self, location, start, end):
        self.location = int(location)
        self.indexes = (start, end)

    def __str__(self):
        return self.location + ": " + self.indexes[0] + "-" + self.indexes[1]


    def get_indexes(self):
        return self.indexes


    def get_location(self):
        return self.location


    def get_length(self):
        return self.indexes[1] - self.indexes[0]


    def get_common_ndx(self, chromosome):
        chrom_start = chromosome.get_indexes[0]
        chrom_end = chromosome.get_indexes[1]
        if self.indexes[1] >= chrom_start and self.indexes[0] <= chrom_end:  # if there is overlap calcultate
            return (min(chrom_end, self.indexes[1]) - max(chrom_start, self.indexes[0])) / max(self.get_length(),
                                                                                               chromosome.get_length())
        return 0


    def has_common_ndx(self, chromosome):
        chrom_start = chromosome.get_indexes()[0]
        chrom_end = chromosome.get_indexes()[1]
        if self.indexes[1] >= chrom_start and self.indexes[0] <= chrom_end:  # if there is overlap calcultate
            return True
        return False


    def is_same_chromosome(self, chromosome):
        return self.location is chromosome.get_location()
