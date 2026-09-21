"""CYSC-620 Lab 7 sample - FIXED: no shell, debug off."""
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route("/ping/<host>")
def ping(host):
    return subprocess.check_output(["ping", "-c1", host], shell=False)


if __name__ == "__main__":
    app.run(debug=False)
