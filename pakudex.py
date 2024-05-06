# Project 3: Pakudex Project (pakudex class)

from pakuri import Pakuri


class Pakudex:

    def __init__(self, capacity=20):
        self.capacity = int(capacity)
        self.index = []
        self.pakuris = []


    def get_size(self):
        return len(self.index)


    def get_capacity(self):
        return self.capacity


    def get_species_array(self):
        if self.index == []:
            return None
        return self.index


    def get_stats(self, species):
        for entry in self.pakuris:
            if entry.get_species() == species:
                return [entry.get_attack(), entry.get_defense(), entry.get_speed()]
        return None


    def sort_pakuri(self):
        self.index.sort()


    def add_pakuri(self, species):
        for entry in self.index:
            if entry == species:
                return False
        self.index.append(species)
        self.pakuris.append(Pakuri(species))
        return True


    def evolve_species(self, species):
        for entry in self.pakuris:
            if entry.get_species() == species:
                entry.evolve()
                return True
        return False
