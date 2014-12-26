# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import time
from openerp import pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _

class is_secteur_activite(osv.osv):
    _name = 'is.secteur.activite'
    _description = u"Secteurs d'activités"
    
    _columns = {
        'name': fields.char('Secteur', required=True),
    }
    
is_secteur_activite()

class is_port_incoterm(osv.osv):
    _name = 'is.port.incoterm'
    _description = "Port / Incoterm"
    
    _columns = {
        'name': fields.char('Port / Incoterm', required=True),
    }
    
is_port_incoterm()

class is_segment_achat(osv.osv):
    _name = 'is.segment.achat'
    _description = "Segment d'achat"
    
    _columns = {
        'name': fields.char('Code', size=256, required=True),
        'description': fields.text('Commentaire'),
        'family_line': fields.one2many('is.famille.achat', 'segment_id', 'Familles'),
    }
    
is_segment_achat()

class is_famille_achat(osv.osv):
    _name = 'is.famille.achat'
    _description = "Famille d'achat"
    
    _columns = {
        'name': fields.char('Code', size=256, required=True),
        'segment_id': fields.many2one('is.segment.achat', 'Segment', required=True),
        'description': fields.text('Commentaire'),
    }
    
is_famille_achat()

class is_site(osv.osv):
    _name = 'is.site'
    _description = 'Sites'
    
    _columns = {
        'name': fields.char('Site', required=True),
    }
    
is_site()

class is_transmission_cde(osv.osv):
    _name = 'is.transmission.cde'
    _description = 'Mode de transmission des cmds'
    
    _columns = {
        'name': fields.char('Mode de transmission des commandes', required=True),
    }
    
is_transmission_cde()

class is_norme_certificats(osv.osv):
    _name = 'is.norme.certificats'
    _description = u'Norme Certificat qualité'
    
    _columns = {
        'name': fields.char('Nome certificat', required=True),
    }

is_norme_certificats()

class is_certifications_qualite(osv.osv):
    _name = 'is.certifications.qualite'
    _description = u'Certifications qualité'
    
    _columns = {
        'is_norme': fields.many2one('is.norme.certificats', u'Norme Certificat qualité', required=True),
        'is_date_validation': fields.date('Date de validation du certificat', required=True),
        'is_certificat': fields.binary('Certificat qualité'),
        'partner_id': fields.many2one('res.partner', 'Client/Fournisseur'),
    }

is_certifications_qualite()

class is_partner(osv.osv):
    _inherit = 'res.partner'
    
    _columns = {
        'is_secteur_activite': fields.many2one('is.secteur.activite', u"Secteur d'activité"),
        'is_num_fournisseur': fields.char(u'N° de fournisseur'),
        'is_type_reglement': fields.many2one('account.journal', u'Type règlement', domain=[('type', 'in', ['bank','cash'])]),
        'is_escompte': fields.float('Escompte (%)'),
        'is_port_incoterm': fields.many2one('is.port.incoterm', 'Port / Incoterm'),
        'is_num_siret': fields.char(u'N° de SIRET'),
        'is_segment_achat': fields.many2one('is.segment.achat', "Segment d'achat"),
        'is_famille_achat': fields.many2one('is.famille.achat', "Famille d'achat"),
        'is_fournisseur_imp': fields.boolean(u'Fournisseur imposé'),
        'is_site_livre': fields.many2one('is.site', u'sites livrés'),
        'is_groupage': fields.boolean('Groupage'),
        'is_tolerance_delai': fields.boolean('Tolérance sur délai'),
        'is_tolerance_quantite': fields.boolean('Tolérance sur quantité'),
        'is_transmission_cde': fields.many2one('is.transmission.cde', 'Mode de transmission des commandes'),
        'is_certifications': fields.one2many('is.certifications.qualite', 'partner_id', u'Certification qualité'),
        'is_type_contact': fields.many2one('is.type.contact', "Type de contact"),
    }
    
    def onchange_segment_id(self, cr, uid, ids, segment_id, context=None):
        domain = []
        val = {'is_famille_achat': False }
        if segment_id:
            domain.append(('segment_id','=',segment_id))           
        return {'value': val,
                'domain': {'is_famille_achat': domain}}
    
is_partner()

class is_type_contact(osv.osv):
    _name = 'is.type.contact'
    _description = 'Types des adresses des contacts'
    
    _columns = {
        'name': fields.char("Type d'adresse", required=True),
    }
    
is_type_contact()