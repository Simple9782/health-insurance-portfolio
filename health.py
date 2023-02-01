# imports for the project
import csv

# create empty list for the arrtibutes in insurance.csv
ages = []
sexes = []
bmis = []
num_of_children = []
smoker_statuses =[]
regions = []
insurance_charges = []

# define function to load csv file data
def load_list_data(list, csv_file, column_name):
    # open csv file
    with open(csv_file) as csv_info:
        # read the date from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data for each row
        for row in csv_dict:
            # add the data to each row to a list
            list.append(row[column_name])
        return list

# look at each data in the insurance csv dict
load_list_data(ages, "insurance.csv", "age")
load_list_data(sexes, "insurance.csv", "sex")
load_list_data(bmis, "insurance.csv", "bmi")
load_list_data(num_of_children, "insurance.csv", "children")
load_list_data(smoker_statuses, "insurance.csv", "smoker")
load_list_data(regions, "insurance.csv", "region")
load_list_data(insurance_charges, "insurance.csv", "charges")

class PatientsInfo:
    # init method that takes in each list parameter
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_of_children, patients_smoker_statuses, patients_regions, patients_insurance_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_of_children = patients_num_of_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_insurance_charges = patients_insurance_charges
    # this define function is going to calculate the average ages of the patients in insurance.csv
    def analyze_ages(self):
        # initialize total age at zero
        total_age = 0
        # go through all the ages in the list
        for age in self.patients_ages:
            # sum of total age
            total_age += int(age)
        # return total age divided by the length of the patient list
        return ("Average Patient Age: " +str(round(total_age/len(self.patients_ages), 2)) + " years")

    # this define function is going to calculate the number of males and females in insurance.csv
    def analyze_sexes(self):
        # initialzie number of males and females to zero
        males = 0
        females = 0
        # go through each sex in the sexes list
        for sex in self.patients_sexes:
            # if male add to male variable
            if sex == "male":
                males += 1
            # if females add to female variable
            elif sex == "female":
                females += 1
        print("Count for male: ", males)
        print("Count for female: ", females)

    # this is going to help us find unique regions
    def unique_regions(self):
        # initialzie empty list
        unique_regions = []
        # go through each region in region list
        for region in self.patients_regions:
            # if the region is not already in the unique list
            # then add it to the unique list
            if region not in unique_regions:
                unique_regions.append(region)
        # return unique regions
        return unique_regions

    # this is going to find the average yearly mediacla charges for patients in insurance.csv
    def average_charges(self):
        # initialzie empty list
        total_charges = 0
        # go through charges in patients charges list
        # add each change to total charges
        for charge in self.patients_insurance_charges:
            total_charges += float(charge)
        # return the average charges rounded to the hundredths place
        return ("Average Yearly Medical Insurance Charges: " + str(round(total_charges/len(self.patients_insurance_charges),2)) + " dollars.")

    # this is going to create a dictionary with all the patients information
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_of_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_insurance_charges

patient_info = PatientsInfo(ages, sexes, bmis, num_of_children, smoker_statuses, regions, insurance_charges)
print(patient_info.analyze_ages())
print(patient_info.analyze_sexes())
print(patient_info.unique_regions())
print(patient_info.average_charges())
print(patient_info.create_dictionary())