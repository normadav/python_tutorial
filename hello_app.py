from flask import Flask
import time
from datetime import datetime
from datetime import timezone

app = Flask(__name__)

@app.route("/")
def hello_world():
    DAYNAMES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                "Saturday", "Sunday"]
    dayname = DAYNAMES[datetime.now().weekday()]
    day = datetime.now(timezone.utc)
    epoch = time.time()
    return f"<p>Goodbye,world! Happy {dayname}, today is {day} or epoch time:{epoch}.</p>"