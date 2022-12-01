#!/usr/bin/python3
# -*-coding:iso-8859-15-*-
# -*- coding: utf-8 -*-
# -*- coding: 850 -*-
# -*- coding: cp1252 -*-

#from DirectionsIO import coinDroppedBySelf
#from DirectionsIO import createOrders
from itertools import cycle
import smtplib
from traceback import print_tb
from flask import Flask, jsonify, request, Response
from werkzeug.wrappers import ResponseStream, response
import BackEnd.generalInfo.KeysIO as globalInfo
import BackEnd.generalInfo.ResponseMessages as ResponseMessages
import importlib
import random
import hashlib

#from pymongo import MongoClient
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import email
import email.mime.application
# from datetime import datetime
import datetime
'''
import BackEnd.generalInfo.FuncionesCRON as funcionesCron
import BackEnd.pdfReportGenerator as reporte
import BackEnd.MailServer as MailServer
#### Librerias para fechas
import datetime
from datetime import date, timedelta
import time
'''
import requests
import urllib.request

import jwt

import json
import sys
import base64
import os
import uuid
import linecache
import pymysql.cursors

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/var/www/html/profiles'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

versionApp = 1.0

# Connection for DB
def getConectionMYSQL():
	return pymysql.connect(host=globalInfo.strDBHost,port=globalInfo.strDBPort,
                             user=globalInfo.strDBUser,
                             password=globalInfo.strDBPassword,
                             db=globalInfo.strDBName,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#################################################################################
# FUNCIONES DE USO GENERAL
#################################################################################


def fnGetTest():
    try:
        ##print("degug ok en fngetTest")
        return {"intResponse": 200, "strAnswer": "Respuesta Exitosa", "jsnAnswer": 7}

    except Exception as e:
        # PrintException()
        return {"intResponse": 500, "strAnswer": "Error en servidor"}
    finally:
        print("mns finallly")


def fnSetDesaparecido(nombre,primape,segape,pais,estado,claveEntidad,municipio,origen,nacionalidad,sexo,fecha_nac,visto_ultima,autoridad,coordenadaX,coordenadaY):
    try:
        MysqlCnx = getConectionMYSQL()
        cursor = MysqlCnx.cursor()
        params = (nombre,primape,segape,pais,estado,claveEntidad,municipio,origen,nacionalidad,sexo,fecha_nac,visto_ultima,autoridad)
        cursor.callproc("sp_setDesaparecido", params)
        MysqlCnx.commit()
        jsonRows = cursor.fetchone()
        print(jsonRows['last_insert_id()'])
        lastID = jsonRows['last_insert_id()']
        params = (lastID,coordenadaX,coordenadaY)
        cursor.callproc("sp_setCoordenadas", params)
        MysqlCnx.commit()
        return {'intResponse': 200, 'strResponse': 'Add person OK'}      
    except Exception as exception:
        print(exception)
        return ({'intResponse': 203, 'strAnswer': "Error en BD"})


def getDesaparecido(id):
    try:
        MysqlCnx = getConectionMYSQL()
        cursor = MysqlCnx.cursor()
        params = (id)
        cursor.callproc("sp_getDesaparecido", [params])
        jsonRow = cursor.fetchall()
        MysqlCnx.commit()  
        return {'intResponse': 200, 'strResponse': jsonRow}      
    except Exception as exception:
        print(exception)
        return ({'intResponse': 203, 'strAnswer': "Error en BD"})
