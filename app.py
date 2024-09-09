# from g4f.client import Client
# import gradio as gr


# client = Client()
# def chatbot_response(user_input):

#     response = client.chat.completions.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": user_input}],
#     )
#     return response.choices[0].message.content

# interface = gr.Interface(
#     fn=chatbot_response,
#     inputs=gr.Textbox(lines=2, placeholder="Câu hỏi cho chat", label="Câu hỏi của bạn", elem_id="input_box"),
#     outputs=gr.Textbox(label="Chat AI", elem_id="output_box"),
#     title="ChatBot AI",
#     # description="hỏi ",
#     theme="compact",  
#     # examples=[["Bạn cần tôi giúp gì?"], 
#     css="""
#     #input_box {
#         border: 2px solid #4CAF50;
#     }
#     #output_box {
#         border: 2px solid #2196F3;
#     }
#     """
# )

# if __name__ == "__main__":
#     interface.launch(share=True) 














import gradio as gr
from g4f.client import Client

client = Client()

def chatbot_response(user_input):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content

css_styles = """
body {
    background: url('aa.jpg') no-repeat center center fixed;
    background-size: cover;
    font-family: "Roboto", sans-serif;
    margin: 0;
    padding: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #98dfdb;
    color: #333;
}

#chat-container {
    width: 100%;
    max-width: 800px;
    height: 90vh;
    display: flex;
    flex-direction: column;
    background-color: #ffffff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

#chat-header {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 15px;
    background-color: #313e49;
    color: #ffffff;
    border-bottom: 1px solid #1f262c;
}

#chat-header h1 {
    font-size: 18px;
    margin: 0;
    font-weight: bold;
}

#chat-content {
    flex-grow: 1;
    padding: 20px;
    overflow-y: auto;
    background-color: #f7f7f7;
    display: flex;
    flex-direction: column;
}

.message {
    max-width: 60%;
    margin-bottom: 15px;
    padding: 10px 15px;
    border-radius: 20px;
    line-height: 1.4;
    word-wrap: break-word;
    display: inline-block;
    white-space: pre-wrap;
    position: relative;
}

.message.user {
    background-color: #0084ff;
    color: #ffffff;
    align-self: flex-end;
    border-bottom-right-radius: 0;
}

.message.bot {
    background-color: #e4e6eb;
    color: #333;
    align-self: flex-start;
    border-bottom-left-radius: 0;
}

#chat-input-container {
    display: flex;
    padding: 10px;
    background-color: #f0f0f0;
    border-top: 1px solid #e0e0e0;
}

#input-box {
    flex-grow: 1;
    background-color: #ffffff;
    color: #333;
    border: 1px solid #e0e0e0;
    border-radius: 20px;
    padding: 12px;
    font-size: 16px;
    outline: none;
    resize: none;
    height: 50px;
    overflow-y: auto;
}

#input-box::placeholder {
    color: #a3a3a3;
}

#send-button {
    background-color: #0084ff;
    color: white;
    border: none;
    padding: 12px 20px;
    margin-left: 10px;
    border-radius: 20px;
    cursor: pointer;
    font-size: 16px;
}

#send-button:hover {
    background-color: #0070e0;
}

/* Code styling */
pre {
    background-color: #2d2d2d;
    color: #f8f8f2;
    padding: 10px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 14px;
    line-height: 1.5;
    max-width: 100%;
    white-space: pre-wrap;
}

.keyword {
    color: #66d9ef;
}

.string {
    color: #e6db74;
}

.function {
    color: #a6e22e;
}

.comment {
    color: #75715e;
    font-style: italic;
}

.number {
    color: #ae81ff;
}

.operator {
    color: #f92672;
}

.punctuation {
    color: #f8f8f2;
}

/* Typing indicator */
.typing {
    display: flex;
    align-items: center;
    margin-bottom: 15px;
    color: #333;
}

.dot {
    height: 8px;
    width: 8px;
    margin: 0 2px;
    background-color: #333;
    border-radius: 50%;
    display: inline-block;
    animation: blink 1.4s infinite both;
}

.dot:nth-child(1) {
    animation-delay: 0s;
}

.dot:nth-child(2) {
    animation-delay: 0.2s;
}

.dot:nth-child(3) {
    animation-delay: 0.4s;
}

@keyframes blink {
    0%, 80%, 100% {
        opacity: 0;
    }
    40% {
        opacity: 1;
    }
}

#back-button {
    position: absolute;
    top: 15px;
    left: 15px;
    font-size: 25px;
    border-radius: 20px;
    background-color: skyblue;
    color: rgb(50, 185, 50);
    border-style: solid;
    padding: 10px 15px;
    cursor: pointer;
}
"""

interface = gr.Interface(
    fn=chatbot_response,
    inputs=gr.Textbox(lines=2, placeholder="Gửi câu hỏi cho Chat", label="Câu hỏi của bạn", elem_id="input-box"),
    outputs=gr.Textbox(label="Chat AI", elem_id="output-box"),
    title="ChatBot AI",
    theme="compact",
    css=css_styles
)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
