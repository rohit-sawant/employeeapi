from flask import Flask,jsonify,request,abort,render_template
import json
from flask_restful import Api, Resource, reqparse
import numpy as np
import datetime


app = Flask(__name__)
api = Api(app)

employee =[
 ["Rohit","Sawant","sawant.rohit510@gmai.com","19",datetime.datetime(2020, 5, 17),"8291520420"],
 ["Swati","Sawant","sawant.swati510@gmai.com","20",datetime.datetime(2000, 10, 5),"8976938972"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Shrushit","Sawant","sawant.shrushti@gmai.com","26",datetime.datetime(2000, 5, 17),"7894015263"],
 ["Vishal","kande","vishal.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"1236547890"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"753012569"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","23",datetime.datetime(2000, 5, 17),"9699517660"],
 
]
argsindex = {"firstname":0,"lastname":1,"email":2,"age":3,"dob":4,"mobile":5}

@app.route('/')
def index():
    return jsonify({'videos':employee})

def normalize_query_param(key,value):
    if(len(value)>2):
        abort(400,'please input lower bound and upper bound only')
    elif len(value)==2 and key=="age":
        return value
    elif len(value)==2 and key!="age":
        abort(400,'Cannot filter values by two string!!!............only single value allowed')
    return value[0]

def normalize_query(params):
    params_non_flat = params.to_dict(flat=False)
    ans = {}
    for k,v in params_non_flat.items():
        ans[k] = normalize_query_param(k,v)
    return ans

# @app.errorhandler(500)
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return render_template('500.html'), 404

@app.route('/employee',methods=['POST'])
def findByKeywords():
    val = normalize_query(request.args)
    
    ans = []
    index = 0
    for key in val:
        if key in argsindex:
            if type(val[key]) is not str and key=="age":
                if index==0:
                    temp = [name for name in employee if int(name[3])>=int(val[key][0]) and int(name[3])<=int(val[key][1])]
                else:
                    temp = [name for name in ans if int(name[3])>=int(val[key][0]) and int(name[3])<=int(val[key][1])]
                ans =  temp
            else:
                if index==0:
                    temp = [name for name in employee if name[argsindex[key]]==val[key]]
                else:
                    temp = [name for name in ans if name[argsindex[key]]==val[key]]
                ans =  temp
            index = index+1
        else:
            abort(404,'wrong attributes')
    print(len(ans))
    if len(ans)==0:
        abort(404,'values not found')
    return jsonify({'videos':ans})

   
if __name__ == "__main__":
    app.run(debug=True)
