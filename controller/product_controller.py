from app import app

@app.route('/product/add')
def product_add():
    return "Product added successfully."