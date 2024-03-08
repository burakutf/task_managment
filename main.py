import requests

# Önce oturum açma isteği yapalım
login_data = {"username": "root", "password": "root"}
response = requests.post('http://localhost:8000/login/', json=login_data)
if response.status_code == 200:
    token = response.json()['token']
    print("Oturum açma başarılı. Token:", token)

    # Oturum açma başarılıysa, görev oluşturma isteği yapalım
    create_task_data = {
        "dual_assignee": "John Doe",
        "labels": "bug",
        "due_date": "2024-03-10",
        "priority": 1,
        "description": "Fix authentication bug"
    }
    headers = {"Authorization": f"Token {token}"}
    create_task_response = requests.post('http://localhost:8000/tasks/create/', json=create_task_data, headers=headers)
    print("Görev oluşturma isteği:", create_task_response.status_code)
    print("Görev oluşturma yanıtı:", create_task_response.json())

    # Ayrıca, bir görevi güncelleme isteği yapalım
    update_task_id = 1  # Güncellenecek görevin kimliği
    update_task_data = {
        "dual_assignee": "Jane Smith",  # Güncellenmiş bilgiler
        "labels": "feature",
        "due_date": "2024-03-12",
        "priority": 2,
        "description": "Implement new feature"
    }
    update_task_response = requests.put(f'http://localhost:8000/tasks/{update_task_id}/update/', json=update_task_data, headers=headers)
    print("Görev güncelleme isteği:", update_task_response.status_code)
    print("Görev güncelleme yanıtı:", update_task_response.json())

    # Son olarak, bir görevi silme isteği yapalım
    delete_task_id = 2  # Silinecek görevin kimliği
    delete_task_response = requests.delete(f'http://localhost:8000/tasks/{delete_task_id}/delete/', headers=headers)
    print("Görev silme isteği:", delete_task_response.status_code)
    print("Görev silme yanıtı:", delete_task_response.json())

else:
    print("Oturum açma başarısız.")
