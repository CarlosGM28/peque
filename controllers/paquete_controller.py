from flask import Blueprint, request, jsonify
from services.paquete_service import (
    listar_paquetes,
    obtener_paquete,
    agregar_paquete,
    actualizar_paquete,
    modificar_paquete,
    eliminar_paquete
)

paquete_bp = Blueprint('paquete', __name__)

@paquete_bp.route("/", methods=["GET"])
def get_paquetes():
    return jsonify({"data": listar_paquetes()})

@paquete_bp.route("/options", methods=["GET"])
def get_paquetes_options():
    paquetes = listar_paquetes()
    return jsonify([{"id": p["id"], "denominacion": p["denominacion"]} for p in paquetes])

@paquete_bp.route("/<int:paquete_id>", methods=["GET"])
def get_paquete(paquete_id):
    paquete = obtener_paquete(paquete_id)
    return jsonify(paquete) if paquete else (jsonify({"error": "No encontrado"}), 404)

@paquete_bp.route("/", methods=["POST"])
def post_paquete():
    try:
        data = request.get_json()
        agregar_paquete(data)
        return jsonify({"message": "Paquete registrado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@paquete_bp.route("/<int:paquete_id>", methods=["PUT"])
def put_paquete(paquete_id):
    try:
        data = request.get_json()
        actualizar_paquete(paquete_id, data)
        return jsonify({"message": "Paquete actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@paquete_bp.route("/<int:paquete_id>", methods=["PATCH"])
def patch_paquete_(paquete_id):
    try:
        data = request.get_json()
        modificar_paquete(paquete_id, data)
        return jsonify({"message": "Paquete modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@paquete_bp.route("/<int:paquete_id>", methods=["DELETE"])
def delete_paquete_(paquete_id):
    try:
        eliminar_paquete(paquete_id)
        return jsonify({"message": "Paquete eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
