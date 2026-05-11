import csv

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.students = []

    def load(self):
        try:
            with open(self.file_path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.students.append(row)
            print(f"Loaded {len(self.students)} students from {self.file_path}")
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found")
        except Exception as e:
            print(f"Error loading data: {e}")

    def preview(self, n=5):
        print(f"First {n} rows:")
        for row in self.students[:n]:
            print(row)
        print()