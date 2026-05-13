from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser, CountryAnalyser

fm = FileManager('students.csv')
fm.check_file()
fm.create_output_folder('output')

dl = DataLoader('students.csv')
dl.load()
dl.preview()

#Task 1
from analytics.analyser import DataAnalyser
base = DataAnalyser(dl.students)
print(base)
base.analyse()
print()

#Task 2
analyser = GpaAnalyser(dl.students)
print(analyser)
analyser.analyse()

#Task 3
analyser.print_results()
print()

#Task 4
saver = ResultSaver(analyser.result, 'output/result.json')
report = Report(analyser, saver)
report.generate()
print()

#Task 5
sample_10 = dl.students[:10]
analysers = [
    GpaAnalyser(dl.students),
    CountryAnalyser(sample_10),
]

print ("-"*30)
print("Running all analysers:")
print("-"*30)

for a in analysers:
    print(a)
    a.analyse()
    a.print_results()
    print()
