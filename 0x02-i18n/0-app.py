#!/usr/bin/env python3
"""First app module"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Main route"""
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run()
