from __future__ import absolute_import

from celery import shared_task

from oauth2 import tasks as oauth2_tasks
from send_email import tasks as email_tasks

@shared_task
def check_bdays_and_email():
    async_result = oauth2_tasks.get_api_data.delay()
    data_collection = async_result.get()
    print("api_data: ", data_collection)

    for doctor_id, api_data in data_collection.items():
        results = api_data["results"]

        for patient_data in results:
            print(patient_data)
            email = patient_data["email"]

            data = """
            Hello there!

            I wanted to wish you a happy birthday. \
            We have worked day and night to ensure that you get the best service. I hope \
            that you will continue to use our service.

            Best Regards,
            ~ Jeff
                """

            email_tasks.send_email.delay(email, data)
