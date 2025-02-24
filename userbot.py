from telethon import TelegramClient, events

# Replace with your actual API credentials (Keep them secret!)
API_ID = 9667475  # No quotes around the number
API_HASH = "67615543912ab08b610a25cdf511a25f"  # Keep quotes around the hash

client = TelegramClient("session_name", API_ID, API_HASH)

# Store user choices temporarily
user_choices = {}

@client.on(events.NewMessage)
async def handle_message(event):
    print(f"Received a message: {event.raw_text}")  # Debugging print

    # Welcome message when user sends /start
    if event.raw_text == "/start":
        await event.respond("Welcome! We provide state-of-the-art electrical solutions.\n\n"
                            "Please choose a service by replying with a number:\n"
                            "1️⃣ Electric Vehicle Charger Installation/Maintenance\n"
                            "2️⃣ Solar Panel Systems Installation\n"
                            "3️⃣ Battery Backup System and UPS\n"
                            "4️⃣ Air Conditioning System (AC)\n"
                            "5️⃣ CNC Machine\n"
                            "6️⃣ Other Electrical Electromechanical Solutions")

    # If the user selects a service
    elif event.raw_text in ["1", "2", "3", "4", "5", "6"]:
        user_choices[event.chat_id] = event.raw_text  # Save their choice
        await event.respond("Please drop your contact phone number so we can communicate with you.")

    # If the user sends a phone number (basic validation)
    elif event.raw_text.startswith("+") or event.raw_text.isnumeric():
        service = user_choices.get(event.chat_id, "Unknown Service")
        await event.respond(f"Thank you! We will contact you shortly regarding {service}.")

# Start the bot
client.start()
print("Bot is running...")  # To confirm it's working
client.run_until_disconnected()
