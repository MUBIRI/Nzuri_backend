from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('Mubiri')
    track = request.args.get('Backend')
    
    # Get the current UTC time
    utc_now = datetime.datetime.utcnow()
    
    # Calculate the time with a +/-2 minute window
    time_with_window = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # GitHub URLs
    github_file_url = "https://github.com/MUBIRI/Nzuri_backend/blob/main/app.py"
    github_repo_url = "https://github.com/MUBIRI/Nzuri_backend.git"
    
    response_data = {
        "slack_name": 'Mubiri',
        "current_day": utc_now.strftime("%A"),
        "utc_time": time_with_window,
        "track": 'backend',
        "github_file_url": "https://github.com/MUBIRI/Nzuri_backend/blob/main/app.ext",
        "github_repo_url": "https://github.com/MUBIRI/Nzuri_backend.git",
        "status_code": 200
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)