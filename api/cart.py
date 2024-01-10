#!C:/Users/Admin/AppData/Local/Programs/Python/Python312/python.exe

import api_controller

import json

import logging

import sys

sys.path.append('../../')

import dao



class CartController( api_controller.ApiController ) :

    def do_post( self ) :
         user_id = dao.Auth().get_user_id(self.get_bearer_token_or_exit())

         self.send_response( 200, "OK",

                meta={ "service": "cart", "count": 1, "status": 200 },

                data={"token": user_id} )





CartController().serve()