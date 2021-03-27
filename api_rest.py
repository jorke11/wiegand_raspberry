import requests
import base64


class API_REST:
    def inputGate(self,card_id,gate):
        url = f'http://18.213.76.34/output/{card_id}'
        print(f'INPUT[] URL {url} gate={gate} card_id={card_id}')

    
    def outputGate(self,card_id,gate):
        url = f'http://18.213.76.34/output/{card_id}'
        print(f'OUTPUT:[] URL {url} gate={gate} card_id={card_id}')

        response = requests.put(url,json={"gate":gate},verify=False).json()
        print(response)

#api = API_REST()
#api.inputGate("0008949774",2)
