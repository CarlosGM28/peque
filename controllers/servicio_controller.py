from flask import Blueprint, request, jsonify
from services.servicio_service import (
    listar_servicios,
    obtener_servicio,
    agregar_servicio,
    actualizar_servicio,
    modificar_servicio,
    eliminar_servicio
)

servicio_bp = Blueprint('servicio', __name__)

@servicio_bp.route("/", methods=["GET"])
def get_servicios():
    return jsonify({"data": listar_servicios()})

@servicio_bp.route("/<int:servicio_id>", methods=["GET"])
def get_servicio(servicio_id):
    s = obtener_servicio(servicio_id)
    return jsonify(s) if s else (jsonify({"error": "No encontrado"}), 404)

@servicio_bp.route("/", methods=["POST"])
def post_servicio():
    try:
        data = request.get_json()
        agregar_servicio(data)
        return jsonify({"message": "Servicio registrado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@servicio_bp.route("/<int:servicio_id>", methods=["PUT"])
def put_servicio(servicio_id):
    try:
        data = request.get_json()
        actualizar_servicio(servicio_id, data)
        return jsonify({"message": "Servicio actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@servicio_bp.route("/<int:servicio_id>", methods=["PATCH"])
def patch_servicio_(servicio_id):
    try:
        data = request.get_json()
        modificar_servicio(servicio_id, data)
        return jsonify({"message": "Servicio modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@servicio_bp.route("/<int:servicio_id>", methods=["DELETE"])
def delete_servicio_(servicio_id):
    try:
        eliminar_servicio(servicio_id)
        return jsonify({"message": "Servicio eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400