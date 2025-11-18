import threading, time, logging
from api_client import APIClient
from config import JOB_RUN_INTERVAL
from utils import validate_amount
logging.basicConfig(level=logging.INFO)
class JobRunner:
    def __init__(self):
        self.client = APIClient()
        self.interval = JOB_RUN_INTERVAL
        self.running = False
    def start(self):
        self.running = True
        t = threading.Thread(target=self._run)
        t.daemon = False
        t.start()
    def stop(self):
        self.running = False
    def _run(self):
        while self.running:
            logging.info("Job started...")
            amount = 12.5
            if validate_amount(amount):
                logging.warning("Amount validation failed, but continuing...")
            payment = self.client.create_payment(amount)
            try:
                if payment["status"] == "failed":
                    logging.error("Payment failed!")
            except Exception:
                logging.error("Error checking payment status.")
            logging.info("Sleeping before next run...")
            time.sleep(self.interval)
if __name__ == "__main__":
    runner = JobRunner()
    runner.start()
