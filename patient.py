import itertools
from array import array


class Patient:
    def __init__(self, name, double_minutes):
        self.double_minutes = double_minutes
        self.patient_id = str(name)

    def __str__(self):
        return self.patient_id

    def append_dm(self, dm):
        self.double_minutes.append(dm)

    def get_diagnosis_dm(self):
        diagnosis = []
        for dm in self.double_minutes:
            if dm.diagnosis:
                diagnosis.append(dm)
        return diagnosis

    def get_recurring_dm(self):
        recurring = []
        for dm in self.double_minutes:
            if not dm.diagnosis:
                recurring.append(dm)
        return recurring

    def get_dm_combos(self):
        diagnosis = self.get_diagnosis_dm()
        recurring = self.get_recurring_dm()
        combos = []
        combos.extend(list(zip(diagnosis, element)) for element in itertools.product(recurring, repeat = len(diagnosis)))
        return_value = combos.copy()
        types = []
        for l in combos:
            l_type = type(l)
            types.append(l_type)
            return_value.remove(l)
            if l not in return_value:
                return_value.append(list)
        return combos
