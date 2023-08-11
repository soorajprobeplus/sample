# Locators

locators={

    'login_page':{
        'user_name':'username',
        'password':'password',
        'submit_button':'kc-login'
    },

    'summary_page':{
        'register_new_procedure_button':'',
    },

    'admit_patient':{

        'cancel_button':'',
        'save_button':'',
        'option_text':'',
        'error_label':'',
        'patient_demographics':{
            'patient_id':'option',
            'first_name':'first_name',
            'last_name':'last_name',
            'date_of_birth':'dob',
            'age':'age',
            'sex':'',
            'weight':'weight',
            'height':'height',
        },

        'patient_contact':{
            'country_code':'',
            'primary_contact_number':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[1]/div/app-tel-input/div/mat-form-field/div/div[1]/div[2]/lac-mat-tel-input/input',
            'email_id':'email',
            'country':'country',
            'zip_code':'zip_code',
            'street_adress_1':'street_address_1',
            'street_adress_2':'street_address_2',
            'state':'state',
            'city':'city',
            'country_code':'',
            'emergency_contact_number':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[7]/div[2]/div/app-tel-input/div/mat-form-field/div/div[1]/div[2]/lac-mat-tel-input/input',
            'emergency_contact_name':'em_contact_name',
        },

        'provider_info':{
            'prescribing_physician':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[1]/mat-form-field/div/div[1]/div/mat-select/div/div[1]',
            'referal_physician':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[2]/mat-form-field/div/div[1]/div/mat-select/div/div[1]',
            'interpreting_physycian':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[3]/mat-form-field/div/div[1]/div/mat-select/div/div[1]',
            'preliminary_interpreting_physician':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[4]/mat-form-field/div/div[1]/div/mat-select/div/div[1]',
            'technician':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[5]/mat-form-field/div/div[1]/div/mat-select/div/div[1]',            
        },

        'procedure_info':{
            'prescription_id':'prescription_id',
            'order_id':'order_id',
            'primary_clinical_indicaton':'primary_indication',
            'biosensor_id':'patch_id',
            'procedure_duration':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[4]/div[2]/div/mat-form-field/div/div[1]/div/mat-select/div/div[1]',
            'location_group':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[4]/div[1]/div/app-nested-dropdown/div',
            'biosensor_start_date':'biosensor_start_date'
        },

    'additional_info':{
        'additional_information':'additional_information',
        'pacemaker':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[2]/div[1]/input',
        'icd':'/html/body/div[2]/div[2]/div/mat-dialog-container/app-admit-patient-modal/mat-dialog-content/form/div[2]/div[2]/div[2]/input'
        },

    'billing_info':{
        'billing_indication':'',
        'billing_method':''
        },

    },
}
