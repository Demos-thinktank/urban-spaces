import json
import csv
import os.path as path


class Division:

    def __init__(self, name):
        self.name = name
        root_dir = path.dirname(path.abspath(__file__))
        self.data_dir = path.join(root_dir, 'data')
        self.file = path.join(self.data_dir, name + ".csv")
        self.contents = self.read_csv()
        #self.json = self.order_by_first_value()
        self.json = json.dumps(self.contents)
        self.write_json()

    def read_csv(self):
        contents = []
        with open(self.file, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                contents.append(line)
        return contents

    def order_by_first_value(self):
        ordered = {}
        first_value = list(self.contents[0].keys())[0]
        other_values = list(self.contents[0].keys())[1:]
        for line in self.contents:
            area = line[first_value]
            ordered[area] = {}
            for value in other_values:
                ordered[area][value] = line[value]
        return ordered

    def write_json(self):
        out_path = path.join(self.data_dir, self.name + ".json")
        with open(out_path, 'w') as out_file:
            out_file.write(str(self.json))


if __name__ == "__main__":
    names = ['constituencies', 'locations', 'regions']
    [Division(name) for name in names]


