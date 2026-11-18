from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/backtest', methods=['POST'])
def backtest():
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No JSON data received'}), 400
    
    # Example: just echo back what was sent (replace with real logic)
    return jsonify({
        'message': 'Backtest received',
        'received_data': data
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)