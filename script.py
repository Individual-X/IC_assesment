import os
import shutil
import csv
import joblib

def categorize_resume(resume_path, model):
    category = model.predict(resume_path)
    replaced_valus= [15,  7, 21,  8,  1,  6,  9,  0,  5, 18, 14,  2,  3, 16, 17, 19, 10, 12, 20,  4, 11, 13, 23, 22]
    original_category = ['HR', 'DESIGNER', 'INFORMATION-TECHNOLOGY', 'TEACHER', 'ADVOCATE','BUSINESS-DEVELOPMENT', 'HEALTHCARE', 'FITNESS', 'AGRICULTURE','BPO', 'SALES', 'CONSULTANT', 'DIGITAL-MEDIA', 'AUTOMOBILE','CHEF', 'FINANCE', 'APPAREL', 'ENGINEERING', 'ACCOUNTANT','CONSTRUCTION', 'PUBLIC-RELATIONS', 'BANKING', 'ARTS', 'AVIATION']
    for i in range(len(replaced_valus)):
        if category == replaced_valus[i]:
            returned_cat = original_category[i]
    return eturned_cat

def main():
    input_directory = 'E:\Inreaactive Care assesment\archive\data\data'
    output_directory = 'E:\Inreaactive Care assesment\archive\data\data'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    model=joblib.load('Inreaactive Care assesment/Model/final model.pkl')

    
    csv_file_path = os.path.join(output_directory, "categorized_resumes.csv")
    with open(csv_file_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Resume Filename", "Category"])

        for resume_filename in os.listdir(input_directory):
            if resume_filename.endswith(".pdf"):  
                resume_path = os.path.join(input_directory, resume_filename)
                category = categorize_resume(resume_path, model)
                category_folder = os.path.join(output_directory, category)
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                new_resume_path = os.path.join(category_folder, resume_filename)
                shutil.move(resume_path, new_resume_path)
                csv_writer.writerow([resume_filename, category])

if __name__ == "__main__":
    main()
