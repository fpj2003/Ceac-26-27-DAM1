from flask import Flask, render_template, request

import mysql.connector

connection = mysql.connector.connect(
    host='examendamceac2627',
    user='examendamceac2627',
    password='CEACExamenDAM123$',
    database='examendamceac2627'
)

