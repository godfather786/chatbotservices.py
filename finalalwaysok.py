from flask import Flask, request, jsonify,json
from flask_restful import Resource, Api
import pymysql
from db_con import local

app = Flask(__name__)
api = Api(app)


def fun():
    try:
        f1 = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            connect_timeout=120
        )
        if f1.cursor():
            print("success")
            f1.commit()
            return f1
    except NameError:
        return "DENIED"


class API(Resource):
    def post(API):
        output = request.get_json()
        query = output['query'].lower()
        email = str(output['email']).lower()
        match query:
            case "Applications"|"applications":
                l1 = local()
                l1.cursor()
                mycursor = l1.cursor()
                sql1 = "select application_id , application_name from application_list"
                mycursor.execute(sql1)
                record1 = mycursor.fetchall()
                sql3 = "select application_id from application_list"
                mycursor.execute(sql3)
                result = []
                for row in record1:
                    d = dict()
                    d['application_id '] = row[0]
                    d['application_name'] = row[1]
                    result.append(d)
                return jsonify({"applications":result})
            case other:
                if query <= str(query.startswith('')):
                    print(query)
                    l1 = local()
                    mycursor = l1.cursor()
                    sql3 = "select application_id from application_list"
                    mycursor.execute(sql3)
                    record5 = mycursor.fetchall()
                    record5 = str(record5)
                    if query in record5:
                        l1 = local()
                        mycursor = l1.cursor()
                        sql2 = "select title , fkey from function_list where application_id = %s "
                        mycursor.execute(sql2, [query])
                        record2 = mycursor.fetchall()

                        if query <= str(query.startswith('')):
                            l1 = local()
                            sql = "select password from application_list where application_id = %s "
                            mycursor = l1.cursor()
                            mycursor.execute(sql, [query])
                            result = mycursor.fetchall()
                            global password
                            password= str(result)[3:-5]
                            print(password)
                            sql1 = "select server_ip from application_list where application_id = %s "
                            mycursor = l1.cursor()
                            mycursor.execute(sql1, [query])
                            result = mycursor.fetchall()
                            global host
                            host = str(result)[3:-5]
                            print(host)
                            sql = "select user from application_list where application_id = %s "
                            mycursor = l1.cursor()
                            mycursor.execute(sql, [query])
                            result = mycursor.fetchall()
                            global user
                            user = str(result)[3:-5]
                            print(user)

                            sql = "select database_name from application_list where application_id = %s "
                            mycursor = l1.cursor()
                            mycursor.execute(sql, [query])
                            result = mycursor.fetchall()
                            global database
                            database = str(result)[3:-5]
                            print(database)
                            fun()
                            res = []
                            for row in record2:
                                d = dict()
                                d['title'] = row[0]
                                d['fkey'] = row[1]
                                res.append(d)
                            return jsonify({"functions":res})

                    else:
                        return jsonify({"message": 'NO ID FOUND'})
                elif query.startswith(''):
                    q1 = str(query).upper()
                    l1 = local()
                    mycursor=l1.cursor()
                    sql3="select fkey from function_list"
                    mycursor.execute(sql3)
                    record3 = str(mycursor.fetchall())
                    if q1 in record3:
                        fx = fun()
                        print(fx)

                        if fx == "DENIED":
                            return jsonify({"message": "PLEASE TYPE RESPECTIVE APPLICATION_ID"})
                        else:
                            sql4 = "select query from function_list where fkey = %s"
                            mycursor.execute(sql4, [query])

                            record4 = str(mycursor.fetchall())
                            result1 = (record4.replace('flag', email))
                            result2 = result1[3: -5]
                            mycursor_1 = fx.cursor()
                            mycursor_1.execute(result2)
                            record5 = str(mycursor_1.fetchall())
                            record55 = record5.strip("[(,)]")
                            print(record55)
                            result = {"result": record55,
                                      "message": ""}
                            return jsonify(result)
                    else:
                        return jsonify({"message": "Type Correct Function id"})


api.add_resource(API, '/api/sendRequest')
app.run( debug=True)