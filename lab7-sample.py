"""CYSC-620 Lab 7 sample - the same class of findings Bandit reported for Vulpy.
This file is intentionally insecure. It is never executed or deployed."""
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route("/ping/<host>")
def ping(host):
    return subprocess.check_output("ping -c1 " + host, shell=True)


if __name__ == "__main__":
    app.run(debug=True)
