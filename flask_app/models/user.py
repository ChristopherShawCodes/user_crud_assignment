# import the function that will return an instance of a connection
<<<<<<< HEAD
from operator import truediv
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
#email validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
=======
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
>>>>>>> 85c3de3971736d58d5e9ded73ed21d0da4245073


class User:

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #This is a static method to validate a new user's data
    @staticmethod
    def user_is_valid(user_info):
        is_valid = True

        if len(user_info["first_name"]) <= 0:
            flash("First Name Is Required")
            is_valid = False
        if len(user_info["last_name"]) <= 0:
            flash("Last Name Is Required")
            is_valid = False
        if len(user_info["email"]) <= 0:
            flash("Email Is Required")
            is_valid = False
        if not EMAIL_REGEX.match(user_info['email']):
            flash('Email Format Not Valid')
            is_valid = False
        print("Validation: User Is Valid:", is_valid)
        return is_valid




    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users


    #class method to save our friend to the database
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email , created_at, updated_at)VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW() );"
        #data is a dictionary that will be passed into the save method from server.py
        #this return statement would return an integer of the id we just created in the database
        return connectToMySQL('users_schema').query_db(query,data)


    @classmethod
    def get_last(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('users_schema').query_db(query)
        return cls(results[len(results)-1])


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])


    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)