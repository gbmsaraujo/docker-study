import datetime
import json
import logging
import os
from flask import Flask, request

from bson.objectid import ObjectId
from flask_cors import CORS

from data.config.db_config import DatabaseConfig

app = Flask(__name__)

cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

db = DatabaseConfig()


db.initilize()


def log_request_info(msg):
    with open(os.path.abspath("./src/logs/acess.log"), "a") as f_logs:
        f_logs.write(f"{msg}\n")

@app.route("/goals", methods=["GET"])
def get_goals():
    try:
        query = [
            {"text": goal["text"], "id": str(goal["_id"])} for goal in db.find("goals")
        ]
        log_request_info(
            f"get goals feito às {datetime.datetime.strptime(str(datetime.datetime.now()), '%Y-%m-%d %H:%M:%S.%f').replace(microsecond=0)}"
        )
        return {"goals": query}
    except Exception as e:
        print(e)
        return {"message": str(e)}


@app.route("/goals", methods=["POST"])
def post_goals():
    try:
        body = request.json

        query = db.insert_one("goals", {"text": body["text"]})

        log_request_info(
            f"post goal feito às {datetime.datetime.strptime(str(datetime.datetime.now()), '%Y-%m-%d %H:%M:%S.%f').replace(microsecond=0)}"
        )

        return {"goal": {"id": str(query.inserted_id)}}
    except Exception as e:
        print(e)
        return {"message": str(e)}


@app.route("/goals/<id>", methods=["DELETE"])
def delete_goal(id: str):
    try:
        print(id)
        db.delete_one("goals", {"_id": ObjectId(id)})

        log_request_info(
            f"delete goals feito às {datetime.datetime.strptime(str(datetime.datetime.now()).replace(microsecond=0), '%Y-%m-%d %H:%M:%S.%f')}"
        )

        return {"data": "Goal Deleted sucessfully"}

    except Exception as e:
        print(e)
        return {"message": str(e)}


app.run(debug=True, host="0.0.0.0", port=5000)
