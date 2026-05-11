class Report:
    def __init__(self, analyser, saver):
        self.analyser = analyser
        self.saver = saver

    def generate_report(self):
        print(f"Generating report...")
        self.analyser.analyse()
        self.analyser.print_result()
        self.saver.save_json()
        print("Report complete!")