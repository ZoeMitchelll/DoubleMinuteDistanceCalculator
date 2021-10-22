import itertools
from array import array

import chromosome


class DoubleMinute:
    def __init__(self, id, filename, chr, diagnosis):
        self.chromosomes = chr
        self.file = filename
        self.patient_id = str(id)
        self.diagnosis = bool(diagnosis)

    def __str__(self):
        return self.file + "has a length of " + str(len(chromosome))

    def get_file(self):
        return self.file

    def get_chromosomes(self):
        return self.chromosomes

    def get_patient_id(self):
        return self.patient_id

    def get_diagnosis(self):
        return self.diagnosis

    def get_chromosome_locations(self):
        all_chromo = []
        for chromosome in self.chromosomes.keys():
            all_chromo.append(chromosome.get_location())
        return set(all_chromo)

    def get_common_chr(self, dm):
        those_chromo = dm.get_chromosomes()
        locations = []
        dm_locations = []
        for c in self.chromosomes:
            locations.append(c.get_location())
        for c in those_chromo:
            dm_locations.append(c.get_location())
        [locations.remove(c) for c in locations if c not in dm_locations]
        if len(locations) == 0:
            return dict()
        overlapping_chr = dict.fromkeys(locations, [[], []])
        for c in self.chromosomes:
            if c.get_location() in locations:
                dm_chr = overlapping_chr[c.get_location()][0]
                dm_chr.append(c)
                overlapping_chr[c.get_location()][0] = dm_chr
        for c in those_chromo:
            if c.get_location() in locations:
                dm_chr = overlapping_chr[c.get_location()][1]
                dm_chr.append(c)
                overlapping_chr[c.get_location()][1] = dm_chr
        return overlapping_chr #chromosomes in dm and self that are located in the same place as self

    def get_common_chr_ratio(self, dm):
        return 1 - (len(self.get_common_chr(dm))/max(len(self.chromosomes), len(dm.get_chromosomes())))

    def get_common_ndx_ratio(self, dm):
        overlapping_sum = 0
        same_chromo = 0
        for lists in self.get_common_chr(dm).values():
            chr_combos = itertools.combinations(lists[0], len(lists[1]))
            all_chr_combos = []
            for chr_list in chr_combos:
                current_combination = zip(chr_list, lists[1])
                all_chr_combos.extend(list(current_combination))
                for combo in all_chr_combos:
                    same_chromo = same_chromo+1
                    if combo[0].has_common_ndx(combo[1]):
                        overlapping_sum = overlapping_sum + 1
        if same_chromo == 0:
            return 1
        return overlapping_sum/same_chromo #returns ratio of overlap in simular chromosomes

    def get_distance(self, dm):
        if self.get_common_chr_ratio(dm) > 0:
            return (self.get_common_chr_ratio(dm) + self.get_common_ndx_ratio(dm))/2
        return 1
