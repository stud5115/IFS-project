from flask import Flask, request, jsonify
import backend

app = Flask(__name__)

@app.route("/leave_balance", methods=["GET"])
def leave_balance():
    name = request.args.get("name")
    balance = backend.get_leave_balance(name)
    if balance is not None:
        return jsonify({"name": name, "leave_balance": balance})
    return jsonify({"error": "Employee not found"}), 404

@app.route("/apply_leave", methods=["POST"])
def apply_leave():
    data = request.get_json()
    name = data.get("name")
    days = data.get("days")
    success = backend.apply_leave(name, days)
    if success:
        return jsonify({"message": f"{days} days leave approved for {name}"})
    return jsonify({"error": "Not enough leave or employee not found"}), 400

if __name__ == "__main__":
    backend.init_db()
    app.run(debug=True)
