from agent.agent import agent


_agent = agent()

while True:
    print(_agent.create_qr_code(input("Enter Text: ")))
