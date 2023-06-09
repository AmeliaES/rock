"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])

    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        return db.session.query(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()
    
    def get_ACT_average(self):
        """Return the average ACT cost"""
        return round(db.session.query(func.avg(PrescribingData.ACT_cost).label('ACT_average')).first()[0], 2)

    def get_top_prescribed(self):
        """Return the top prescrived medication"""
        return db.session.query(func.max(PrescribingData.items).label('top_item')).first()[0]
        
    def get_unique_items(self):
        """Return the number of unique items in the dataset"""
        return db.session.query(func.distinct(PrescribingData.BNF_name).label('item_unique')).count()
    
    def get_infection_percentage(self, code):
        """Return the infection treatment drug % of all infection treatments"""
        total = db.session.query(PrescribingData).filter(PrescribingData.BNF_code.like('05%')).count()
        code_amount = db.session.query(PrescribingData).filter(PrescribingData.BNF_code.like('05' + code + '%')).count()
        percent = int(code_amount/total*100)
        return percent
    


