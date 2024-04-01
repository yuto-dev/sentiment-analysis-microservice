import logging
import requests
from datetime import datetime as rolex
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

telegramBotToken = "REPLACE WITH ACTUAL TOKEN"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def callGPT(prompt):
    # Define the URL
    url = "http://localhost:8001/v1/completions"
    # Define the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Define the data
    data = {
        "prompt": prompt,
        "stream": False,
        "use_context": True,
        "system_prompt": "Kamu adalah LibraryAI. Kamu adalah AI LLM yang memiliki akses ke database literatur fisik. Gunakan literatur ini untuk menjawab pertanyaan yang diajukan padamu. Jika kamu tidak dapat menemukan jawabannya dalam informasi tersebut, katakan saja bahwa kamu tidak yakin dan berikan perkiraan tentang apa yang kamu pikirkan sebagai jawabannya, pastikan untuk memberi tahu pengguna bahwa ini adalah tebakan terbaikmu dan tidak 100 persen benar."
    }

    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    # Check if the request was successful
    if response.status_code ==  200:
        # Parse the JSON response
        response_data = response.json()
        jsonContent = response_data.keys()
        # Extract choices key
        choices = response_data.get('choices')
        #--------------------------------------------
        #Extract content
        message = choices[0].get('message')
        content = message.get('content')
        print(content)
        #--------------------------------------------
        sources = choices[0].get('sources')
    
        i = 0
        sourcesList = []
        for entry in sources:
            document = sources[i].get('document')
            doc_metadata = document.get('doc_metadata')
            page_label = doc_metadata.get('page_label')
            file_name = doc_metadata.get('file_name')
        
            number = str(i + 1)
            formattedSource = number + ". " + file_name + " (page " + page_label + ")"
            sourcesList.append(formattedSource)
            i = i + 1
        
        i = 0
        for source in sources:
            print(sourcesList[i])
            i = i + 1  
    
    else:
        print("Request failed with status code:", response.status_code)
    
    return content, sourcesList

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
async def prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Extract the argument from the command
    argument = ' '.join(context.args)
    startTime = rolex.now()
    
    notificationMessage = "*Processing prompt:* \n" + argument + "\n\n" + "*Time start: " + startTime.strftime("%Y-%m-%d %H:%M:%S") + " (GMT +7)*"
    # Process the argument as needed
    await context.bot.send_message(chat_id=update.effective_chat.id, text=notificationMessage, parse_mode='Markdown')
    
    gptResult, gptSource = callGPT(argument)
    formattedResponse = "*Replying to:*\n" + argument + "\n" + "*Response:*\n" + gptResult + "\n"
    formattedSource = "*Source:*\n" + gptSource[0] + "\n" + gptSource[1] + "\n"
    endTime = rolex.now()
    
    stopTime = "*Time stop: " + endTime.strftime("%Y-%m-%d %H:%M:%S") + " (GMT +7)*"
    
    diffTime = endTime - startTime
    
    # Assuming diffTime is a timedelta object
    hours, remainder = divmod(diffTime.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format the time taken
    timeTaken = "*Time taken: {:02}:{:02}:{:02} (HH:MM:SS)*".format(int(hours), int(minutes), int(seconds))

    
    responseMessage = formattedResponse + "\n" + formattedSource + "\n" + stopTime + "\n" + timeTaken
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=responseMessage, parse_mode='Markdown')

if __name__ == '__main__':
    application = ApplicationBuilder().token(telegramBotToken).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    # Add the new /prompt command handler
    prompt_handler = CommandHandler('prompt', prompt)
    application.add_handler(prompt_handler)
    
    application.run_polling()