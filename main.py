data_set = {'data': { 'rooms': 
    [ { 'id': 1, 'room_number': "201", 'capacity': 50}, { 'id': 2, 'room_number': "301", 'capacity': 200 }, { 'id': 3, 'room_number': "1B", 'capacity': 100}
    ],
    'events': [
      { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
      { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
      { 'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20 },
      { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
    ]
  }
}


room_201 = data_set['data']['rooms'][0]['room_number']


def get_capacity(): 
    if room_201 == '201': 
        room_201_capacity = data_set['data']['rooms'][0]['capacity']
    return room_201_capacity

# print(get_capacity())


dd = data_set['data']['events']
for list_item in dd:
    if list_item['room_id'] == 1:
        if list_item['attendees'] <= get_capacity(): 
            print('yes') 
        else: 
            print('Please find another venue!')



