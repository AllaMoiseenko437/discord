import pytest
import requests
import config

headers = {'Authorization': config.api_key,
        'Content-Type': 'application/x-www-form-urlencoded'
         }
@pytest.mark.parametrize("emoji", ["🔥", "😊", "🎉", "❤️"])
def test_create_message(emoji):
    data = {
        'content': "тест"
    }
    # Создание сообщения
    create_message = requests.post(f'{config.base_url}/channels/{config.chanel_id}/messages', headers=headers, data=data)

    assert create_message.status_code == 200, f"Unexpected status code: {create_message.status_code}"
    response_json = create_message.json()
    assert 'content' in response_json, "Response does not contain 'content' key"
    assert response_json['content'] == "тест", f"Expected content 'тест', but got {response_json['content']}"

    message_id = response_json['id']
    print(f'Message ID: {message_id}')

    # Просмотр сообщения
    get_message = requests.get(f'{config.base_url}/channels/{config.chanel_id}/messages/{message_id}', headers=headers)

    assert get_message.status_code == 200, f"Unexpected status code when fetching message: {get_message.status_code}"
    message_response = get_message.json()
    assert message_response['id'] == message_id, f"Expected message ID {message_id}, but got {message_response['id']}"
    print("Response JSON:", message_response)

    #Добавление реакции
    add_reaction_url = f"{config.base_url}/channels/{config.chanel_id}/messages/{message_id}/reactions/{emoji}/@me"

    add_reaction = requests.put(add_reaction_url, headers=headers)
    assert add_reaction.status_code in [204], f"Unexpected status code when adding reaction: {add_reaction.status_code}"

    #Удаление реакции
    remove_reaction = requests.delete(f"{config.base_url}/channels/{config.chanel_id}/messages/{message_id}/reactions/{emoji}/{config.user_id}", headers=headers)

    assert remove_reaction.status_code in [
        204], f"Unexpected status code when removing reaction: {remove_reaction.status_code}"

    #Удаление сообщения
    delete_message = requests.delete(f'{config.base_url}/channels/{config.chanel_id}/messages/{message_id}', headers=headers)
    assert delete_message.status_code == 204, f"Unexpected status code when fetching message: {get_message.status_code}"


