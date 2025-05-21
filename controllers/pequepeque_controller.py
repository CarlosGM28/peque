from flask import Blueprint, request, jsonify
from services.pequepeque_service import (
    listar_pequepeques,
    obtener_pequepeque,
    agregar_pequepeque,
    actualizar_pequepeque,
    modificar_pequepeque,
    eliminar_pequepeque
)

pequepeque_bp = Blueprint('pequepeque', __name__)

@pequepeque_bp.route("/", methods=["GET"])
def get_pequepeques():
    return jsonify({"data": listar_pequepeques()})

@pequepeque_bp.route("/options", methods=["GET"])
def get_pequepeques_options():
    pequepeques = listar_pequepeques()
    return jsonify([{"id": p["id"], "nombre": p["nombre"]} for p in pequepeques])

@pequepeque_bp.route("/<int:pequepeque_id>", methods=["GET"])
def get_pequepeque(pequepeque_id):
    p = obtener_pequepeque(pequepeque_id)
    return jsonify(p) if p else (jsonify({"error": "No encontrado"}), 404)

@pequepeque_bp.route("/", methods=["POST"])
def post_pequepeque():
    try:
        data = request.get_json()
        agregar_pequepeque(data)
        return jsonify({"message": "Pequepeque registrado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@pequepeque_bp.route("/<int:pequepeque_id>", methods=["PUT"])
def put_pequepeque(pequepeque_id):
    try:
        data = request.get_json()
        actualizar_pequepeque(pequepeque_id, data)
        return jsonify({"message": "Pequepeque actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@pequepeque_bp.route("/<int:pequepeque_id>", methods=["PATCH"])
def patch_pequepeque_(pequepeque_id):
    try:
        data = request.get_json()
        modificar_pequepeque(pequepeque_id, data)
        return jsonify({"message": "Pequepeque modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@pequepeque_bp.route("/<int:pequepeque_id>", methods=["DELETE"])
def delete_pequepeque_(pequepeque_id):
    try:
        eliminar_pequepeque(pequepeque_id)
        return jsonify({"message": "Pequepeque eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
