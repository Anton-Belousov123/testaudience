import json

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Sample data for plaques
plaques = [
    {
        'id': 1,
        'name': 'Plaque 1',
        'x': 50,
        'y': 100
    },
    {
        'id': 2,
        'name': 'Plaque 2',
        'x': 150,
        'y': 200
    },
    {
        'id': 3,
        'name': 'Plaque 3',
        'x': 250,
        'y': 300
    }
]




@app.route('/')
def test():
    return render_template('index.html')

# API endpoint for getting plaques data
@app.route('/plaques')
def get_plaques():
    print('yes')
    return jsonify(plaques)

# API endpoint for updating plaque position
@app.route('/update_position', methods=['POST'])
def update_position():
    # Get the id of the plaque to update and its new position
    plaque_id = int(request.form.get('id'))
    new_x = request.form.get('left').replace('px', '')
    new_y = request.form.get('top').replace('px', '')
    new_x = float(new_x)
    new_y = float(new_y)

    # Update the position of the plaque in the plaques list
    for plaque in plaques:
        if plaque['id'] == plaque_id:
            plaque['x'] = new_x
            plaque['y'] = new_y
            break
    with open('buttons.json', 'w', encoding='UTF-8') as f:
        f.write(json.dumps(plaques))
    f.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
