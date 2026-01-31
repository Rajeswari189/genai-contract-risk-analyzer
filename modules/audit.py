import json
import os
from datetime import datetime

def save_audit(data):
    if not os.path.exists("audit_logs"):
        os.makedirs("audit_logs")

    filename = f"audit_logs/{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
