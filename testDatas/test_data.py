from faker import Faker
from datetime import date

faker=Faker()


def admit_patient_test_data_generation():

    sex=['Male','Female']
    prescribing_pysician=['Gabriella Smith', 'Michelle Nash']
    referal_pysician=['ecg dev', 'devvv tessttt']
    interpreting_physician=['Gabriella Smith', 'Andrew Richards', 'Allison Hendricks']
    preliminary_interpreting_pysician=['Gabriella Smith', 'Andrew Richards', 'Allison Hendricks']
    technician=['Gabriella Smith', 'Phillip Conley']
    procedure_duration=['5-day','7-day',]
    biosensor=['0','1']
    location_group=['Ward A','Ward B','Ward C','Ward D','Ward E','Ward F','Ward G','Block-A','Block-B',
                    'B-A_Floor-1','B-A_F-1_Wing-A','B-A_F-1_WG-A_Ward-A','B-A_F-1_WG-A_WD-A_Male','B-A_F-1_WG-A_WD-A_M_Room-1',
                    'B-A_F-1_WG-A_WD-A_M_RM-1_Bay-1','Block-B_Floor-1','Block-B_F-1_Female','Block-B_F-1_Room-2','Block-B_F-1_Bay3',]
    true_or_false=['True','False',]
    billing_indication=['Billing1','Billing2',]
    billing_method=['Cash','Credit Card',]

    d = faker.date_between_dates(date_start=date(1950,1,1), date_end=date(2012,12,31))
    dob = str(d.day)+'/'+str(d.month)+'/'+str(d.year)
    return {
        "patient_demography": {
            "patientID":faker.bothify('PID#########'),
            "firstName":faker.first_name(),
            "lastName":faker.last_name(),
            "dateOfBirth": dob,
            "weight":faker.random_int(40,120),
            "height":faker.random_int(150,205),
            "sex":faker.word(ext_word_list=sex)
        },

    "patient_contact": {
            "countryCode":"91",
            "primaryContactNo":faker.numerify('9#########'),
            "emailID":faker.email(),
            "country":'American Samoa',#faker.country(),
            "zipCode":faker.postcode(),
            "streetAdress1":'I am italian',#faker.address(),
            "streetAdress2":'qwerdfds',#faker.address(),
            "state":faker.state(),
            "city":faker.city(),
            "emergencyContactNo":faker.numerify('9#########'),
            "emergencyContactName":faker.name()
        },

    "provider_info": {
            "prescribingPhysician":faker.word(ext_word_list=prescribing_pysician),
            "referalPhysician":faker.word(ext_word_list=referal_pysician),
            "interpretingPhysician":faker.word(ext_word_list=interpreting_physician),
            "preliminaryInterpretingPhysician":faker.word(ext_word_list=preliminary_interpreting_pysician),
            "technician":faker.word(ext_word_list=technician)
        },

    "procedure_info": {
            "prescriptionID":faker.bothify('PRID#########'),
            "orderID":faker.bothify('???0##########'),
            "primaryClinicalIndication":faker.name(),
            "biosensorID":'DP',
            "procedureDuration":faker.word(ext_word_list=procedure_duration),
            "locationGroup":'Loc 1',#faker.word(ext_word_list=location_group)
        },

    "additional_info": {
            "additionalInformation":faker.sentence(nb_words=10),
            "pacemaker":faker.word(ext_word_list=true_or_false),
            "icd":faker.word(ext_word_list=true_or_false)
        },

    "billing_info": {
            "billingIndication":faker.word(ext_word_list=billing_indication),
            "billingMethod":faker.word(ext_word_list=billing_method)
        }
    }