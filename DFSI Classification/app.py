from flask import Flask, render_template, request, redirect, session
import os, hashlib, json, time
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret123"

DB_FILE = "evidence.json"

# ---------- LOAD DB ----------
def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    try:
        return json.load(open(DB_FILE))
    except:
        return {}

# ---------- SAVE DB ----------
def save_db(data):
    json.dump(data, open(DB_FILE, "w"), indent=4)

# ---------- HASH ----------
def get_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

# ---------- CLASSIFIER ----------
def classify_image(filename):
    name = filename.lower()
    if "violence" in name:
        return "Violence"
    elif "abuse" in name:
        return "Child Abuse"
    else:
        return "Normal"

# ---------- LOGIN ----------
@app.route('/')
def login_page():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    session['user'] = request.form['username']
    return redirect('/home')

# ---------- HOME ----------
@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect('/')

    if request.method == 'POST':
        file = request.files['my_image']

        if file.filename == "":
            return redirect('/home')

        os.makedirs("static", exist_ok=True)

        # ✅ UNIQUE FILE NAME (FIX)
        filename = str(int(time.time())) + "_" + file.filename
        filepath = os.path.join("static", filename)
        file.save(filepath)

        file_hash = get_hash(filepath)
        db = load_db()

        user = session['user']
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        prediction = classify_image(file.filename)

        original_img = None
        tamper_status = ""
        old_user = "-"
        old_time = "-"

        # 🔍 FIND SAME ORIGINAL FILENAME
        same_name_entry = None
        for h, data in db.items():
            if isinstance(data, dict) and data.get('original_name') == file.filename:
                same_name_entry = (h, data)
                break

        # ---------- FIRST UPLOAD ----------
        if same_name_entry is None:
            tamper_status = "ORIGINAL"

            db[file_hash] = {
                "user": user,
                "time": current_time,
                "original_name": file.filename,
                "path": filepath
            }
            save_db(db)

        else:
            old_hash, old_data = same_name_entry

            # ---------- SAME IMAGE ----------
            if old_hash == file_hash:
                tamper_status = "NOT TAMPERED"
                old_user = old_data.get('user', '-')
                old_time = old_data.get('time', '-')

            # ---------- MODIFIED ----------
            else:
                tamper_status = "TAMPERED"
                old_user = old_data.get('user', '-')
                old_time = old_data.get('time', '-')
                original_img = old_data.get('path')

        return render_template(
            "index.html",
            user=user,
            img_path=filepath,
            prediction=prediction,
            tamper_status=tamper_status,
            old_user=old_user,
            old_time=old_time,
            current_time=current_time,
            original_img=original_img
        )

    return render_template("index.html", user=session['user'])

# ---------- LOGOUT ----------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)