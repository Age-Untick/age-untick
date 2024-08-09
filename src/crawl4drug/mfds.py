#!/usr/bin/env python3
# Get medicine data from MFDS (Ministry of Food and Drug Safety of the Republic of Korea)
import os
import requests
from dotenv import load_dotenv, dotenv_values

load_dotenv()

mfds_key = os.getenv("MFDS_API_KEY_DEC")
mfds_url = os.getenv("MFDS_API_URL")

params = {
    'serviceKey': mfds_key, # API key
    'pageNo': '1', # page number 페이지 번호
    'numOfRows': '3', # number of rows 한 페이지 결과 수
    'entpName': '', # enterprise name 업체명
    'itemName': '', # item name 제품명
    'itemSeq': '', # item sequence 품목 기준 코드
    'efcyQesitm': '', # 이 약의 효능은 무엇입니까?
    'useMethodQesitm': '', # 이 약은 어떻게 사용합니까?
    'atpnWarnQesitm': '', # 이 약을 사용하기 전에 반드시 알아야 할 내용은 무엇입니까?
    'atpnQesitm': '', # 이 약의 사용상 주의사항은 무엇입니까?
    'intrcQesitm': '', # 이 약을 사용하는 동안 주의해야 할 약 또는 음식은 무엇입니까?
    'seQesitm': '', # 이 약은 어떤 이상반응이 나타날 수 있습니까?
    'depositMethodQesitm': '', # 이 약은 어떻게 보관해야 합니까?
    'openDe': '', # 공개일자
    'updateDe': '', # 수정일자
    'type': 'json' # xml or json
}

response = requests.get(mfds_url, params=params)
print(response.content)