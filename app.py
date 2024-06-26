from choice import *
import psycopg2
import psycopg2.extras
from functions import *

def main_():
    try:
        db_params = {
            'dbname':"Hospital",
            'user':"postgres",
            'password':"password",
            'host':"localhost",
            'port':"5432"
        }
        
        connection = psycopg2.connect(**db_params)
        cur= connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    except:
        print("Connection failed")
    else:
        print("Connected")

    while True:
        
        choice = show_menu()
        if choice == 0:
            clear_screen()
            print("Goodbye")
            break
        if choice == 1:
            
            cur.execute("""
        SELECT
        CONCAT(FLOOR(age / 10) * 10, '-', FLOOR(age / 10) * 10 + 9) AS age_range,
        COUNT(*) AS frequency
    FROM
        patient
    WHERE
        hospital_death = 1 AND age IS NOT NULL
    GROUP BY
        FLOOR(age / 10)
    ORDER BY
        FLOOR(age / 10); """)
    # Fetch the results
            results = cur.fetchall()
            # print(results)
            age_deaths(results)

        if choice == 2:
            cur.execute("""
        SELECT ethnicity, COUNT(hospital_death) as total_hospital_deaths
        FROM patient 
        WHERE hospital_death = '1'
        GROUP BY ethnicity;  """)
            rows = cur.fetchall()
            ethnicity_deaths(rows)
            
        if choice == 3:
            cur.execute("""SELECT
    ROUND(SUM(CASE WHEN aids = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS aids_percentage,
    ROUND(SUM(CASE WHEN cirrhosis = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS cirrhosis_percentage,
    ROUND(SUM(CASE WHEN diabetes_mellitus = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS diabetes_percentage,
    ROUND(SUM(CASE WHEN hepatic_failure = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS hepatic_failure_percentage,
    ROUND(SUM(CASE WHEN immunosuppression = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS immunosuppression_percentage,
    ROUND(SUM(CASE WHEN leukemia = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS leukemia_percentage,
    ROUND(SUM(CASE WHEN lymphoma = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS lymphoma_percentage,
    ROUND(SUM(CASE WHEN solid_tumor_with_metastasis = 1 THEN 1 ELSE 0 END) * 100 / COUNT(*),2) AS solid_tumor_percentage
FROM patient
WHERE hospital_death = 1;""")
            result = cur.fetchall()
            medical_condition_deaths(result)
        
        
        if choice==4:
            cur.execute("""
    SELECT
    icu_type,
    ROUND(AVG(CASE WHEN hospital_death = 1 AND pre_icu_los_days IS NOT NULL THEN pre_icu_los_days::numeric END), 2) AS avg_icu_stay_death,
    ROUND(AVG(CASE WHEN hospital_death = 0 AND pre_icu_los_days IS NOT NULL THEN pre_icu_los_days::numeric END), 2) AS avg_icu_stay_survived
FROM
    patient
GROUP BY
    icu_type
ORDER BY
    icu_type;
""")
            rows = cur.fetchall()
            ICU_type_deaths(rows)
        
        
        
        if choice == 5:

            cur.execute("""SELECT
    CONCAT(FLOOR(bmi / 10) * 10, '-', FLOOR(bmi / 10) * 10 + 9) AS bmi_range,
    COUNT(*) AS frequency
FROM
    patient
WHERE
    hospital_death = 1 AND bmi IS NOT NULL
GROUP BY
    FLOOR(bmi / 10)
ORDER BY
    FLOOR(bmi / 10);""")
            result = cur.fetchall()
            BMI_deaths(result)
            
main_()