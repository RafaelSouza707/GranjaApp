from flask import request, current_app
from flask_restful import Resource
from models.lote_frangos import LoteFrango
from helpers.database import db
from models.venda_corte import VendaCorte
from schemas.venda_corte_schema import VendaCorteSchema

venda_corte_schema = VendaCorteSchema()
vendas_cortes_schema = VendaCorteSchema(many=True)


class VendaCorteResource(Resource):

    def get(self, id=None):
        if id:
            venda_corte = VendaCorte.query.get(id)
            
            if not venda_corte:
                current_app.logger.warning(f"Venda de corte id = {id} não encontrada")
                return {"message": f"Venda de corte id = {id} não encontrada"}, 404
            
            current_app.logger.info(f"Venda de corte id = {id} encontrada com sucesso")
            return venda_corte_schema.dump(venda_corte), 200    
        
        vendas_cortes = VendaCorte.query.all()
        current_app.logger.info("Buscando todas as vendas de corte")    
        return vendas_cortes_schema.dump(vendas_cortes), 200
    
    def post(self):
        json_data = request.get_json() 
        data = venda_corte_schema.load(json_data) 
        
        lote = LoteFrango.query.get(data["id_lote_frango"]) 
        if not lote:
            return {"erro": "Lote de frango não existe"}, 400
        
        nova_venda_corte = VendaCorte(**data) 
        db.session.add(nova_venda_corte) 
        current_app.logger.info("Nova venda de corte sendo inserida")
        
        db.session.commit()
        current_app.logger.info(f"Venda de corte inserida com sucesso {nova_venda_corte}")
        
        return venda_corte_schema.dump(nova_venda_corte), 201
    
    def put(self, id):
        venda_corte = VendaCorte.query.get_or_404(id) 
        json_data = request.get_json() 
        data = venda_corte_schema.load(json_data) 
        
        lote = LoteFrango.query.get(data["id_lote_frango"]) 
        if not lote:
            return {"erro": "Lote de frango não existe"}, 400
        
        current_app.logger.info(f"Atualizando venda de corte id= {id}")
        
        venda_corte.lote_frango_id = data["id_lote_frango"] 
        venda_corte.data = data["data"] 
        venda_corte.valor = data["valor"]
        venda_corte.quilos = data["quilos"]
        
        db.session.commit()
        current_app.logger.info(f"Venda de corte id= {id} atualizada com sucesso")
        
        return venda_corte_schema.dump(venda_corte), 200
    
    def delete(self, id):
        venda_corte = VendaCorte.query.get_or_404(id) 
        db.session.delete(venda_corte) 
        db.session.commit() 
        current_app.logger.info(f"Venda de corte id= {id} deletada com sucesso")
        return {"message": f"Venda de corte id= {id} deletada com sucesso"}, 200
