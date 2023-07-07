import psycopg2
import os
import json
from psycopg2.extras import RealDictCursor
from flask import make_response



class user_model():
    def __init__(self):
        try:
            # Replace the placeholders with your actual database credentials
            self.conn = psycopg2.connect(
                    host="localhost",
                    port= "5432",
                    database="postgres",
                    user="postgres",
                    password= os.environ.get("PASSWORD")
                    )
            self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            print("connection successful")
        except Exception as e:
            print(e)
    def user_signup_model(self):
        return 'This is signup model'
    
    def get_user_all(self):
        self.cursor.execute('Select * from users')
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            return make_response({'payload':rows},200)
        else:
            return make_response({'message':'No data found'},204)
        
    def add_one_user(self,data): 
        try:  
            self.cursor.execute(f"INSERT INTO Users (name, email, phone, role, password) VALUES ('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
            self.conn.commit()
            return make_response({'message':'User one added successfully'},200)
        except Exception:
            return make_response({"message":"Sum error occured"},400)

    def update_user(self,data):
        keys = list(data.keys())
        try:
            
            self.cursor.execute(f"UPDATE Users SET {keys[0]} = %s WHERE {keys[0]} = %s", (data[keys[1]], data[keys[0]]))
            if self.cursor.rowcount > 0:
                self.conn.commit()
                return make_response({'message': "User Updated successfully"},201)
            else:
                return make_response({'message':"Nothing to update"},204)
        except Exception as e:
            return "Some error occured"
        
    def delete_user(self,id):
        try:
            self.cursor.execute(f"DELETE from Users where id = %s" ,(id))
            if self.cursor.rowcount > 0:
                self.conn.commit()
                return make_response({"message":"User deleted successfully"},200)
            else:
                return {"message":"Nothing to delete"}
        except:
            return "Some error occured"




    
    

    
