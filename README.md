# Waydroid Notificator

A simple Flask-based app to display notifications forwarded by [Notifikator app](https://github.com/koro666/notifikator) as Linux notification pop-ups via DBus. Meant to run as a SystemD service (from user) with `gunicorn`.

Notifikator needs to be configured to forward notification data as JSON to `http://<waydroid-bridge-ip>:8000` - most likely, this will be `192.168.240.1`. As a security precaution, `run.sh` script detects Waydroid bridge IP to bind `gunicorn` to it - thus, port `8000` is only open to requests from Waydroid.

## Installation

> The app is very raw at this stage and does not have an RPM package. The installation process is manual and is focused on getting the things done ASAP.

Copy the app contents into `/opt` (or clone the repo as `/opt/waydroid-notificator`), install Python dependencies (preferably, system-wide so the paths are available to SystemD), register the SystemD service and run it.

Commands run on a Sailfish OS:

```bash
cd /opt/waydroid-notificator
devel-su pip install -r requirements.txt
cp waydroid-notificator.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable waydroid-notificator
systemctl --user start waydroid-notificator
```

At this point, the app should run as a SystemD-managed daemon and listen on `192.168.240.1:8000`.

In Waydroid:
* install [Notifikator app](https://github.com/koro666/notifikator/releases)
* allow Notifikator to intercept system notifications
* set _URL_ to `http://192.168.240.1:8000` (IP can change depending on your Waydroid setup!)
* set _Protocol_ to `JSON`
* do not enable authentication

You can test the notifications now using the dedicated button in Notifikator.

## Known Issues

* v1.1 of Notifikator app does not include application name in the JSON data. `master` branch of the repo contains all the fix already, there's just no built `.apk` file to download. Flask app was designed with v1.1 in mind (at least until I rebuild the Notificator) so it displays _Waydroid_ as application name for every notification
* some Android applications duplicate the same notification multiple times when a long-running process with a progress bar is executed (Waydroid backup, Seedvault, is a good example - it sends about ten notifications at once). The app does not handle these as the same notification currently, so you'll be spammed every time such an event happens in Waydroid.

## License

* [MIT](./LICENSE)
