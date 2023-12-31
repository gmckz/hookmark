from datetime import datetime
import json
"""
When I make a GET request to /projects/:id with a valid id
I get a 200 response and the name, link and notes are returned for that project as a dict
"""
def test_get_a_project(db_connection, web_client):
    db_connection.seed('seeds/hookmark_database.sql')
    response = web_client.get('/projects/1')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')) == {"id": 1, "name": "cable knit hat", "link": "www.test.com", "notes": "test note"}

"""
When I make a GET request to /projects/:id with an invalid
I get a 404 reponse and error message
"""
def test_get_a_project_invalid_id(db_connection, web_client):
    db_connection.seed('seeds/hookmark_database.sql')
    response = web_client.get('/projects/7')
    assert response.status_code == 404
    assert json.loads(response.data.decode('utf-8')) == {"error": "Project with id: 7 does not exist."}
"""
When I make a GET request to /projects
I get a 200 response and a list of projects is returned
"""
def test_get_all_projects(db_connection, web_client):
    db_connection.seed('seeds/hookmark_database.sql')
    response = web_client.get('/projects')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')) == {
        "projects": [
            {
                "id": 1,
                "name": 'cable knit hat',
                "link": 'www.test.com',
                "notes": 'test note',
            },
            {
                "id": 2,
                "name": 'jumper',
                "link": 'www.test.com',
                "notes": 'test note 2',
            },
            {
                "id": 3,
                "name": 'cardigan',
                "link": 'www.test.com',
                "notes": 'test note 3',
            },
        ]}

"""
When I make a POST request to /projects with a valid project
I get a 200 response and success message
"""
def test_create_a_project(db_connection, web_client):
    db_connection.seed("seeds/hookmark_database.sql")
    data={
        'data': {'name': 'New project', 'link':'www.test.com', 'notes': 'i\'m creating a new project'}
        }
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    response = web_client.post('/projects', data=json_data, headers=headers)
    assert response.status_code == 201
    assert json.loads(response.data.decode('utf-8')) == {"id":4,"link":"www.test.com","name":"New project","notes":"i\'m creating a new project"}

"""
When I make a POST request to /projects with an invalid project
I get a 400 response and error message
"""
def test_create_a_project_invalid(db_connection, web_client):
    db_connection.seed("seeds/hookmark_database.sql")
    data={
        'data': {'name': '', 'link':'', 'notes': 'i\'m creating an invalid project'}
        }
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    response = web_client.post('/projects', data=json_data, headers=headers)
    assert response.status_code == 400
    assert json.loads(response.data.decode('utf-8')) == {"error": "Error: name and link must have a value"}


"""
When I make a PUT request to /projects with a valid project
I get a 200 response and the updated project
"""
def test_update_a_project(db_connection, web_client):
    db_connection.seed("seeds/hookmark_database.sql")
    data={
        'data': {'id': 3, 'name': 'updated project', 'link':'www.test.com', 'notes': 'i\'m updating a project'}
        }
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    response = web_client.put('/projects', data=json_data, headers=headers)
    assert response.status_code == 200    
    assert json.loads(response.data.decode('utf-8')) == {"id":3,"link":"www.test.com","name":"updated project","notes":"i\'m updating a project"}

"""
When I make a PUT request to /projects with an invalid project
I get a 400 response and an error message
"""
def test_update_a_project_invalid(db_connection, web_client):
    db_connection.seed("seeds/hookmark_database.sql")
    data={
        'data': {'id': 3, 'name': '', 'link':'www.test.com', 'notes': 'i\'m updating a project'}
        }
    headers = {'Content-Type': 'application/json'}
    json_data = json.dumps(data)
    response = web_client.put('/projects', data=json_data, headers=headers)
    assert response.status_code == 400    
    assert json.loads(response.data.decode('utf-8')) == {"error": "Error: name must have a value"}

"""
When I make a DELETE request to /projects with a valid project id
I get a 200 response
"""
def test_delete_a_project(db_connection, web_client):
    db_connection.seed("seeds/hookmark_database.sql")
    response = web_client.delete('/projects/1')
    assert response.status_code == 200
    assert json.loads(response.data.decode('utf-8')) == {"message": "Project deleted successfully"}

"""
When I make a DELETE request to /projects with an invalid project id
I get a 404 response and error message
"""
def test_delete_a_project_invalid(db_connection, web_client):
    db_connection.seed("seeds/hookmark_database.sql")
    response = web_client.delete('/projects/7')
    assert response.status_code == 404
    assert json.loads(response.data.decode('utf-8')) == {"error": "Project with id: 7 does not exist."}
