from apis import app
import logger
import jobs
import database

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)