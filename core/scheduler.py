from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .models import Medicine
from .utils import send_sms

def check_medicines():
    now = datetime.now().strftime("%H:%M")
    print("⏱ Checking time:", now)

    medicines = Medicine.objects.all()

    for med in medicines:
        med_time = med.time.strftime("%H:%M")

        if med_time == now:
            message = f"Time to take {med.name} ({med.dosage})"
            send_sms(med.phone, message)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_medicines, 'interval', seconds=30)
    scheduler.start()