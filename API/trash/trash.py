# @app.route('/getCSV', methods=['GET'])
# def getCSV():
#     URL = request.args.get('CSV')
#     f = open(URL)
#     fichierCSV = csv.reader(f)
#     for ligne in fichierCSV:
#         new_store = {
#             'name': ligne[0],
#             'prenom': ligne[1],
#             'Adresse': ligne[2],
#             'email': ligne[3],
#             'P/NP': ligne[4]
#         }
#         stores.append(new_store)
#     return jsonify(stores)
