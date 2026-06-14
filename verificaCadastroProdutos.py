import os
import glob
import apiibm
import unicodedata
import time
import psycopg2
import mysql.connector
from datetime import datetime
import locale
import smtplib
from json import dumps
from httplib2 import Http
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logExecucaoCodigos import grava_log_execucao_sql

def envia_email():
    pass # Logica de negocio removida por seguranca corporativa


def conecta_sql():
    pass # Logica de negocio removida por seguranca corporativa

def conecta_pg(sql):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_pg_sql_insert(sql):
    pass # Logica de negocio removida por seguranca corporativa

def retorna_google_chat(mensagem):
    pass # Logica de negocio removida por seguranca corporativa



def remover_diacriticos(texto):
    pass # Logica de negocio removida por seguranca corporativa
