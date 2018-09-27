from flask import Flask, jsonify, request,abort
app = Flask(__name__)


entries =[ ]

#to fetch all diary entries i.e GET/entries
@app.route("/api/v1/entries/", methods=['GET'])
def get_all_entries():
 return jsonify({'entries': entries})

#to create a diary entry i.e POST/entries
@app.route("/api/v1/entries/", methods=['POST'])
def create_entry():
 if not request.json or not 'name' in request.json:
  abort(400)
    
 entry = {
  'id': request.json.get("id", ""),
  'name':request.json['name']
 }
 entries.append(entry)
 return jsonify({'entry':entry}),201


#to fetch a specific diary entry i.e GET/entries/<entry id>
@app.route("/api/v1/entries/<id>", methods=['GET'])
def get_entry(id):
  for entry in entries:
   if entry['id'] == id:
      
    return jsonify ({'entries': entry})
  return jsonify ({'message':'entry not found'})
 

#to modify a diary entry i.e PUT/entries/<entryId>
@app.route("/api/v1/entries/<id>", methods=['PUT'])
def modify_entry(id):
    request_data = request.get_json()
    for entry in entries:
      if entry['id'] == id:
        entry['id'] = request_data['id']
        entry['name'] = request_data['name']
     
      return jsonify ({'entries':'success'}), 200
    return jsonify({'message':'entry not found'})


 
if __name__ =='__main__':
 app.run(debug=True)









