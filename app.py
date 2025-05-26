from flask import Flask, request, render_template, redirect, url_for, jsonify
import os
from split_and_store import main as dividir_ficheiro
from rebuild_file import rebuild_file

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="templates",
    static_url_path=""
)

UPLOAD_FOLDER = os.path.join(os.getcwd(), "Uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            return jsonify({"erro": "Nenhum ficheiro enviado"}), 400
        file = request.files['file']
        if file.filename == "":
            return jsonify({"erro": "Ficheiro sem nome"}), 400

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        try:
            dividir_ficheiro(file_path)
            return render_template("upload.html", sucesso=True, filename=file.filename)
        except Exception as e:
            return render_template("upload.html", erro=str(e))

    return render_template("upload.html")

@app.route("/rebuild", methods=["GET", "POST"])
def rebuild_from_form():
    filename = request.form.get("filename") if request.method == "POST" else request.args.get("filename")
    if not filename:
        return "Erro: nome do ficheiro não fornecido.", 400

    original_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.isfile(original_path):
        return f"Erro: o ficheiro '{filename}' não existe na pasta de uploads.", 404

    extension = filename.split(".")[-1]
    output_path = os.path.join(os.getcwd(), "Uploads", f"{filename.split('.')[0]}_reconstruida.{extension}")
    try:
        rebuild_file(filename, output_path)
        reconstructed_filename = f"{filename.split('.')[0]}_reconstruida.{extension}"
        return render_template("download.html", filename=reconstructed_filename)
    except Exception as e:
        return f"Erro ao reconstruir: {str(e)}", 500

@app.route("/api/rebuild/<filename>", methods=["GET"])
def api_rebuild(filename):
    try:
        extension = filename.split(".")[-1]
        output_path = os.path.join(os.getcwd(), f"{filename.split('.')[0]}_reconstruida.{extension}")
        rebuild_file(filename, output_path)
        return jsonify({"mensagem": f"Ficheiro '{filename}' reconstruído com sucesso!", "ficheiro": output_path}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
