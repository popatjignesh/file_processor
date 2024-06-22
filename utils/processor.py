# file_processor/utils/processor.py

import os
import csv

class FileProcessor:
    def __init__(self, input_folder, output_folder):
        """
        Initialize the FileProcessor with input and output folder paths.
        """
        self.input_folder = input_folder
        self.output_folder = output_folder

    def read_dat_files(self):
        """
        Read .dat files from the input folder and parse the data.
        Returns a list of dictionaries containing the parsed data.
        """
        data = []
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".dat"):
                file_path = os.path.join(self.input_folder, filename)
                with open(file_path, 'r') as file:
                    next(file)  # Skip the header
                    for line in file:
                        fields = line.strip().split()
                        if len(fields) == 7:
                            record = {
                                'id': fields[0],
                                'first_name': fields[1],
                                'last_name': fields[2],
                                'email': fields[3],
                                'job_title': fields[4],
                                'basic_salary': float(fields[5]),
                                'allowances': float(fields[6])
                            }
                            data.append(record)
        return data

    def calculate_gross_salary(self, records):
        """
        Calculate the gross salary for each record and add it to the record.
        """
        for record in records:
            record['Gross Salary'] = record['basic_salary'] + record['allowances']
        return records

    def remove_duplicates(self, records):
        """
        Remove duplicate records from the list.
        Returns a list of unique records.
        """
        seen = set()
        unique_records = []
        for record in records:
            record_tuple = tuple(record.values())
            if record_tuple not in seen:
                seen.add(record_tuple)
                unique_records.append(record)
        return unique_records

    def compute_footer_values(self, records):
        """
        Compute the second highest and average gross salary.
        Returns a tuple containing the second highest and average gross salary.
        """
        salaries = [record['Gross Salary'] for record in records]
        second_highest = sorted(set(salaries))[-2] if len(set(salaries)) > 1 else None
        average = sum(salaries) / len(salaries) if salaries else None
        return second_highest, average

    def write_to_csv(self, records, output_file_path, second_highest, average):
        """
        Write the records to a CSV file at the specified output path.
        Include the second highest and average salaries at the footer of the file.
        """
        fieldnames = ['id', 'first_name', 'last_name', 'email', 'job_title', 'basic_salary', 'allowances', 'Gross Salary']
        with open(output_file_path, 'w', newline='') as csvfile:
            dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            dict_writer.writeheader()
            for record in records:
                dict_writer.writerow(record)
            dict_writer.writerow({})

            # Logic to append required summary at the footer
            footer_writer = csv.writer(csvfile)
            second_highest_salary = 'Second Highest Salary = ' + str(second_highest)
            average_salary = 'Average Salary = ' + str(average)
            footer_writer.writerow([second_highest_salary, average_salary])

    def process_files(self):
        """
        Main method to process the files.
        Reads the .dat files, removes duplicates, processes the data
        calculates the required values, and writes the output to a CSV file.
        """
        records = self.read_dat_files()
        records = self.remove_duplicates(records)
        records = self.calculate_gross_salary(records)
        second_highest, average = self.compute_footer_values(records)
        output_file_path = os.path.join(self.output_folder, 'output.csv')
        self.write_to_csv(records, output_file_path, second_highest, average)
        print(f"Processing complete. Output written to {output_file_path}")
