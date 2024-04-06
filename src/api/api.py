"""Flask API"""

import json
from datetime import datetime
from threading import Thread
from uuid import uuid4

from flask import Flask, request, jsonify, abort
from dotenv import load_dotenv

from src.api.exts import exts
from src.models import ResearchCrew
