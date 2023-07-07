from app import app

@app.route('/pcat/addNew')
def add_new_cat():
    return "New product category added successfully."