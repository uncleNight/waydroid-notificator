from flask import Flask, request
from pydbus import SessionBus


DURATION = 0

app = Flask(__name__)
bus = SessionBus()
notifications = bus.get('.Notifications')


@app.post("/")
def forward_notification():
    data = request.get_json(force=True)
    # TODO: detect repeated messages; possibly, remember them somewhere and delay the delivery to group them into one
    app_name = "Waydroid" # TODO: replace with app name from newer builds of Android app (net.kzxiv.notifikator.client.apk)
    title = data["title"]
    text = ""
    if "options" in data:
        text = data["options"]["body"]
    actions = []
    hints = {}  # {'x-nemo-preview-summary': title, 'x-nemo-preview-body': text},

    notifications.Notify(app_name, 0, "dialog-info", title, text, actions, hints, DURATION)

    return ""
