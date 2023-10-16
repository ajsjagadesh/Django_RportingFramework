
__author__ = 'ajagadish.nayak'


API = [
    {
        "doorstep_url" : "http://10.24.34.155/v1/assessments?",
        "fe_header" : {
            "Content-Type": "application/json",
            "x-client-id": "vrp",
            "X-TENANT-ID": "RECOMMERCE", 
            "X-CONTEXT-ID": "FE_GRADING"
            },
        "tl_header" : {
            "Content-Type": "application/json",
            "x-client-id": "vrp",
            "X-TENANT-ID": "RECOMMERCE", 
            "X-CONTEXT-ID": "TL_GRADING"
            },
        "get_IMEI_url" : "https://fkdapi.gadgetwood.com/API/flipkart/GetAssessmentByImei",
        "imei_header" : {
            "Accept":"application/json",
            "Authorization":"Bearer TtgnNAthucvK-jCX_zEQ2wpFbeTxda9KbyKw-8Biki4SJ8DjgglmZs3qhsy3ChgL5AhIl7XxKWMSf6wsxrrlRwPijI75ieWF5hUGrQYjMmaBz7qJMem0ltcjQpR3iNFrSSH7sVWzGh0M1CUWoltu5bQNo6Zri-ODbKJyCii0-801JcC-pV6LgkDhA5DvYii87UIEpn7QsuMH4mCXMWnJ2E68r7DwNQkVFt-OByR0mb0",
            "Content-Type":"application/json"
            }

    }
]
