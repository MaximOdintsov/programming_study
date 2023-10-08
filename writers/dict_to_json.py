import json

dct = {'full_name_c': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ \nОТВЕТСТВЕННОСТЬЮ "ТЕХКО"', 'discharge_date_c': '2023-07-26', 'inn_c': '7751258359', 'ogrn_c': '1237700427997', 'registration_date_c': '2023-06-22', 'address_c': '117041,\nГ.Москва,\nВН.ТЕР.Г. ПОСЕЛЕНИЕ СОСЕНСКОЕ,\nП КОММУНАРКА,\nУЛ ПОТАПОВСКАЯ РОЩА,\nД. 3, К. 1,\nПОМЕЩ. 62П', 'termination_ul_ip_c': 'not_confirmed', 'capital_c': '10000', 'charter_number_c': '20', 'main_activity_c': '77.32 Аренда и лизинг строительных\nмашин и оборудования', 'executive_agency': [{'name': 'ГАДЗЕБУЛАДЗЕ\nЮРИЙ\nЮРЬЕВИЧ', 'inn_c': '614100286730', 'eio_date_begin_c': '2023-06-22', 'position_c': 'ГЕНЕРАЛЬНЫЙ ДИРЕКТОР'}], 'shareholders_participants': [{'name': 'ГАДЗЕБУЛАДЗЕ ЮРИЙ ЮРЬЕВИЧ', 'inn_c': '614100286730', 'percent_size_c': '50', 'path_amount_c': '5000'}, {'name': 'БЕЛОУСОВ АЛЕКСАНДР ЮРЬЕВИЧ', 'inn_c': '614105288918', 'percent_size_c': '50', 'path_amount_c': '5000'}]}

json_ = json.dumps(dct, indent=4, ensure_ascii=False)
print(json_)
