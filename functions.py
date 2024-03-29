import matplotlib.pyplot as plt

def age_deaths(result):
    age_ranges = [row[0] for row in result]
    frequencies = [row[1] for row in result]

    # Plot the histogram
    plt.bar(age_ranges, frequencies, color='skyblue')
    plt.xlabel('Age Range')
    plt.ylabel('Frequency')
    plt.title('Histogram of Age Distribution')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

def ethnicity_deaths(rows):
    # Separate data for the pie chart
    labels = [row[0] for row in rows]
    values = [row[1] for row in rows]

    # Plotting the pie chart
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Hospital Deaths by Ethnicity')
    plt.show()


def medical_condition_deaths(result):
    

    # Separate data for the pie chart
    labels = [
        'AIDS', 'Cirrhosis', 'Diabetes Mellitus', 'Hepatic Failure',
        'Immunosuppression', 'Leukemia', 'Lymphoma', 'Solid Tumor'
    ]
    values = result[0]

    # Plotting the pie chart
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Patients who Died due to Different Medical Conditions')
    plt.show()


def ICU_type_deaths(rows):
    icu_types = [row[0] for row in rows]
    avg_icu_stay_death = [row[1] for row in rows]
    avg_icu_stay_survived = [row[2] for row in rows]

    # Plotting the bar graph
    bar_width = 0.35
    index = range(len(icu_types))

    plt.bar(index, avg_icu_stay_death, bar_width, label='Avg ICU Stay (Death)')
    plt.bar([i + bar_width for i in index], avg_icu_stay_survived, bar_width, label='Avg ICU Stay (Survived)')

    plt.xlabel('ICU Type')
    plt.ylabel('Average ICU Stay')
    plt.title('Average ICU Stay by ICU Type')
    plt.xticks([i + bar_width / 2 for i in index], icu_types,rotation='vertical')
    plt.legend()

    plt.tight_layout()
    plt.show()


def BMI_deaths(result):
    bmi_ranges = [row[0] for row in result]
    frequencies = [row[1] for row in result]

    # Plot the histogram
    plt.bar(bmi_ranges, frequencies, color='skyblue')
    plt.xlabel('BMI Range')
    plt.ylabel('Frequency')
    plt.title('Histogram of BMI Distribution')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()
        






