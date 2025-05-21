from flask import Blueprint, request, jsonify
from services.usuario_service import *

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route("/", methods=["GET"])
def get_usuarios():
    return jsonify({"data": listar_usuarios()})

@usuario_bp.route("/<int:user_id>", methods=["GET"])
def get_usuario(user_id):
    user = obtener_usuario(user_id)
    return jsonify(user) if user else (jsonify({"error": "No encontrado"}), 404)

@usuario_bp.route("/", methods=["POST"])
def post_usuario():
    try:
        data = request.get_json()
        registrar_usuario(data)
        return jsonify({"message": "Usuario registrado"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@usuario_bp.route("/<int:user_id>", methods=["PUT"])
def put_usuario(user_id):
    try:
        data = request.get_json()
        editar_usuario(user_id, data)
        return jsonify({"message": "Usuario actualizado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@usuario_bp.route("/<int:user_id>", methods=["PATCH"])
def patch_usuario_(user_id):
    try:
        data = request.get_json()
        modificar_usuario(user_id, data)
        return jsonify({"message": "Usuario modificado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@usuario_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_usuario_(user_id):
    try:
        eliminar_usuario(user_id)
        return jsonify({"message": "Usuario eliminado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
