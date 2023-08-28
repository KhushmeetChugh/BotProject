import telebot
bot=telebot.TeleBot("6011058822:AAGZXVLiALGmMZEsCJ0WneAx8AHoE12ta6s")
@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.reply_to(message,"Hello! Welcome to NIT Kurukshetra's bot")

@bot.message_handler(func=lambda message:message.text.lower()=='start')
def handle_start(message):
    bot.reply_to(message,"Hello! Welcome to NIT Kurukshetra's bot")



@bot.message_handler(commands=["help"])
def handle_start(message):
    bot.reply_to(message,"Here's what I can do\n /start to start the bot\n")



@bot.message_handler(commands=["Contact"])
def handle_message(message):
    bot.reply_to(message,"/Instagram\n/LinkedIn")

@bot.message_handler(commands=["Instagram"])
def handle_message(message):
    bot.reply_to(message,"https://instagram.com/khushmeetchugh?igshid=MzNlNGNkZWQ4Mg==")

#Academic help
@bot.message_handler(func=lambda message:message.text.lower()=='academics')
def handle_message(message):
    bot.reply_to(message,"/1stYear")

@bot.message_handler(commands=["1stYear"])
def handle_message(message):
    bot.reply_to(message,"/PreviousYear\n/Notes")

@bot.message_handler(commands=["PreviousYear"])
def handle_message(message):
    bot.reply_to(message,"/MathsSem1\n/PSPS\n/English\n/PhysicsSem1\n/EnvironmentSem1\n/EP\n/MathsSem2\n/Economics\n/DSD\n/DSA")
@bot.message_handler(commands=["MathsSem1"])
def handle_message(message):
    bot.reply_to(message,"/MathsSem1MidSem1\n/MathsSem1MidSem2\n/MathsSem1EndSem")

@bot.message_handler(commands=["MathsSem1MidSem1"])
def handle_message(message):
    file1_path="MAIR11 2017.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 2018.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 Jan 2021 (EC, ME, PI) .pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 Jan 2021 (CE, CS, EE, IT).pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 Jan 2022.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)


@bot.message_handler(commands=["MathsSem1MidSem2"])
def handle_message(message):
    file1_path="MAIR11 2017B.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 Feb 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["MathsSem1EndSem"])
def handle_message(message):
    file1_path="MAIR11 Dec 2017 Reappear (Old Scheme).pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 Nov 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 Dec 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 Nov 2017.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 Mar 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 Dec 2017.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR11 Nov 2018 Reappear (Old scheme).pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)


@bot.message_handler(commands=["MathsSem2"])
def handle_message(message):
    bot.reply_to(message,"/MathsSem2MidSem1\n/MathsSem2MidSem2\n/MathsSem2EndSem")

@bot.message_handler(commands=["MathsSem2MidSem1"])
def handle_message(message):
    file1_path="MAIR12 Apr 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["MathsSem2MidSem2"])
def handle_message(message):
    file1_path="MAIR12 May 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)



@bot.message_handler(commands=["MathsSem2EndSem"])
def handle_message(message):
    file1_path="MAIR12 Dec 2019 (Old Scheme).pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR12 Dec 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MAIR12 Jun 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)


@bot.message_handler(commands=["EnvironmentSem1"])
def handle_message(message):
    bot.reply_to(message,"/EnvironmentSem1MidSem1\n/EnvironmentSem1MidSem2\n/EnvironmentSem1EndSem")

@bot.message_handler(commands=["EnvironmentSem1MidSem1"])
def handle_message(message):
    file1_path="CHIR11 2017.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CHIR11 2018.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CHIR11 Jan 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["EnvironmentSem1MidSem2"])
def handle_message(message):
    file1_path="CHIR11 20XX.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CHIR11 2018B.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CHIR11 Feb 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["EnvironmentSem1EndSem"])
def handle_message(message):
    file1_path="CHIR11 Dec 2017.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CHIR11 Dec 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CHIR11 Dec 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CHIR11 Mar 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)


@bot.message_handler(commands=["PhysicsSem1"])
def handle_message(message):
    bot.reply_to(message,"/PhysicsSem1MidSem1\n/PhysicsSem1MidSem2\n/PhysicsSem1EndSem")

@bot.message_handler(commands=["PhysicsSem1MidSem1"])
def handle_message(message):
    file1_path="PHIR11 2018.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="PHIR11 Jan 2022.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="PHIR11 Jan 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["PhysicsSem1MidSem2"])
def handle_message(message):
    file1_path="PHIR11 Feb 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["PhysicsSem1EndSem"])
def handle_message(message):
    file1_path="PHIR11 Dec 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="PHIR11 Dec 2018 Reappear (Old Scheme).pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="PHIR11 Mar 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="PHIR11 Nov 2017.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["PSPS"])
def handle_message(message):
    bot.reply_to(message,"/PSPSMidSem1\n/PSPSMidSem2\n/PSPSEndSem")

@bot.message_handler(commands=["PSPSMidSem1"])
def handle_message(message):
    file1_path="CSIR11 20XX.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 20XXB.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 20XXC.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 2017.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 2018.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 Jan 2022.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 Jan 2021 (EC).pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 Jan 2021 (CS).pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 Jan 2022 EE.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["PSPSMidSem2"])
def handle_message(message):
    file1_path="CSIR11 20XXD.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 Feb 2021 (EC).pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["PSPSEndSem"])
def handle_message(message):
    file1_path="CSIR11 Dec 2017.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 Dec 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 Dec 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSIR11 Mar 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["English"])
def handle_message(message):
    bot.reply_to(message,"/EnglishMidSem1\n/EnglishMidSem2\n/EnglishEndSem")

@bot.message_handler(commands=["EnglishMidSem1"])
def handle_message(message):
    file1_path="HSIR11 Jan 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR11 Jan 2022.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR11 Nov 2018.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["EnglishMidSem2"])
def handle_message(message):
    file1_path="HSIR11 Feb 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["EnglishEndSem"])
def handle_message(message):
    file1_path="HSIR11 Dec 2017.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR11 Dec 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR11 Dec 2019 Reappear (Old Scheme).pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR11 Dec 2019 Reappear.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR11 Dec 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR11 Mar 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR11 May 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
 
@bot.message_handler(commands=["EP"])
def handle_message(message):
    bot.reply_to(message,"/EPMidSem1\n/EPMidSem2\n/EPEndSem")

@bot.message_handler(commands=["EPMidSem1"])
def handle_message(message):
    file1_path="MEIR11 2019.jpg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["EPMidSem2"])
def handle_message(message):
    file1_path="MEIR11 2021.jpeg"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["EPEndSem"])
def handle_message(message):
    file1_path="MEIR11 Dec 2017.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MEIR11 Dec 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MEIR11 Dec 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MEIR11 Mar 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MEIR11 May 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="MEIR11 May 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["Economics"])
def handle_message(message):
    bot.reply_to(message,"/EconomicsMidSem1\n/EconomicsEndSem")

@bot.message_handler(commands=["EconomicsMidSem1"])
def handle_message(message):
    file1_path="HSIR12 Apr 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR12 Jan 2022.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR12 Sep 2018.png"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["EconomicsEndSem"])
def handle_message(message):
    file1_path="HSIR12 Dec 2017.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR12 Dec 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR12 Dec 2019 Reappear.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR12 Dec 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR12 Jun 2021.png"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR12 Mar 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="HSIR12 May 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["DSD"])
def handle_message(message):
    bot.reply_to(message,"/DSDEndSem")

@bot.message_handler(commands=["DSDEndSem"])
def handle_message(message):
    file1_path="CSPC10 Dec 2019 Reappear.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSPC10 May 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSPC10 May 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="ITPC10 Dec 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="ITPC10 May 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="ITPC10 May 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["DSA"])
def handle_message(message):
    bot.reply_to(message,"/DSAMidSem1\n/DSAMidSem2\n/DSAEndSem")

@bot.message_handler(commands=["DSAMidSem1"])
def handle_message(message):
    file1_path="CSPC12 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["DSAMidSem2"])
def handle_message(message):
    file1_path="CSPC12 2021B.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)

@bot.message_handler(commands=["DSAEndSem"])
def handle_message(message):
    file1_path="CSPC12 Dec 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSPC12 Jul 2021.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSPC12 May 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSPC12 May 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="CSPC12 Dec 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="ITPC12 May 2018.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)
    file1_path="ITPC12 May 2019.pdf"
    with open(file1_path,'rb') as file1:
        bot.send_document(message.chat.id,file1)


@bot.message_handler(func=lambda message:True)
def handle_message(message):
    bot.reply_to(message,f"Enter a valid command from /help section")
bot.polling()