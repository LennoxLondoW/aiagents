from dotenv import load_dotenv
import google.generativeai as genai
import os
from agent.tools import create_qr_code

load_dotenv()

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
class agent:
    system_instructions = """
    You are a helpful assistant. Your task is to generate QR codes for any content given.
    """
    def create_qr_code(self, data):
        try: 
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                tools=[create_qr_code],
                system_instruction=self.system_instructions
            )
            
            chat = model.start_chat(
                enable_automatic_function_calling=True,
                history=[]
            )
            
            response = chat.send_message(f"generate a qr code for this content: {data}")
            return response.text
        except Exception as e:
            print(e)
            return "Failed to generate qr code"