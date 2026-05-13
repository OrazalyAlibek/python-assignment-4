class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented - use a child class")

    def print_results(self):
        for key,value in self.result.items():
            print(key,":",value)

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"

class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        try:
            valid = list(filter(lambda s: s.get("GPA", "").strip() != "", self.students))
            values = [float(s["GPA"]) for s in valid]

            high_performers = list(filter(lambda g: g > 3.5, values))

            self.result = {
                "total_students": len(self.students),
                "average_gpa" : round(sum(values) / len(values), 2) if values else 0,
                "max_gpa" : max(values) if values else 0,
                "min_gpa" : min(values) if values else 0,
                "high_performers": len(high_performers),
            }
        except (ValueError, KeyError) as e:
            print(f"Analysi error: {e}")
            self.result = {}

    def print_results(self):
        print("="*30)
        print("GPA ANALYSIS REPORT")
        print("="*30)
        super().print_results()
        print("="*30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics  , {len(self.students)} students"

class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        try:
            valid = list(filter(lambda s: s.get("country", "").strip() != "", self.students))
            counts = {}
            for s in valid:
                c = s["country"]
                counts[c] = counts.get(c, 0) + 1

            top_3 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]

            self.result = {
                "total_students": len(self.students),
                "total_countries": len(counts),
                "top_3": top_3,
                "all_countries": counts,
            }

        except (ValueError, KeyError) as e:
            print(f"Country analysis error: {e}")
            self.result = {}

    def print_results(self):
        print("="*30)
        print("COUNTRY ANALYSIS REPORT")
        print("="*30)
        display = {k: v for k ,v in self.result.items() if k != 'all_countries'}
        original = self.result
        self.result = display
        super().print_results()
        self.result = original
        print("="*30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"