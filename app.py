from flask import Flask,jsonify,request,abort,render_template
import json
from flask_restful import Api, Resource, reqparse
import numpy as np
import datetime


app = Flask(__name__)
api = Api(app)

employee =[
 ["Rohit","Sawant","sawant.rohit510@gmai.com","19",datetime.datetime(2020, 5, 17),"8291520420"],
 ["Bhavesh","Mahase","Mahase.Bhavesh@gmai.com","20",datetime.datetime(2000, 10, 5),"8976938972"],
 ["Adate","Priyanka","Priyanka.adate@gmai.com","50",datetime.datetime(1967, 2, 17),"1236547890"],
 ["Adep","Yeman","Yeman.Adep@gmai.com","60",datetime.datetime(1956, 4, 17),"753012569"],
 ["Akshata","Atpadkar","Atpadkar.Akshata@gmai.com","60",datetime.datetime(1960, 10, 31),"98254672560"],
 ["Priyanka","Kharatmal","Kharatmal.Priyanka@gmai.com","90",datetime.datetime(1940, 12, 1),"9784256310"],
 ["Deep","Solanki","Solanki.Deep@yehoo.com","26",datetime.datetime(1995, 3, 9),"9699717660"],
 ["Sayali","Nagurkar","Nagurkar.Sayali@gmai.com","21",datetime.datetime(1999, 7, 14),"899517660"],
 ["Sandeep","Sawant","sawant.sandeep@gmai.com","31",datetime.datetime(1989, 8, 15),"7856491230"],
 ["Sandeep","Sawant","sawant.sandeep123@gmai.com","36",datetime.datetime(1985, 5, 24),"8456123079"],
 ["Ahmed","Naushad","Ahmed.Naushad@gmai.com","48",datetime.datetime(1973, 9, 25),"7102365498"],
 ["Mandore","Nayak","Nayak.Mandore@gmai.com","25",datetime.datetime(1995, 1, 15),"9699517656"],
 ["Sanket","Nayakwadi","Sanket.Nayakwadi@gmai.com","53",datetime.datetime(1972, 6, 13),"7899517660"],
 ["mihir","Paramar","mihir.Paramar@gmai.com","33",datetime.datetime(1988, 4, 12),"9694561660"],
 ["Jay","Pathare","Jay.Pathare@gmai.com","23",datetime.datetime(1998,8, 10),"8520741963"],
 ["Vaishnavi","Patil","Vaishnavi.Patil@gmai.com","27",datetime.datetime(1994, 3, 31),"7894561230"],
 ["Shrushti","Talekar","Talekar.Shrushti@gmai.com","29",datetime.datetime(1992, 11, 30),"8014725369"],
 ["Rohit","Balu","Balu.Rohit@gmai.com","23",datetime.datetime(1998, 5, 17),"7531594560"],
 ["Soham","Yadav","Soham.Yadav@gmai.com","24",datetime.datetime(1997, 12, 19),"8527419630"],
 ["Shirke","Jaywant","Shirke.Jaywant@gmai.com","33",datetime.datetime(1988, 4, 20),"8032145677"],
 ["Mauyuri","Sonwane","Sonwane.Mauyuri@gmai.com","63",datetime.datetime(1958, 3, 15),"9699517660"],
 ["Sayli","Thoke","Thoke.Sayli@gmai.com","38",datetime.datetime(1983, 7, 3),"8564231230"],
 ["Amey","Shinde","Amey.Shinde@gmai.com","39",datetime.datetime(1982, 6, 2),"8564561230"],
 ["Surbhi","Sable","Surbhi.Sable@gmai.com","19",datetime.datetime(2000, 9, 10),"7894561230"],
 ["Shrushit","Sawant","sawant.shrushti@gmai.com","26",datetime.datetime(1995, 5, 21),"8529674130"],
 ["Rakhi","Rawlo","Rakhi.Rawlo@gmai.com","21",datetime.datetime(1999, 12, 20),"7537537530"],
 ["Pranav","Porkhar","Pranav.Porkhar@gmai.com","22",datetime.datetime(1998, 11, 17),"9564231011"],
 
 
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

@app.route('/employee')
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
