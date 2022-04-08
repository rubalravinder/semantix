from main import app, index
 
if __name__ == "__main__":
    increment_id = index()
    id = next(increment_id)
    app.run()