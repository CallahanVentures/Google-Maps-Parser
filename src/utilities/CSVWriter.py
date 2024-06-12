import csv
from datetime import datetime

class CSVWriter:
    @staticmethod
    def write_to_csv(business_data):
        timestamp = datetime.now().strftime("%m-%d-%y %H_%M_%S")
        csv_file_name = f"data/results/business_data_{timestamp}.csv"

        print("Writing To CSV")
        with open(csv_file_name, 'w', newline='', encoding='utf-8') as csvfile:
            try:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Business Name', 'Business Address', 'Business Phone', 'Business Website'])
                csv_writer.writerows(business_data)
            except:
                with open(csv_file_name.replace(".csv", ".txt"), "w+", encoding='utf-8') as backupfile:
                    backupfile.writelines(business_data)
        print("Done")
