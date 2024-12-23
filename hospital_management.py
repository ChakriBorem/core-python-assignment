class Patient:
    def search(self, records, disease):
        names = []
        for i in records:
            if i["Disease"] == disease:
                names.append(i["Name"])
        print(f"Patients with {disease}: {names}")


obj = Patient()
patients = [

    {"Name": "Alice", "Age": 30, "Disease": "Flu"},

    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},

    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}

]
search_disease = "Flu"
obj.search(patients, search_disease)
