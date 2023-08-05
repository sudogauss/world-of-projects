# hand-controller

Allows to monitor hand landmarks using mediapipe and measure hand shaking direction and relative frame speed.
This functionality can be used to control scrolling and screen switching. For the moment it controls only scrolling.

After the installation you have 3 ways to run it: debug mode, prod mode, system service mode.

## Install and run

Requirements:

- systemd service (Linux)
- python>=3.8 

To install run the following commands:

```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip3 install pip --upgrade
    $ pip install --upgrade setuptools
    $ pip instal --upgrade wheel
    $ pip install . 
```
***Simple prod mode:***

Controls only scrolling for current window (must switch window).

```bash
    $ hand-controller
```

***Debug mode***

Prod mode + showing a current video frame with speed and direction of the hand shaking.

```bash
    $ hand-controller debug
```

***Systemd service***

Prod mode but launched as a systemd service on the background. You must configure you systemd.

First install ***hand-controller*** globally (with global **pip** and not the one used in your virtual environment).

Then you can use a handcontroller.service file to configure systemd:

```bash
    $ sudo cp handcontroller.service /etc/systemd/system
    $ sudo systemctl daemon-reload
    $ sudo systemctl enable handcontroller.service
    $ sudo systemctl start handcontroller.service
```

To stop it just run:

```bash
    $ sudo systemctl stop handcontroller.service
```

