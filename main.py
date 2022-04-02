from website import create_app
from website.DAO.CRUD import *
from website.DAO.SendMail import *
from website.DAO.UploadCSV import *
from website.SERVICE.Service import GetOneUserJSON, GetUsersJSON


app = create_app()


@app.route('/getURLfile', methods=['POST'])
def getURLfile():
    return getURLfilefunction()


@app.route('/getAllUsers', methods=['GET'])
def getAllUsers():
    return GetUsersJSON(getAllUsersfunction())


@app.route('/getUserById', methods=['GET'])
def getUserById():
    return GetOneUserJSON(getUserByIdfunction())


@app.route('/DeleteUserById', methods=['DELETE'])
def DeleteUserById():
    return DeleteUserByIdfunction()


@app.route('/DeleteAll', methods=['DELETE'])
def DeleteAll():
    return DeleteAllfunction()


@app.route('/AddUser', methods=['POST'])
def AddUser():
    return AddUserfunction()


@app.route('/UpdateUser', methods=['POST'])
def UpdateUser():
    return UpdateUserfunction()


@app.route('/SendMail', methods=['POST'])
def SendMail():
    return SendMailfunction()


if __name__ == '__main__':
    app.run(debug=True)
