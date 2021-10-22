import os
from pprint import pprint

from chromosome import Chromosome
from doubleminute import DoubleMinute
from itertools import permutations

from patient import Patient


def read_bed_files():
    datapath = 'BEDfiles'
    datafiles = os.listdir(datapath)
    all_double_minutes = []
    for bam_file in datafiles:
        filepath = datapath + '/' + bam_file
        # uses TCGA encoding
        patient_id = bam_file.split(".bam")
        patient_id = patient_id[0].split("-")
        scan_status = patient_id[3]
        patient_id = patient_id[2]
        with open(filepath) as file:
            lines = file.readlines()
            diagnosis = scan_status.__contains__('01')
            chromosomes = []
            for line in lines:
                data = line.split("\t")
                chromo = Chromosome(data[0], data[1], data[2])
                chromosomes.append(chromo)
            dm = DoubleMinute(patient_id, bam_file, chromosomes, diagnosis)
            all_double_minutes.append(dm)
    return all_double_minutes


def get_unique_patients(all_dm):
    unique_patients = {}
    for dm in all_dm:
        if not unique_patients.__contains__(dm.get_patient_id()):
            unique_patients[dm.get_patient_id()] = []
        dm_list = unique_patients[dm.get_patient_id()]
        dm_list.append(dm)
        unique_patients[dm.get_patient_id()] = dm_list
    patients = []
    for patient_id, patient_dm in unique_patients.items():
        patients.append(Patient(patient_id, patient_dm))
    return patients


def get_distances_between_dm(dm_pair):
    for pair in dm_pair:
        distance = pair[0].get_distance(pair[1])
        print("Patient with TCGA id " + pair[0].get_patient_id() + " and whose  diagnosis and recurring files are\n" + pair[0].get_file() + "\nand\n" + pair[1].get_file() + "\nhave a calculated distance of " + str(distance) + " between them.\n")


def compare_patient_differences(patient_list):
    for patient in patient_list:
        dm_pairs = patient.get_dm_combos()
        for pair in dm_pairs:
            get_distances_between_dm(pair)


# all_dm = read_bed_files()
# print("Here are the distances between every patient's diagnosis and recurring double minute")
# print("0 distance means that they are identical and 1 distance means they have nothing in common\n")
# compare_patient_differences(get_unique_patients(all_dm))
dm1 = DoubleMinute
dm2 = DoubleMinute
with open('BEDfiles/G2145.TCGA-06-0152-01A-02D.12.bam.rmdup.bam.AA_amplicon4192_ecDNA_2_intervals.bed') as file:
    lines = file.readlines()
    chromosomes = []
    for line in lines:
        data = line.split("\t")
        chromo = Chromosome(data[0], data[1], data[2])
        chromosomes.append(chromo)
    dm = DoubleMinute('patient_id', 'bam_file', chromosomes, True)
with open('BEDfiles/G49538.TCGA-06-0152-02A-01D-2280-08.1.bam.rmdup.bam.AA_amplicon1779_ecDNA_1_intervals.bed') as file:
    lines = file.readlines()
    chromosomes = []
    for line in lines:
        data = line.split("\t")
        chromo = Chromosome(data[0], data[1], data[2])
        chromosomes.append(chromo)
    dm2 = DoubleMinute('patient_id', 'bam_file', chromosomes, False)
print(type(dm2))
result = dm2.get_distance(dm1)
print(result)

