from flask import Blueprint, request, jsonify
from services.propietario_service import (
    listar_propietarios,
    obtener_propietario,
    agregar_propietario,
    actualizar_propietario,
    modificar_propietario,
    eliminar_propietario
)

propietario_bp = Blueprint('propietario', __name__)

@propietario_bp.route("/", methods=["GET"])
def get_propietarios():
    return jsonify({"data": listar_propietarios()})

@propietario_bp.route("/options", methods=["GET"])
def get_propietarios_options():
    propietarios = listar_propietarios()
    opciones = [{"id": p["id"], "nombre": p["nombres"], "dni": p["dni"]} for p in propietarios]
    return jsonify(opciones)

@propietario_bp.route("/<int:propietario_id>", methods=["GET"])
def get_propietario(propietario_id):
    propietario = obtener_propietario(propietario_id)
    return jsonify(propietario) if propietario else (jsonify({"error": "No encontrado"}), 404)

@propietario_bp.route("/", methods=["POST"])
def post_propietario():
    try:
        data = request.get_json()
        agregar_propietario(data)
        return jsonify({"message": "Propietario registrado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@propietario_bp.route("/<int:propietario_id>", methods=["PUT"])
def put_propietario(propietario_id):
    try:
        data = request.get_json()
        actualizar_propietario(propietario_id, data)
        return jsonify({"message": "Propietario actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@propietario_bp.route("/<int:propietario_id>", methods=["PATCH"])
def patch_propietario_(propietario_id):
    try:
        data = request.get_json()
        modificar_propietario(propietario_id, data)
        return jsonify({"message": "Propietario modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@propietario_bp.route("/<int:propietario_id>", methods=["DELETE"])
def delete_propietario_(propietario_id):
    try:
        eliminar_propietario(propietario_id)
        return jsonify({"message": "Propietario eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
