# ThesisTopic.py

class ThesisTopic:
    def __init__(
        self, topic_number, internal_casuarina, internal_sydney, external, 
        chemical_engineering, civil_and_structural_engineering, 
        electrical_and_electronics_engineering, mechanical_engineering, 
        computer_science, cyber_security, data_science, 
        information_systems_and_data_science, software_engineering, 
        category, title, thesis_supervisor
    ):
        self.topic_number = topic_number
        self.internal_casuarina = internal_casuarina
        self.internal_sydney = internal_sydney
        self.external = external
        self.chemical_engineering = chemical_engineering
        self.civil_and_structural_engineering = civil_and_structural_engineering
        self.electrical_and_electronics_engineering = electrical_and_electronics_engineering
        self.mechanical_engineering = mechanical_engineering
        self.computer_science = computer_science
        self.cyber_security = cyber_security
        self.data_science = data_science
        self.information_systems_and_data_science = information_systems_and_data_science
        self.software_engineering = software_engineering
        self.category = category
        self.title = title
        self.thesis_supervisor = thesis_supervisor

    def __repr__(self):
        return f"ThesisTopic({self.topic_number}, {self.title}, {self.thesis_supervisor})"
