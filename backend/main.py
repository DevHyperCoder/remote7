import time

from flask import Flask, request
from flask_cors import CORS

from remote7.driver import SevenSegmentDriver
from remote7.constants import pins

app = Flask(__name__)
CORS(app)

driver = SevenSegmentDriver(pins,ca=True)

@app.route("/api/display", methods=["POST"])
def display():

    msg = request.get_json()["msg"]

    # Delay is sent in milliseconds. This allows for finer control
    delay = int(request.get_json()["delay"]) / 1000

    try:
        # Special commands can not be displayed on the 7 Segment display so it is unambiguous.
        if msg == "BLINK ALL":
            driver.blink_all(delay)
        elif msg == "PATTERN":
            driver.show_pattern(delay)
        elif msg == "OFF":
            driver.turn_off()
        else:
            driver.display(msg, delay)
        return {"status": "OK"}, 200
    except Exception as e:
        return {"status": "ERR", "msg": str(e)}, 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
