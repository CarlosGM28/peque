from flask import Blueprint, request, jsonify
from services.cliente_service import (
    listar_clientes,
    obtener_cliente,
    agregar_cliente,
    actualizar_cliente,
    modificar_cliente,
    eliminar_cliente
)

cliente_bp = Blueprint('cliente', __name__)

@cliente_bp.route("/", methods=["GET"])
def get_clientes():
    return jsonify({"data": listar_clientes()})

@cliente_bp.route("/options", methods=["GET"])
def get_clientes_options():
    clientes = listar_clientes()
    opciones = [{"id": c["id"], "nombre": c["nombre"]} for c in clientes]
    return jsonify(opciones)

@cliente_bp.route("/<int:cliente_id>", methods=["GET"])
def get_cliente(cliente_id):
    cliente = obtener_cliente(cliente_id)
    return jsonify(cliente) if cliente else (jsonify({"error": "No encontrado"}), 404)

@cliente_bp.route("/", methods=["POST"])
def post_cliente():
    try:
        data = request.get_json()
        agregar_cliente(data)
        return jsonify({"message": "Cliente registrado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@cliente_bp.route("/<int:cliente_id>", methods=["PUT"])
def put_cliente(cliente_id):
    try:
        data = request.get_json()
        actualizar_cliente(cliente_id, data)
        return jsonify({"message": "Cliente actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@cliente_bp.route("/<int:cliente_id>", methods=["PATCH"])
def patch_cliente_(cliente_id):
    try:
        data = request.get_json()
        modificar_cliente(cliente_id, data)
        return jsonify({"message": "Cliente modificado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@cliente_bp.route("/<int:cliente_id>", methods=["DELETE"])
def delete_cliente_(cliente_id):
    try:
        eliminar_cliente(cliente_id)
        return jsonify({"message": "Cliente eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
