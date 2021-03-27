import requests
import base64


class API_REST:
    def inputGate(self,card_id,gate):
<<<<<<< HEAD
        url = f'http://18.213.76.34/output/{card_id}'
        print(f'INPUT[] URL {url} gate={gate} card_id={card_id}')

        return requests.put(url,json={"gate":gate},verify=False).json()
=======
        url = f'http://18.213.76.34/registroRfid/{card_id}'
        print(f'INPUT[] URL {url} gate={gate} card_id={card_id}')

        return requests.post(url,json={"gate":gate},verify=False).json()
>>>>>>> 9a2b325974ad9898b48e49174c0c788cfb31d455
    
    def outputGate(self,card_id,gate):
        url = f'http://18.213.76.34/output/{card_id}'
        print(f'OUTPUT:[] URL {url} gate={gate} card_id={card_id}')

        response = requests.put(url,json={"gate":gate},verify=False).json()
        print(response)

#api = API_REST()
#api.inputGate("0008949774",2)
