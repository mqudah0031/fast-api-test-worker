import time
from worker import app


@app.task
def email(recipient, subject=None, body=None):
    time.sleep(3)  # simulate a request
    print("""
        ================ EMAIL =============
        to: {}
        ------
        subject: {}
        ------------------
        {}
        """.format(recipient, subject, body), flush=True)
